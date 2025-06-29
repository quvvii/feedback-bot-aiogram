from tortoise.transactions import in_transaction

class UnitOfWork:
    def __init__(self, db_alias: str = "default"):
        self.db_alias = db_alias
        self.transaction = None

    async def __aenter__(self):
        self.transaction = in_transaction(self.db_alias)
        await self.transaction.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.transaction.__aexit__(exc_type, exc_val, exc_tb)
        self.transaction = None
