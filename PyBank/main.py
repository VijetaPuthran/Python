import os
import csv

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    months = []
    netTotal = []
    sum = 0
    # Read each row of data after the header
    for row in csvreader:
        months.append(row)
        print("The total number of months included in the dataset is " + str(len(months)) + " months.")

    for row1 in csvreader:
        netTotal.append(row1(1)
            for x in netTotal
                sum = sum + x
            print(sum)    

  #  sum = 0
#for x in [1,2,3,4,5]:
 #     sum = sum + x

#print(sum)