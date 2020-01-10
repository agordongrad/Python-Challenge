import csv
import os

budget_file = os.path.join("C:\\Users\\Amanda\\Desktop\\Python-Challenge\\PyBank", "budget_data.csv")
row_count = sum(1 for row in csv.reader( open(budget_file) ) )
print("Total Months: %s" %row_count)


row_count = sum(2 for row in csv.reader( open(budget_file) ) )


 with open(budget_file, newline = '') as budget:
     reader = csv.reader(budget)
     for i in reader:
         print(i)

     total_months = 0
    
     for row in reader:
         row += 1
        

      # The net total amount of "Profit/Losses" over the entire period    
with open(budget_file, newline = '') as budget:
    reader = csv.reader(budget)
    header = next(reader)
    profitnet = 0
    list_profit = []    
    for row in reader:
        #profitnet = profitnet + int(row[1])
        profitnet += int(row[1])
        # to append is to add something together. I needed to append list_profit to my row. row[1] = my row that I named plus [1] which is the second column of the csv file
        list_profit.append(row[1]) 

    print(profitnet)
    print(list_profit)
    # next  I need to subtract each value from the other in order to get the avg of the changes in Profit/Losses
