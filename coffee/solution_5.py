from functions import quantile
import data


records = data.get("Total.Cup.Points")

for p in [0.1, 0.25, 0.5, 0.75, 0.9]:
    print("percentile (%d)" % (p * 10), quantile(records, p))
