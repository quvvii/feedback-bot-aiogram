from environs import Env

class Config:
    def __init__(self):
        self.env = Env()
        self.env.read_env()

        self.TOKEN = self.env.str("TELEGRAM_BOT_TOKEN")
        self.ADMIN_ID = self.env.int("TELEGRAM_ADMIN_ID")
        self.DB_URL = self.env.str("DATABASE_URL")
        self.LOGGER_FORMAT = "[%(name)s] [%(asctime)s] [%(levelname)s] - %(message)s"
        self.DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

config = Config()
