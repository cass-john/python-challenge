#modules
import os 
import csv

#set path for the csv file
pybank_data = os.path.join("..", "python-challenge", "PyBank", "Resources", "pybank_data.csv")

#Resetting values to 0 and creating lists to store data 
total_months = 0
total_revenue = 0
value = 0
change = 0
dates = []
profits = []

#Opening and reading the CSV file
with open(pybank_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)

    #Reading first row 
    first_row = next(csvreader)
    total_months += 1
    total_revenue += int(first_row[1])
    value = int(first_row[1])
    
    #looping through data after header 
    for row in csvreader:
        # Keeping track of the dates
        dates.append(row[0])
        
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        #Total revenue
        total_revenue = total_revenue + int(row[1])

        #Finding the average change
        avg_change = sum(profits)/len(profits)

        #Finding the greatest increase
        greatest_increase = max(profits)
        greatest_index = profits.index(greatest_increase)
        greatest_date = dates[greatest_index]

        #Find greatest decrease
        greatest_decrease = min(profits)
        worst_index = profits.index(greatest_decrease)
        worst_date = dates[worst_index]

#print data
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_revenue)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#output data to txt
#set output path
pybank_results = os.path.join("..", "python-challenge", "PyBank", "Analysis", "pybank_results.txt")

#write data to txt file
with open(pybank_results, "w", newline="") as text_file:
    writer = csv.writer(text_file)

    text_file.write("Financial Analysis")
    text_file.write("---------------------")
    text_file.write(f"Total Months: {str(total_months)}")
    text_file.write(f"Total: ${str(total_revenue)}")
    text_file.write(f"Average Change: ${str(round(avg_change,2))}")
    text_file.write(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
    text_file.write(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")





        