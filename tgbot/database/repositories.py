from tortoise.exceptions import DoesNotExist
from .models import User, MessageRelations


class UserRepository:
    async def get_user(self, user_id: int) -> User | None:
        try:
            return await User.get(id=user_id)
        except DoesNotExist:
            return None

    async def create_user(self, user_id: int, name: str) -> User:
        return await User.create(id=user_id, name=name)

    async def update_user(self, user_id: int, is_banned: bool) -> None:
        await User.filter(id=user_id).update(is_banned=is_banned)

    async def count_all(self) -> int:
        return await User.all().count()

    async def count_banned(self) -> int:
        return await User.filter(is_banned=True).count()

class MessageRelationsRepository:
    async def get_relation(self, message_id: int) -> MessageRelations | None:
        try:
            return await MessageRelations.get(message_id=message_id)
        except DoesNotExist:
            return None

    async def create_relation(self, message_id: int, user_id: int) -> MessageRelations:
        return await MessageRelations.create(
            message_id=message_id,
            user_id=user_id
        )
