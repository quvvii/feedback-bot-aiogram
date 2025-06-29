from tortoise.exceptions import DoesNotExist

from tgbot.database.uow import UnitOfWork
from tgbot.database.repositories import UserRepository
from tgbot.services.schemas import User as UserSchema


class UserService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self.repo = UserRepository()

    async def get_user(self, user_id: int, name: str) -> UserSchema:
        async with self.uow:
            user = await self.repo.get_user(user_id)

            if not user:
                user = await self.repo.create_user(user_id, name)

            return UserSchema.from_orm(user)

    async def get_user_by_id(self, user_id: int) -> UserSchema | None:
        async with self.uow:
            user = await self.repo.get_user(user_id)

            if user is None:
                return None

            return UserSchema.from_orm(user)

    async def ban_user(self, user_id: int, unban: bool = False) -> None:
        async with self.uow:
            await self.repo.update_user(user_id, is_banned=(not unban))

    async def total(self) -> int:
        async with self.uow:
            return await self.repo.count_all()

    async def total_banned(self) -> int:
        async with self.uow:
            return await self.repo.count_banned()
