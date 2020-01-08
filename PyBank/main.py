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
        
with open(budget_file, newline = '') as budget:
    reader = csv.reader(budget)
    header = next(reader)
    profitnet = 0
    for row in reader:
        profitnet += int(row[1])
    print(profitnet)
