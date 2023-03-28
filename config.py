import os
from dotenv import load_dotenv


class Config:
    def __init__(self) -> None:
        load_dotenv()
        self.PHONENUMBER = os.getenv("PHONENUMBER")
        self.PASSWORD = os.getenv("PASSWORD")