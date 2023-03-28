from datetime import date
import pandas as pd

from jqdatasdk import *

class Downloader:
    def __init__(self):
        pass

        # get all stock names
    def get_all_stock_names(self):
        return get_all_securities(['stock']).index.tolist()
    
    # process the data before store to the database
    def process_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """add the index column name to date"""
        df = df.reset_index().rename(columns={'index': 'date'})
        df['paused'] = df['paused'].map({0.0:0, 1.0:1})
        return df 
    
    def get_stock_history_data(self, stock_name: str):  
        df = get_price(stock_name, start_date= '2022-03-28 09:00:00',end_date=date.today(),fq='none', frequency='daily', fields=['open','close','low','high','volume','money','factor',
        'high_limit','low_limit','avg','pre_close','paused'])
        return df