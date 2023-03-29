import os
from dotenv import load_dotenv


class Config:
    def __init__(self) -> None:
        load_dotenv()
        self.PHONENUMBER = os.getenv("PHONENUMBER")
        self.PASSWORD = os.getenv("PASSWORD")
        self.DATABASE_HOST = os.getenv("DATABASE_HOST")
        self.DATABASE_PORT = os.getenv("DATABASE_PORT")
        self.DATABASE_NAME = os.getenv("DATABASE_NAME")
