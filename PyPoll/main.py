import os
import csv
import numpy as np

#Specifying path of the csv file
csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

#Reading using csv module
with open(csvpath,encoding="utf-8") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Reading the header row first 
    csv_header = next(csvreader)

    #Initializing the variables
    total_votes = []
    candidates = []
    correy = []
    khan = []
    li = []
    oTooley = []

    # Read each row of data after the header
    for row in csvreader:
    #Adding the elements to the total_votes[], using the first column of the csv file
        total_votes.append(row[0])
        candidates.append(row[2])

        if row[2] == "Correy":
            correy.append(row[1])
        elif row[2] == "Khan":
            khan.append(row[1])
        elif row[2] == "Li":
            li.append(row[1])
        elif row[2] == "O'Tooley":
            oTooley.append(row[1])
            
    #Determining the candidates in the election poll data
    def unique(candidates): 
        x = np.array(candidates) 
        print(np.unique(x)) 
#print("List of candidates in the election is :") 
#unique(candidates) 
#['Correy' 'Khan' 'Li' "O'Tooley"]

#Calculating percentage of votes for each candidate and converting them to 3 decimal places
correy_perc = (len(correy)/len(total_votes) *100)
correy_perc_float = "{:.3f}".format(correy_perc)
khan_perc = (len(khan)/len(total_votes) *100)
khan_perc_float = "{:.3f}".format(khan_perc)
li_perc = (len(li)/len(total_votes) *100)
li_perc_float = "{:.3f}".format(li_perc)
oTooley_perc = (len(oTooley)/len(total_votes) *100)
oTooley_perc_float = "{:.3f}".format(oTooley_perc)

#Calculating winner based on maximum percentage of votes
winner = max(correy_perc, khan_perc, li_perc, oTooley_perc )
#Condition to provide the name of the candidate based on maximum percentage of votes for winner
if winner == correy_perc:
    election_winner = "Correy"
elif winner == khan_perc:
    election_winner = "Khan"
elif winner == li_perc:
    election_winner = "Li"  
elif winner == oTooley_perc:
    election_winner = "O'Tooley"    
#Printing the results to the terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(len(total_votes)))
print("-------------------------")
print(f"Khan : {khan_perc_float}% ({len(khan)})")
print(f"Correy : {correy_perc_float}% ({len(correy)})")
print(f"Li : {li_perc_float}% ({len(li)})")
print(f"O'Tooley : {oTooley_perc_float}% ({len(oTooley)})")
print("-------------------------")
print("Winner: " + election_winner)
print("-------------------------")

# Specifying the path to the file to write the summary
output_path = os.path.join("Analysis", "analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
# Writing the contents to the file    
    txtfile.write("Election Results")
    txtfile.write("\n")
    txtfile.write("-----------------------------")
    txtfile.write("\n")
    txtfile.write("Total Votes: " + str(len(total_votes)))
    txtfile.write("\n")
    txtfile.write("-----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Khan : {khan_perc_float}% ({len(khan)})")
    txtfile.write("\n")
    txtfile.write(f"Correy : {correy_perc_float}% ({len(correy)})")
    txtfile.write("\n")
    txtfile.write(f"Li : {li_perc_float}% ({len(li)})")
    txtfile.write("\n")
    txtfile.write(f"O'Tooley : {oTooley_perc_float}% ({len(oTooley)})")
    txtfile.write("\n")
    txtfile.write("-----------------------------")
    txtfile.write("\n")
    txtfile.write("Winner: " + election_winner)
    txtfile.write("\n")
    txtfile.write("--------------------------")