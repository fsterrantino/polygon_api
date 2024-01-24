import pandas as pd
import numpy as np

df = pd.read_csv('./archives/stocks_bars - 2024.01.17.csv', sep=';', usecols=['ticker', 'close_price'])

df['percentage_change'] = df.groupby('ticker')['close_price'].pct_change() * 100

percentage_increase_threshold = 0.5

df['exceeded'] = df['percentage_change'].gt(percentage_increase_threshold)

filtered_df = df[df['exceeded'] | df['exceeded'].shift(-1)]

print(filtered_df)

