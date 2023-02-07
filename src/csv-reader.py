import csv
import os
import json

data_folder = "data"
file_name = "deal.csv"

fp = os.path.join(data_folder, file_name)

d = {}
keys = None
rows = []
with open(fp, "r", encoding = "utf-8") as f:
    csvfile = csv.reader(f, dialect="excel", delimiter=",", quotechar='"')
    for i, row in enumerate(csvfile):
        if i == 0:
            keys = row
            d = {k: None for k in keys}

        if row[0] in ("3669775299", "3669995209"):
            row_dict = {**d, **{k:v for k, v in zip(keys, row)} }
            rows.append(row_dict)

    with open(os.path.join(data_folder, "deal.json"), "w", encoding="utf-8") as f:
        json.dump(rows, f)
