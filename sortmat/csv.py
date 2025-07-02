import csv

with open('numbers.csv') as file:
    reader = csv.reader(file)
    data = list(reader)

header = data[0]
rows = data[1:]

# Remove empty or incomplete rows
rows = [row for row in rows if len(row) == len(header)]

# Sort by Score (3rd column)
rows.sort(key=lambda x: int(x[2]))

print(','.join(header))
for row in rows:
    print(','.join(row))
