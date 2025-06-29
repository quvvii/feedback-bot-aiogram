from aiogram import types, Router, Bot, F
from aiogram.utils.markdown import html_decoration as hd

from tgbot.services.database.message_relations import MessageRelationsService
from tgbot.services.database.user_service import UserService
from tgbot.services.utils import time_ago

from config import config

import logging


logger = logging.getLogger(__name__)
router = Router()


@router.message(~F.text.startswith("/"))
async def forward_user_message_to_admin(
    msg: types.Message,
    bot: Bot,
    mr: MessageRelationsService,
    us: UserService
):
    user = msg.from_user
    db_user = await us.get_user_by_id(user.id)

    username = f"📛 Username: @{user.username}\n" if user.username else ""

    user_info = (
        f"👤 Пользователь: {user.mention_html()}\n"
        f"🆔 ID: {hd.code(user.id)}\n"
        f"{username}"
        f"⏰ Создан: {hd.quote(time_ago(db_user.created_at))}" if db_user else ""
    )

    info_msg = await bot.send_message(config.ADMIN_ID, user_info)

    try:
        if msg.video_note:
            sent_msg = await bot.send_video_note(
                chat_id=config.ADMIN_ID,
                video_note=msg.video_note.file_id
            )
        elif msg.voice:
            sent_msg = await bot.send_voice(
                chat_id=config.ADMIN_ID,
                voice=msg.voice.file_id,
                caption=msg.caption
            )
        else:
            sent_msg = await msg.send_copy(config.ADMIN_ID)

        # Сохраняем оригинальное сообщение к админу
        await mr.create_relation(
            message_id=sent_msg.message_id,
            user_id=user.id
        )

        # И еще одно (инфо юзера) если хотим так же иметь возможность отвечать на него
        # (опционально, будет в 2 раза больше связей в бд)
        await mr.create_relation(
            message_id=info_msg.message_id,
            user_id=user.id
        )

        await msg.reply("✅ Ваше сообщение доставлено администратору")

    except Exception as e:
        logger.error(f"Forward error: {e}")
        await msg.reply("⚠ Не удалось отправить сообщение")
