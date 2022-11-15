# Importing the relevant Python Libraries.
import pandas as pd
import numpy as np

# Reading the CSV dataset and storing the header row.
f_df = pd.read_csv("budget_data.csv", header=0)

# Determining the total number of months included in the dataset.
# This is equivalent to counting the number of cells in the "Date" column of the CSV file.
total_months=len(f_df)
# print("Total Months: " + str(total_months))

# Determining the net total amount of "Profit/Losses" over the entire period.
# This is equivalent to taking the sum of all of the values in the "Profit/Losses" column.
net_total = f_df["Profit/Losses"].sum()
# print("Total: $" +str(int(net_total)))

# Determining the greatest increase in profits (amount) over the entire time period.
# This is equivalent to doing the following:
    # (1) Determining the first differences in the "Profit/Losses" column of our dataset; and
    # (2) Finding the maximum/largest value in the column of first differences using the Pandas DataFrame max() Method.
first_differences = f_df["Profit/Losses"].diff()
largest_val = first_differences.max()

# Determining the greatest increase in profits (date) over the entire time period.
# This is equivalent to the following:
    # (1) Finding the index of largest_val; and
    # (2) Finding the value from f_df in the "Date" column that has the same index as that of largest_val.
index_largest_val = first_differences.idxmax()
v1 = f_df["Date"]
largest_val_date = v1[index_largest_val]
# print("Greatest Increase in Profits: " +str(largest_val_date) + " " + "(" + "$" +str(int(largest_val)) + ")")

# Determining the greatest decrease in profits (amount) over the entire time period.
# This is equivalent to doing the following:
    # (1) Determining the first differences in the "Profit/Losses" column of our data frame (already done in the prior block of code); and
    # (2) Finding the minimum/smallest value in the column of first differences using the Pandas DataFrame min() Method.
smallest_val = first_differences.min()

# Determining the greatest decrease in profits (date) over the entire time period.
# This is equivalent to the following:
    # (1) Finding the index of smallest_val; and
    # (2) Finding the value from f_df in the "Date" column that has the same index as that of smallest_val.
index_smallest_val = first_differences.idxmin()
v2 = f_df["Date"]
smallest_val_date = v2[index_smallest_val]
# print("Greatest Decrease in Profits: " +str(smallest_val_date) + " " + "(" + "$" +str(int(smallest_val)) + ")")

# Determining the changes in "Profit/Losses" over the entire time period.
# This is equivalent to the following:
    # (1) Finding the first differences in the "Profit/Losses" column of our data frame (already done above); and
    # (2) Finding the average of the the first differnces column.
avg_changes = first_differences.mean()
# print("Average Change: " + "$" + str(format(avg_changes, ".2f")))

# Printing the results of our analysis.
print("Financial Analysis")
print("----------------------------------------------------")
print("Total Months: " + str(total_months))
print("Total: $" +str(int(net_total)))
print("Average Change: " + "$" + str(format(avg_changes, ".2f")))
print("Greatest Increase in Profits: " +str(largest_val_date) + " " + "(" + "$" +str(int(largest_val)) + ")")
print("Greatest Decrease in Profits: " +str(smallest_val_date) + " " + "(" + "$" +str(int(smallest_val)) + ")")

# Writing a text file containing the results of our financial analysis.
f = open("PyBank.txt", "w")
with open("PyBank.txt", 'a') as f:
    line1 = "Financial Analysis \n \n"
    line2 = "----------------------------------------------------- \n \n"
    line3 = "Total Months: " + str(total_months)
    line4 = "\n \n"
    line5 = "Total: $" +str(int(net_total))
    line6 = "\n \n"
    line7 = "Average Change: " + "$" + str(format(avg_changes, ".2f"))
    line8 = "\n \n"
    line9 = "Greatest Increase in Profits: " +str(largest_val_date) + " " + "(" + "$" +str(int(largest_val)) + ")"
    line10 = "\n \n"
    line11 = "Greatest Decrease in Profits: " +str(smallest_val_date) + " " + "(" + "$" +str(int(smallest_val)) + ")"
    f.writelines([line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11])
f.close()