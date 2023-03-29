import pandas as pd
import matplotlib.pyplot as plt
from database import Database
from config import Config



app_config = Config() 
mongoClient = Database(
    app_config.DATABASE_HOST,
    int(app_config.DATABASE_PORT),
    "",
    "",
    app_config.DATABASE_NAME,
)

def get_collection(stock_name: str) -> pd.DataFrame:
    data = mongoClient.get_collection(stock_name)
    return pd.DataFrame(list(data))

def plot_single_stock(stock_name: str) -> None:
    df = get_collection(stock_name)
    print(df.columns)
    # print(df.head(5))
    df['close'].plot(title=stock_name)
    plt.title('Stock Close Price')
    plt.xlabel('Date')
    plt.ylabel('Close Price')

    plt.show()

def plot_stocks(stock_names: list) -> None:
    for stock_name in stock_names:
        df = get_collection(stock_name)
        df['close'].plot(title=stock_name)
        plt.title('Stock Close Price')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    stock_list = ['000001.XSHE', '000002.XSHE', '000004.XSHE', '000005.XSHE', '000006.XSHE', '000007.XSHE']
    plot_stocks(stock_list)