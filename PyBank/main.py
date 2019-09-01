# PyBank HW

#import dependencies
import csv
import os
import statistics

pybank_list = []
date_list = []
greatest_inc = 0
greatest_dec = 0
avg = 0
month_count = 0
total_sum = 0

# set file path and open
filePath = os.path.join('..', '..', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')

with open(filePath, 'r') as pybank:
    pybank_reader = csv.reader(pybank)
    pybank_header = next(pybank_reader)

    # list comprehension: for each row in pybank_reader, append the list with the value in row[column index]
    for row in pybank_reader:
        pybank_list.append(row[1])
        date_list.append(row[0]) 
    # pybank_list = [row[1] for row in pybank_reader]
    # date_list = [row[0] for row in pybank_reader] this doesnt work for some reason???

    # print(pybank_list)
    # print(date_list)

    month_count = int(len(pybank_list))   

    # calculate the total sum and make sure all variables are current data types
    for i in range(len(pybank_list)):
        total_sum = int(pybank_list[i]) + total_sum

    # calculate average of each change, starting with a sub list
    change_list = [int(pybank_list[i+1]) - int(pybank_list[i]) for i in range(len(pybank_list) - 1)]
    avg = statistics.mean(change_list)
    

    # calculating the greatest increases and decreases
    greatest_inc = max(change_list)
    maxdex = change_list.index(greatest_inc) + 1

    greatest_dec = min(change_list)
    mindex = change_list.index(greatest_dec) + 1

    # printing time
    print(f"Financial Analysis\n----------------------------\nTotal months: {month_count}")
    print(f"Total: {total_sum}")
    print("Average Change: " + '{:0.2f}'.format(avg))
    print(f"Greatest increase in profits: {date_list[maxdex]} ({greatest_inc})")
    print(f"Greatest decrease in profits: {date_list[mindex]} ({greatest_dec})")

output_path = os.path.join('..', '..', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')
f = open('fin_output.txt', "w")

f.write(f"Financial Analysis\n----------------------------\nTotal months: {month_count}\n")
f.write(f"Total: {total_sum}\n")
f.write("Average Change: " + '{:0.2f}'.format(avg) + "\n")
f.write(f"Greatest increase in profits: {date_list[maxdex]} ({greatest_inc})\n")
f.write(f"Greatest decrease in profits: {date_list[mindex]} ({greatest_dec})\n")

f.close()

