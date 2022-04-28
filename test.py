import csv
file = open("bos2021ModC.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
#print(rows)
print(len(rows))
print(rows[0])
file.close()