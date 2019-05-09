import csv
from collections import defaultdict

_DATA = defaultdict(list)

reader = csv.DictReader(open("datasets/arabica_data_cleaned.csv", "r"))
for row in reader:
    for fld in reader.fieldnames:
        _DATA[fld].append(row[fld])


def get(field):
    return _DATA[field]
