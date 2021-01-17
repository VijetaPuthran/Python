import os
import csv
from statistics import mean

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(csvpath,encoding="utf-8") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    #Initializing the variables
    months = []
    sum = 0
    profit_losses = []
    profit_loss_change = []
    average = 0

    # Read each row of data after the header
    for row in csvreader:
    #Adding the elements to the months[], using the first column of the csv file
        months.append(row[0])
    #Net total of Profit/Losses over the entire period, using the second column of the csv file     
        sum +=int(row[1])
    #Adding the elements to the profit_losses[], using the second column of the csv file 
        profit_losses.append(int(row[1]))
    #For loop to iterate through the profit_losses[] to calculate the change in profit/loss        
    for row in range(len(profit_losses)-1):
        profit_loss_change.append(profit_losses[row+1]-profit_losses[row])
    #Python in-built function to calculate mean
    def Average(profit_loss_change):
        return mean(profit_loss_change)

    average = Average(profit_loss_change)
    #Calculation to get the index of the month from the month[], for max and min changes in profit/loss respectively
    max_month = profit_loss_change.index(max(profit_loss_change)) + 1
    min_month = profit_loss_change.index(min(profit_loss_change)) + 1
    max_month_profit_loss_change = months[max_month]
    min_month_profit_loss_change = months[min_month]

    print("Financial Analysis")
    print("----------------------------")
    print("Total months: " + str(len(months)))
    print("Total: " + "$"+ str(sum))
    print("Average Change: " + "$"+ str(round(average, 2)))
    print("Greatest Increase in Profits: " + str(max_month_profit_loss_change) + " " +"($" + str(max(profit_loss_change)) +")")
    print("Greatest Decrease in Profits: " + str(min_month_profit_loss_change) + " " +"($" + str(min(profit_loss_change)) +")")

    # Specifying the path to the file to write the summary
output_path = os.path.join("Analysis", "analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis")
    txtfile.write("\n")
    txtfile.write("----------------------------")
    txtfile.write("\n")
    txtfile.write("Total months: " + str(len(months)))
    txtfile.write("\n")
    txtfile.write("Total: " + "$"+ str(sum))
    txtfile.write("\n")
    txtfile.write("Average Change: " + "$"+ str(round(average, 2)))
    txtfile.write("\n")
    txtfile.write("Greatest Increase in Profits: " + str(max_month_profit_loss_change) + " " +"($" + str(max(profit_loss_change)) +")")
    txtfile.write("\n")
    txtfile.write("Greatest Decrease in Profits: " + str(min_month_profit_loss_change) + " " +"($" + str(min(profit_loss_change)) +")")



    

