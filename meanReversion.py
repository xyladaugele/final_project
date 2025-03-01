def mean_reversion(df):
    window = 30  # 30-day moving average
    df['SMA'] = df['4. close'].rolling(window=window).mean()

    signal_data = df['4. close'].iloc[-1]
    if signal_data < df['SMA'].iloc[-1] * 0.95:
        print("Buy signal detected!")
    elif signal_data > df['SMA'].iloc[-1] * 1.05:
        print("Sell signal detected!")