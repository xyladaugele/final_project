import requests
import json
import pandas as pd
import os

ticker = 'ULTA'
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=3KFTX66MTVG8S61G'
req = requests.get(url)

# for browser- http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=ULTA&outputsize=full&apikey=3KFTX66MTVG8S61G

req_dict = json.loads(req.text)

print(req_dict.keys())

# Time Series (Daily)
# all dates


key1 = "Time Series (Daily)" # dictionary with all prices by date
key2 = '4. close'

csv_file = open(ticker + ".csv", "w")
csv_file.write("Date,ULTA\n")
write_lines = []
for date in req_dict[key1]:
    print(date + "," + req_dict[key1][date][key2]) #print key, value
    # csv_file.write(date + "," + req_dict[key1][date][key2]+"\n") #print key, value
    write_lines.append(date + "," + req_dict[key1][date][key2]+"\n")
    
write_lines = write_lines[::-1]
csv_file.writelines(write_lines)
csv_file.close()

def mean_reversion(df):
    window = 50  # 50-day moving average
    df['SMA'] = df['4. close'].rolling(window=window).mean()
   
    buy_signal = df['4. close'].iloc[-1] < df['SMA'].iloc[-1] * 0.95
    sell_signal = df['4. close'].iloc[-1] > df['SMA'].iloc[-1] * 1.05
   
    if buy_signal:
        print("Buy signal detected!")
    elif sell_signal:
        print("Sell signal detected!")


# # average of the last four days 
# last_four_avg = sum(prices[-4:])/4
# print("last_four_avg:", last_four_avg)

# print()

# # set up iterator values and trading variables
# i = 0
# buy = 0
# total_profit = 0

# # loop through prices
# for price in prices:
#     if i >= 4: # only begin 4 day average once there are 4 days to backtrack to
#         avg = (prices[i] + prices[i - 1] + prices[i - 2] + prices[i - 3]) / 4
#         if price < avg and buy == 0: # buy conditions
#             buy = price
#             print("Buying at:", "\t", price)
#         elif price > avg and buy != 0: # sell conditions
#             trade_profit = price - buy
#             print("Selling at:", "\t", price)
#             print("Trade profit:", "\t", trade_profit)
#             total_profit += trade_profit
#             buy = 0
            
#     i += 1
   
# print("total_profit:", "\t", total_profit)