from tgbot.database.uow import UnitOfWork
from tgbot.database.repositories import MessageRelationsRepository
from tgbot.services.schemas import MessageRelations as MessageSchema


class MessageRelationsService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self.repo = MessageRelationsRepository()

    async def create_relation(self, message_id: int, user_id: int) -> MessageSchema:
        async with self.uow:
            relation = await self.repo.get_relation(message_id)

            if not relation:
                relation = await self.repo.create_relation(
                    message_id=message_id,
                    user_id=user_id
                )

            return MessageSchema.from_orm(relation)

    async def get_relation(self, message_id: int) -> MessageSchema | None:
        async with self.uow:
            relation = await self.repo.get_relation(message_id)

            if relation is None:
                return None

            return MessageSchema.from_orm(relation)
