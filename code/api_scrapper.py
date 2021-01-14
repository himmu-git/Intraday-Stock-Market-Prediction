import requests
import pandas as pd 

myapi="AX455WGGI9P6Z5TO"
symbol="TSLA"
t_frame="1"
t_interval="year1month3"
url=f"https://www.alphavantage.co/query?"
params={'function': 'TIME_SERIES_INTRADAY_EXTENDED',
           'symbol': 'TSLA',
           'interval': '1min',
           'slice': 'year1month4',
           'apikey': 'AX455WGGI9P6Z5TO'}
#url=f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={symbol}&interval={t_frame}min&slice={t_interval}&apikey={myapi}"

#print(url)
#%%
response= requests.get(url, params=params)
#%%
#print(response)
r= response.text
print(type(r))
#%%
import csv
wrapper = csv.reader(response.text.strip().split('\n'))
i=0
arr=[]
for temp in wrapper:
    arr.append(temp)
#%%
print(type(wrapper))
csvfile=open("sample.csv", 'w') 
csvwriter = csv.writer(csvfile)
csvwriter.writerows(arr)
#%%
print(arr[1])