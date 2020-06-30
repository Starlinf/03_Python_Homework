import os
import csv
import fileinput

budget_csv = os.path.join('Resources', 'budget_data.csv')

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    pl_list = []
    delta_list = []
    lines = 0
    total = 0

    for row in csvreader:
        date = row[0]
        profitloss = int(row[1])
        lines += 1
        total += int(row[1])       
        pl_list.append([date, profitloss])

    monthly_delta = 0

    for i in range(len(pl_list) - 1):
        current_month_row = pl_list[i]
        current_month_date = row[0]
        current_month_price = current_month_row[-1]
        last_month_row = pl_list[i+1]
        last_month_price = last_month_row[-1]
        delta = (last_month_price - current_month_price)
        monthly_delta += delta

        delta_list.append(delta)

        pl_change_max = max(delta_list)
        pl_change_min = min(delta_list)

#        pl_change_max = max(delta_list, key=lambda row: int(row[1]))
#        pl_change_min = min(delta_list, key=lambda row: int(row[1]))


    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {lines}")
    print(f"Total: ${total:.0f}")
    print(f"Average Change: ${monthly_delta / (lines - 1):.2f}")
    print(f"Greatest Increase in Profits: (${pl_change_max:.0f})")
    print(f"Greatest Decrease in Profits: (${pl_change_min:.0f})")

    output_path = os.path.join("analysis", "PyBank_FinanicalAnalysis.txt")
    
    with open(output_path, "w") as textfile:
        textfile.writelines("Financial Analysis" + '\n')
        textfile.writelines("----------------------------" + '\n')
        textfile.writelines(f"Total Months: {lines}" + '\n')
        textfile.writelines(f"Total: ${total:.0f}" + '\n')
        textfile.writelines(f"Average Change: ${monthly_delta / (lines - 1):.2f}" + '\n')
        textfile.writelines(f"Greatest Increase in Profits: (${pl_change_max:.0f})" + '\n')
        textfile.writelines(f"Greatest Decrease in Profits: (${pl_change_min:.0f})" + '\n')














