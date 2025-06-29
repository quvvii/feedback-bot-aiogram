from aiogram import Router
from tgbot.filters.id_filter import IDFilter

from . import start, handle_admin_reply, ban_user


router = Router()
router.message.filter(IDFilter())

router.include_routers(
    start.router,
    handle_admin_reply.router,
    ban_user.router
)
