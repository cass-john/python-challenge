"""
You will be give a set of poll data called election_data.csv.
The dataset is composed of three columns: Voter ID, County, and Candidate.
Your task is to create a Python script that analyzes the votes and calculates
each of the following:
    - The total number of votes cast
    - A complete list of candidates who received votes
    - The percentage of votes each candidate won
    - The total number of votes each candidate won
    - The winner of the election based on popular vote.
As an example, your analysis should look similar to the one below:
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
"""
import csv
import os
# set path for the csv file
pypoll_data = os.path.join("..", "python-challenge", "PyPoll", "Resources", "pypoll_data.csv")
# Resetting values to 0 and creating lists to store data
total_votes = 0
candidates = []
vote_count = []
percent_votes = []
# Opening and reading the CSV file
with open(pypoll_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # skipping the header row
    csv_header = next(csv_reader)
    # looping through data after header
    for row in csv_reader:
        # count total votes
        total_votes += 1
        # listing all of the candidtaes who received votes
        if row[2] not in candidates:
            candidates.append(str(row[2]))
# Print out our Candidates list to see what Candidates are in it.
print()
print("Candidates List:")
for candidate in candidates:
    print()
    print(f"Candidate: {candidate}")
    print()
      



    