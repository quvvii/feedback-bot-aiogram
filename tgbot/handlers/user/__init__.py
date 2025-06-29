from aiogram import Router
from tgbot.filters.id_filter import IDFilter

from . import handle_message, start

router = Router()
router.message.filter(~IDFilter())

router.include_routers(
    handle_message.router,
    start.router
)
