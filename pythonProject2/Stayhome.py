import pandas as pd

reader=pd.read_csv("cleaned_COVIDDataPull.csv", converters={"FIPSCounty": '{:0>5}'.format})

filtered=reader[reader["PolicyName"].str.contains("Stay at Home")]

for i in filtered["StartDate"]:
    i = pd.to_datetime(i)

#Then sort by datetime
filtered=filtered.sort_values(by=["StartDate"])



filtered.to_csv("Stayhome.csv")