import csv
from pprint import pprint
import pandas as pd

records = []

with open("ex53.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        records.append(row)

# do you analysis here

df = pd.DataFrame(records)

pprint(df)

df.to_excel("ex54.xlsx")