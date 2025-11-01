from fetch_data import get_rainfall_timeseries, compare_states_rainfall

df, err = get_rainfall_timeseries("Maharashtra", days=30)
print(err or df.head())

comp = compare_states_rainfall(["Maharashtra", "Karnataka", "Kerala"], days=30)
print(comp)
