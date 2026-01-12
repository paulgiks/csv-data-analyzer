import csv

total = 0
count = 0

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        value = float(row['amount'])
        total += value
        count += 1

average = total / count if count > 0 else 0

print("Total:", total)
print("Average:", average)
