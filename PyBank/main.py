import os
import csv

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(csvpath,encoding="utf-8") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
  
    months = []
    sum = 0
    average_change = []

    # Read each row of data after the header
    for row in csvreader:
        months.append(row)
        sum +=int(row[1])
        average_change.append((row+1) - row)


    print("Total months: " + str(len(months)))
    print("Total: " + "$"+ str(sum))
    print(average_change)

