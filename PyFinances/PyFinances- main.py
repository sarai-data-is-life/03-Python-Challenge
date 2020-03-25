import os
import csv
#import os.path

list = os.listdir('Resources')
number_files = len(list)

for numbers in range(number_files):

    budget_csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

    #Declare empty list variables

    date = []
    ProLoss = []
    month = []
    year = []
    ProLossChange = []
    Total_ProLoss = 0
    TotalProLossChange = 0
    ProLoss_Start = 0
    itemCount = 0
    
    
    

    with open(budget_csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        next(csvreader, None)

        for row in csvreader:
            itemCount = itemCount + 1
            date.append(row[0])
            ProLoss.append(int(row[1]))
            Total_ProLoss = Total_ProLoss + int(row[1])
            ProLoss_End = int(row[1])
            ProLossDiff = ProLoss_End - ProLoss_Start
            TotalProLossChange = TotalProLossChange + ProLossDiff
            ProLossChange.append(ProLossDiff)
            splitdate = row[0].split('-')
            month.append(str(splitdate[0]))
            year.append(splitdate[1][-2:])
            ProLoss_Start = ProLoss_End

# To determine the greatest increase in profits (date and amount) over the entire period and 
# the greatest decrease in losses (date and amount) over the entire period

averagechange_ProLoss = TotalProLossChange / itemCount
GIncrease = max(ProLossChange)
GDecrease = min(ProLossChange)
IncreaseDate = date[ProLossChange.index(GIncrease)]
DecreaseDate = date[ProLossChange.index(GDecrease)]
CountM = len(set(date))


with open('financial_analysis_report_' + str(numbers+1) + '.txt', 'w') as text:
        text.write("Financial Analysis for file 'budget_data "+ ".csv'"+"\n")
        text.write("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-\n")
        text.write("    Total Months: " + str(CountM) + "\n")
        text.write("    Total Profit and Loss: " + "$" + str(Total_ProLoss) +"\n")
        text.write("    Average Profit and Loss Change: " + '$' + str(int(averagechange_ProLoss)) +'\n')
        text.write("    Greatest Increase in Profit: " + str(IncreaseDate) + " ($" + str(GIncrease) + ")\n")
        text.write("    Greatest Decrease in Loss: " + str(DecreaseDate) + " ($" + str(GDecrease) + ")\n\n")