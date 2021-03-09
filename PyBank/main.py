#modules
import os 
import csv

#set path for the csv file
pybank_data = os.path.join("..", "python-challenge", "PyBank", "Resources", "pybank_data.csv")

with open(pybank_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #print header 
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")


      

