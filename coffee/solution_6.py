from functions import mode, mean
import data


records = [round(float(x)) for x in data.get("Flavor")]

print("Mode", mode(records))
print("Min", min(records))
print("Max", max(records))
print("Mean", mean(records))
