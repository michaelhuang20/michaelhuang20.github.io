import pandas as pd

cars = pd.read_csv("cars2017.csv")
grouped = cars.groupby("Fuel").mean()[["AverageCityMPG"]]
grouped["CarCount"] = cars["Fuel"].value_counts()
grouped = grouped.reset_index()
grouped.to_csv("fuel_group_summary.csv", index=False)
