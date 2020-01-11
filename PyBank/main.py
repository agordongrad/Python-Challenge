import os, csv
from pathlib import Path 
budget_file = os.path.join("C:\\Users\\Amanda\\Desktop\\Python-Challenge\\PyBank", "budget_data.csv")
totalMonths = []
totalProfit = []
monthlyProfitChange = []
with open(budget_file,newline="", encoding="utf-8") as budget:
     csvreader = csv.reader(budget,delimiter=",") 
     header = next(csvreader) 
     for row in csvreader:
        totalMonths.append(row[0])  # creating a an empty list and then dumping data into that list. Jan2010 is the oth index in the array
        totalProfit.append(int(row[1])) # '867884' second index. Have to put int bc there are no quotes around the number
#print(totalMonths)
#print(totalProfit) 
for i in range(len(totalProfit)-1): # -1 one is to condense from 10 to 9 bc it starts from 0
    monthlyProfitChange.append(totalProfit[i+1]-totalProfit[i]) 
maxIncreaseValue = max(monthlyProfitChange)
maxDecreaseValue = min(monthlyProfitChange)
#add plus one so you are perfectly alligned. If you do not complete this step you will be one index off.
maxIncreaseMonth = monthlyProfitChange.index(max(monthlyProfitChange)) + 1
maxDecreaseMonth = monthlyProfitChange.index(min(monthlyProfitChange)) + 1 
print(maxIncreaseValue)
print(maxDecreaseValue)
print(monthlyProfitChange)
print(maxIncreaseMonth)
print(maxDecreaseMonth)
print(f"Average Change: {(sum(monthly_profit_change)/len(monthly_profit_change))}")
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {len(totalMonths)}")
print(f"Total: ${sum(totalProfit)}")
print(f"Average Change: {(sum(monthly_profit_change)/len(monthly_profit_change))}")
print(f"Greatest Increase in Profits: {totalMonths[maxIncreaseMonth]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {totalMonths[maxDecreaseMonth]} (${(str(max_decrease_value))})")
