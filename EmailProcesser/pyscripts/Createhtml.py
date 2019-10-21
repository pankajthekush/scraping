import csv

with open(r"C:\etemp\localdb.csv",encoding='utf-8-sig',mode="r") as file:
    next(file)
    data = csv.reader(file)
    data = next(data)
