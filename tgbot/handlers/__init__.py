from aiogram import Dispatcher, F

from . import admin, user


def setup_routers(dp: Dispatcher):
    dp.message.filter(F.chat.type == "private")

    dp.include_routers(
        user.router,
        admin.router
    )
