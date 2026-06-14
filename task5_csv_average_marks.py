import csv

total = 0
count = 0

with open("marks.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        print("Name:", row["name"])
        print("Marks:", row["marks"])

        total = total + int(row["marks"])
        count = count + 1

if count > 0:

    average = total / count

    print("\nAverage Marks =", average)

else:

    print("No records found in CSV file")