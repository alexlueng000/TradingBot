from database import Database
from config import Config

from infra.base_object import MongoBaseModel

config = Config()
db = Database(config)


class StockService(MongoBaseModel):
    def __init__(self):
        pass

    def get_all_stocks(self):
        return db.get_all_stocks()