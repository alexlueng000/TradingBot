from pymongo import MongoClient
from jqdatasdk import *
from datetime import date

import pandas as pd

"""
get_price(security, start_date=None, end_date=None, frequency='daily', fields=['open','close','low','high','volume','money','factor',
        'high_limit','low_limit','avg','pre_close','paused'], skip_paused=False, fq='pre', count=None)

df =get_price('000001.XSHE', start_date= '2022-01-28 09:00:00',end_date='2022-01-30 14:00:00',fq='post', frequency='daily', fields=['open','close','low','high','volume','money','factor',
        'high_limit','low_limit','avg','pre_close','paused'])
"""

# write a function that checks the connection to mongoDB    
def check_mongo_connection():
    try:
        client = MongoClient('localhost', 27017)
        client.server_info()
    except:
        print('No connection')
    else:
        print('Connected to MongoDB')


# get all stock names
def get_all_stock_names():
    return get_all_securities(['stock']).index.tolist()


# write a function to get the infomaiton of a single stock
def get_stock_info(stock_name):
    stock_info = get_security_info(stock_name)
    print(stock_info.display_name)  


def read_data_from_csv(file_name: str):
    df = pd.read_csv(file_name)
    print(df)
    return df


# save data to csv
def save_data_to_csv(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(filename + '.csv', index=False)


def get_stock_history_data(stock_name):  
    df = get_price(stock_name, start_date= '2022-03-28 09:00:00',end_date=date.today(),fq='none', frequency='daily', fields=['open','close','low','high','volume','money','factor',
        'high_limit','low_limit','avg','pre_close','paused'])
    return df


# process the data before store to the database
def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """add the index column name to date"""
    df = df.reset_index().rename(columns={'index': 'date'})
    df['paused'] = df['paused'].map({0.0:0, 1.0:1})
    return df 

# print simple data
def print_data(df: pd.DataFrame, lines: int = 5):
    print(df.head(lines))
    # print(df.tail(lines))
    print(df.shape)
    print(df.info())


# downdload  all the data from the API and save it to mongoDB
# start date: 2022-01-01
# end date: now
# frequency: daily
# stock name: 'AAPL'
def download_and_save_data(stock_name):
    # download the data
    # data = requests.get(url).json()
    # save the data to mongoDB
    


    client = MongoClient()
    db = client['gpt_trading']
    collection = db['stock_name']
    if collection is None:
        collection = db.create_collection(stock_name)
        collection.insert_many(data)
    else:
        collection.update_many({}, {'$set': data})

    print('Data downloaded and saved to MongoDB')
    


if __name__ == '__main__':
    auth('19128326936', 'Turkey414')
    pingan = get_stock_history_data('000001.XSHE')
    # print(pingan)
    # stock_list = get_all_stock_names()

    # print("total: ", len(stock_list))
    # history_data = get_stock_history_data('000001.XSHE')
    history_data = read_data_from_csv('zhongguopingan.csv')
    history_data = process_data(history_data)
    print_data(history_data)
    # save_data_to_csv(history_data, 'zhongguopingan')
    