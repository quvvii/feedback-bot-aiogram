from aiogram import BaseMiddleware
from typing import Any, Awaitable, Callable, Dict
from aiogram.types import TelegramObject, User as TelegramUser

from tgbot.services.database.message_relations import MessageRelationsService
from tgbot.services.database.user_service import UserService
from tgbot.database.uow import UnitOfWork


class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        user: TelegramUser | None = getattr(event, "from_user", None)

        uow = UnitOfWork()
        us = UserService(uow)
        mr = MessageRelationsService(uow)

        if user and user.id:
            db_user = await us.get_user(user.id, user.full_name)

            if db_user.is_banned:
                return

            data["user"] = db_user

        data["us"] = us
        data["mr"] = mr

        return await handler(event, data)
