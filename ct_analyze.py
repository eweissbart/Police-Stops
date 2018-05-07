import csv

with open('CT_Cleaned.csv', 'r') as f:
    rows = csv.reader(f)
    for x in rows:
        print(x)
