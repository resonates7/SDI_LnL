import os
import pandas as pd

api_token = os.environ['eod_token']

def get_stock_price(ticker):
    #create an empty dataframe
    eod_df=pd.DataFrame()
    query_string=f'https://eodhistoricaldata.com/api/eod/{ticker}.US?from=1990-01-01&to=2022-06-01&period=d&api_token={api_token}'
    eod_df=pd.read_csv(query_string)

    print(eod_df)

print(api_token)
get_stock_price('aapl')
