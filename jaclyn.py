import requests
import json

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

# def mean_reversion():
#     avg_price = ['4. close'].mean()  # Average price of the stock (mean)
#     last_price = ['4. close'].iloc[-1]  # Last price in the data (the most recent price)

#     # Check for buy or sell signals based on the mean reversion strategy
#     if last_price > avg_price * 1.05:  # If last price is greater than 105% of average (sell)
#         print(f"Sell signal: Price is {last_price} which is more than 5% higher than the average ({avg_price})")
#     elif last_price < avg_price * 0.95:  # If last price is less than 95% of average (buy)
#         print(f"Buy signal: Price is {last_price} which is more than 5% lower than the average ({avg_price})")
#     else:
#         print(f"No signal: Price is {last_price} which is within 5% of the average ({avg_price})")

def mean_reversion(prices):
    # Calculate the average price (mean) from the prices list
    avg_price = sum(prices) / len(prices)

    # Get the last (most recent) closing price from the list
    last_price = prices[-1]

    # Print out the last price and the average price for debugging
    print(f"Last Price: {last_price}, Average Price: {avg_price}")

    # Buy signal: If the last price is 5% lower than the average price
    if last_price < avg_price * 0.95:
        print(f"Buy signal: Price is {last_price} which is more than 5% lower than the average ({avg_price})")
    
    # Sell signal: If the last price is 5% higher than the average price
    elif last_price > avg_price * 1.05:
        print(f"Sell signal: Price is {last_price} which is more than 5% higher than the average ({avg_price})")
    
    # No signal: If the last price is within 5% of the average price
    else:
        print(f"No signal: Price is {last_price} which is within 5% of the average ({avg_price})")

# 8. Extract all closing prices from the 'Time Series (Daily)' data
closing_prices = [float(req_dict[key1][date][key2]) for date in req_dict[key1]]

# 9. Call the mean reversion strategy function with the list of closing prices
mean_reversion(closing_prices)