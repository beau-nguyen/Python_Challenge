# Dependencies
import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(csvpath, newline='') as csvfile:
        
    #variables
    month_count=[]
    profit=[]
    change_profit=[]
    
    # Initialize csv.writer
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}") 
    
 
    for row in csvreader: 
        month_count.append(row[0])
        profit.append(int(row[1]))

    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])

    #max and min
    increase= max(change_profit)
    decrease= min(change_profit)

    # using the index
    import numpy as np
    month_increase= np.argmax(change_profit)+1  
    month_decrease= np.argmin(change_profit)-1




    print("Financial Analysis")
    print("-------------------")
    print(f"Total Months:{len(month_count)}")
    print(f"Total Profit: ${sum(profit)}")
    print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    print(f"Greatest Increase in Profits: {month_count[month_increase]} ${increase}")
    print(f"Greatest Decrease in Profits: {month_count[month_decrease]} ${decrease}")

text_file = open("main.txt","w",newline='')

text_file.write(("Finacial Analysis"))
text_file.write("---------------")
text_file.write(f"Total Months:{len(month_count)}")
text_file.write(f"Total Profit: ${sum(profit)}")
text_file.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
text_file.write(f"Greatest Increase in Profits: {month_count[month_increase]} ${increase}")
text_file.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} ${decrease}")
text_file.close()
