from aiogram import Router, types, filters
from aiogram.utils.markdown import html_decoration as hd

from tgbot.services.database.user_service import UserService
from tgbot.services.database.message_relations import MessageRelationsService


router = Router()

@router.message(filters.Command("ban"))
async def handle_ban_user_cmd(
    msg: types.Message,
    us: UserService,
    mr: MessageRelationsService
):
    if msg.reply_to_message:
        relation = await mr.get_relation(msg.reply_to_message.message_id)

        if not relation:
            return await msg.reply("❌ Не удалось найти пользователя")

        user_id = relation.user_id

    else:
        sl = msg.text.split()

        if len(sl) == 2 and sl[1].isdigit():
            user_id = int(sl[1])
        else:
            return await msg.reply("❌ Не удалось найти пользователя")

    user = await us.get_user_by_id(user_id)

    if not user:
        return await msg.reply("❌ Не удалось найти пользователя")

    await us.ban_user(user.id)
    await msg.reply(f"Пользователь {hd.bold(user.name)} был забанен.")


@router.message(filters.Command("unban"))
async def handle_unban_user_cmd(
        msg: types.Message,
        us: UserService,
        mr: MessageRelationsService
):
    if msg.reply_to_message:
        relation = await mr.get_relation(msg.reply_to_message.message_id)

        if not relation:
            return await msg.reply("❌ Не удалось найти пользователя")

        user_id = relation.user_id

    else:
        sl = msg.text.split()

        if len(sl) == 2 and sl[1].isdigit():
            user_id = int(sl[1])
        else:
            return await msg.reply("❌ Не удалось найти пользователя")

    user = await us.get_user_by_id(user_id)

    if not user:
        return await msg.reply("❌ Не удалось найти пользователя")

    await us.ban_user(user.id, unban=True)
    await msg.reply(f"Пользователь {hd.bold(user.name)} был разбанен.")
