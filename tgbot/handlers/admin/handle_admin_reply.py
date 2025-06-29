from aiogram import Router, Bot, types, F, exceptions

from tgbot.services.database.message_relations import MessageRelationsService

import logging


logger = logging.getLogger(__name__)
router = Router()

@router.message(~F.text.startswith("/") & F.reply_to_message)
async def handle_admin_reply(
    msg: types.Message,
    bot: Bot,
    mr: MessageRelationsService
):
    relation = await mr.get_relation(
        message_id=msg.reply_to_message.message_id
    )

    if not relation:
        return await msg.reply("❌ Не удалось найти получателя")

    try:
        if msg.video_note:
            await bot.send_video_note(
                chat_id=relation.user_id,
                video_note=msg.video_note.file_id
            )

        elif msg.voice:
            await bot.send_voice(
                chat_id=relation.user_id,
                voice=msg.voice.file_id,
                caption=msg.caption
            )

        else:
            await msg.send_copy(relation.user_id)

        await msg.reply("✅ Ответ отправлен пользователю")

    except exceptions.TelegramForbiddenError:
        await msg.reply("❌ Пользователь заблокировал бота")

    except Exception as e:
        logger.error(f"Reply error: {e}")
        await msg.reply(f"❌ Ошибка: {e}")
