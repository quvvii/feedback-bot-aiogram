from aiogram import Dispatcher

from . import user_middleware


def setup_middlewares(dp: Dispatcher):
    dp.message.middleware(user_middleware.UserMiddleware())
