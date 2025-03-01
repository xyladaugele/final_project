# # in downloaded pip packages in the terminal

# from dotenv import load_lotenv

# load_dotenv()

# #dowloading the environment I need to read the spotify files

# client_id = os.getenv("client_id")
# client_secret = os.getenv("client_secret")

# print (client_id, client_secret)
import requests
import json
import pandas as pd

# 1. Fetch data from the API
ticker = 'ULTA'
url = f'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full&apikey=JXXKB6YLITRTY12X'
req = requests.get(url)
req_dict = json.loads(req.text)

# 2. Define keys for time series and close price
key1 = "Time Series (Daily)"  # Dictionary with all prices by date
key2 = '4. close'  # Close price for each day

# 3. Extract and prepare the data
dates = list(req_dict[key1].keys())  # All available dates
dates.sort()  # Sort dates in ascending order

# 4. Prepare a list of closing prices sorted by date
closing_prices = [float(req_dict[key1][date][key2]) for date in dates]

# 5. Create a DataFrame to store the closing prices and calculate the moving average
df = pd.DataFrame({
    'Date': dates,
    '4. close': closing_prices
})

# Calculate the 30-day moving average (SMA)
window = 30
df['SMA'] = df['4. close'].rolling(window=window).mean()

# 6. Define the mean reversion strategy
def mean_reversion(df):
    # Get the last (most recent) closing price and the 30-day moving average
    last_price = df['4. close'].iloc[-1]
    sma = df['SMA'].iloc[-1]

    # Print out the last price and the moving average for debugging
    print(f"Last Price: {last_price}, 30-Day Moving Average: {sma}")

    # Buy signal: If the last price is 5% lower than the moving average
    if last_price < sma * 0.95:
        print(f"Buy signal: Price is {last_price} which is more than 5% lower than the moving average ({sma})")
    
    # Sell signal: If the last price is 5% higher than the moving average
    elif last_price > sma * 1.05:
        print(f"Sell signal: Price is {last_price} which is more than 5% higher than the moving average ({sma})")
    
    # No signal: If the last price is within 5% of the moving average
    else:
        print(f"No signal: Price is {last_price} which is within 5% of the moving average ({sma})")

# 7. Call the mean reversion strategy with the DataFrame
mean_reversion(df)

# import requests
# import json
# import numpy
# import pandas as pd
# import os

# # 1. Fetch the stock data from the API
# ticker = 'ULTA'
# url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=JXXKB6YLITRTY12X'
# req = requests.get(url)

# req_dict = json.loads(req.text)

# print(req_dict.keys())

# # 2. Define keys for time series and close price
# key1 = "Time Series (Daily)"  # Dictionary with all prices by date
# key2 = '4. close'  # Close price for each day

# # 3. Prepare data for CSV export
# csv_file = open(ticker + ".csv", "w")
# csv_file.write("Date,ULTA\n")
# write_lines = []

# # Extract and save the data for the last 30 days
# dates = list(req_dict[key1].keys())  # All available dates
# dates.sort()  # Sort dates in ascending order
# closing_prices = []

# # Loop through dates and collect close prices
# for date in dates:
#     closing_price = req_dict[key1][date][key2]
#     print(date + "," + closing_price)  # Print the date and close price
#     write_lines.append(date + "," + closing_price + "\n")
#     closing_prices.append(float(closing_price))  # Convert to float for calculations

# # Reverse the lines to have data from earliest to latest and write to CSV
# write_lines = write_lines[::-1]
# csv_file.writelines(write_lines)  # Write all the lines at once

# def mean_reversion(df):
#     window = 30  # 30-day moving average
#     df['SMA'] = df['4. close'].rolling(window=window).mean()

#     signal_data = df['4. close'].iloc[-1]
#     if signal_data < df['SMA'].iloc[-1] * 0.95:
#         print("Buy signal detected!")
#     elif signal_data > df['SMA'].iloc[-1] * 1.05:
#         print("Sell signal detected!")
# def mean_reversion(prices):
#     # Calculate the average price (mean) from the prices list
#     avg_price = sum(prices) / len(prices)

#     # Get the last (most recent) closing price from the list
#     last_price = prices[-1]

#     # Print out the last price and the average price for debugging
#     print(f"Last Price: {last_price}, Average Price: {avg_price}")

#     # Buy signal: If the last price is 5% lower than the average price
#     if last_price < avg_price * 0.95:
#         print(f"Buy signal: Price is {last_price} which is more than 5% lower than the average ({avg_price})")
    
#     # Sell signal: If the last price is 5% higher than the average price
#     elif last_price > avg_price * 1.05:
#         print(f"Sell signal: Price is {last_price} which is more than 5% higher than the average ({avg_price})")
    
#     # No signal: If the last price is within 5% of the average price
#     else:
#         print(f"No signal: Price is {last_price} which is within 5% of the average ({avg_price})")

# # 8. Extract all closing prices from the 'Time Series (Daily)' data
# closing_prices = [float(req_dict[key1][date][key2]) for date in req_dict[key1]]

# # 9. Call the mean reversion strategy function with the list of closing prices
# mean_reversion(closing_prices)