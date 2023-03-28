from jqdatasdk import *

from downloader import Downloader
from config import Config
from database import Database
import pandas as pd

config = Config()
auth(config.PHONENUMBER, config.PASSWORD)

downloader = Downloader()
mongoClient = Database(
    host='localhost',
    port=27017,
    username="",
    password="",
    database="gpt-trading",
)


# download ten stocks' history data
def test_download_stock_history_data():
    stock_infos = mongoClient.get_collection('stock_code')
    # print(stock_infos)
    for doc in stock_infos[:10]:
        # print(doc['stock_code'])
        data = downloader.get_stock_history_data(doc['stock_code'])
        mongoClient.insert(doc['stock_code'], data)

def test_get_all_stock_names():
    config = Config()
    # print(config.PHONENUMBER, config.PASSWORD)

    auth(config.PHONENUMBER, config.PASSWORD)

    downloader = Downloader()

    for stock in downloader.get_all_stock_names()[0:5]:
        print(stock)

def test_download_and_save():
    
    config = Config()
        # print(config.PHONENUMBER, config.PASSWORD)
    
    auth(config.PHONENUMBER, config.PASSWORD)

    downloader = Downloader()

    mongoClient = Database(
        host='localhost',
        port=27017,
        username="",
        password="",
        database="gpt-trading",
    )

    print(mongoClient.test_connection())

    # for stock in downloader.get_all_stock_names:
    #     data = downloader.get_stock_history_data(stock)
    #     mongoClient.insert(stock, data)
    stock = '000001.XSHE'
    data = downloader.get_stock_history_data(stock)
    mongoClient.insert(stock, data)

# this function will not execute again
def download_stock_code():
    config = Config()
    auth(config.PHONENUMBER, config.PASSWORD)

    downloader = Downloader()
    stocks = downloader.get_all_stock_names()

    with open('stock_code.txt', 'w') as f:
        for stock in stocks:
            f.write(stock + '\n')


def download_and_save_stock_info():

    dataframe = pd.DaaFrame()
    

    config = Config()
    auth(config.PHONENUMBER, config.PASSWORD)

    downloader = Downloader()
    # stocks = downloader.get_all_stock_names()

    # for stock in stocks:


def save_data():


    stock_code_data_frame = pd.DataFrame()
    count = 0

    with open('stock_code.txt', 'r') as f:
        stocks = f.readlines()
        for stock_code in stocks:
            if count == 5:
                return
            stock_code = stock_code.strip('\n')
            stock_info = get_security_info(stock_code)
            # add the stock to stock_code_data_frame
            stock_code_data_frame.append(stock_info, ignore_index=True)
            data = downloader.get_stock_history_data(stock_code)
            mongoClient.insert(stock_code, data)
            count += 1
        
    print(stock_code_data_frame)
    mongoClient.insert('stock_code', stock_code_data_frame)


def save_all_stock_info():
    config = Config()
    auth(config.PHONENUMBER, config.PASSWORD)

    mongoClient = Database(
        host='localhost',
        port=27017,
        username="",
        password="",
        database="gpt-trading",
    )
    

    df = get_all_securities(types=['stock'])    
    df = df.reset_index().rename(columns={'index': 'stock_code'})
    df = df.reset_index().rename(columns={'index': 'id'})

    mongoClient.insert('stock_code', df)
    


def main():
    config = Config()

    auth(config.USERNAME, config.PASSWORD)

    downloader = Downloader()

    mongoClient = Database(
        host='localhost',
        port=27017,
        username="",
        password="",
        database="gpt-trading",
    )

    print(mongoClient.test_connection())

    for stock in downloader.get_all_stock_names:
        data = downloader.get_stock_history_data(stock)
        mongoClient.insert(stock, data)





if __name__ == '__main__':

    # test_download_and_save()
    # test_get_all_stock_names()
    # download_stock_code()

    # config = Config()
    # auth(config.PHONENUMBER, config.PASSWORD)

    # count = get_query_count()
    # print(count)
    # read_txt()
    # save_all_stock_info()
    test_download_stock_history_data()