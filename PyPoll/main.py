#modules
import os 
import csv

#set path for the csv file
pypoll_data = os.path.join("..", "python-challenge", "PyPoll", "Resources", "pypoll_data.csv")

#Resetting values to 0 and creating lists to store data 
total_votes = 0
candidates = []
vote_count = []
percent_votes = []

#Opening and reading the CSV file
with open(pypoll_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)


    #looping through data after header 
    for row in csvreader:

        #count total votes
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            vote_count.append(1)
        else:
            index = candidates.index(row[2])
            vote_count[index] += 1