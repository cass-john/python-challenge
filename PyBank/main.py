#modules
import os 
import csv

#lists to store data


#reset values at 0
total_months = 0
total_revenue = 0
avg_revenue_change = 0
greatest_increase = 0
greatest_decrease = 0

#set path for the csv file
pybank_data = os.path.join("..", "python-challenge", "PyBank", "Resources", "pybank_data.csv")

with open(pybank_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #read header row first and print header 
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")



        