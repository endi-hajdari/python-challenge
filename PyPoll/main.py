# Importing the relevant Python Libraries.
import pandas as pd
import numpy as np

# Reading the CSV dataset.
e_df = pd.read_csv("election_data.csv", header=0)

# Finding the total number of votes cast.
# This is equivalent to counting the number of cells in the "Ballot ID" column of the CSV file.
total_votes=len(e_df)
print("Total Votes: " + str(total_votes))

# Creating a complete list of candidates who received votes.
# This is equivalent to printing the unique values in the "Candidate" column of the CSV file into a list.
unique_candidates = [e_df["Candidate"].unique()]

# Determining the total amount of votes each candidate won.
# This is equivalent to counting the number of rows that are associated with each candidate.
e_df2 = e_df.groupby(["Candidate"])["Candidate"].count().reset_index(name='Counts')
 
print(e_df2)

# Determining the total percentage of votes each candidate won.
# This is equivalent to the following:
#   (1) Counting the number of rows that are associated with each candidate; and
#   (2) 100*(# of rows associated with Candidate i)/(total_votes).
total_percentage= (100*e_df.groupby(["Candidate"])["Candidate"].count()/total_votes).reset_index(name='pCounts')

# print(total_percentage["pCounts"])

# Formatting the results obtained from the last two blocks of code via concatenation.
new_table = e_df2.join(total_percentage["pCounts"])

print(new_table)

# Printing the statistics for each candidate to verify values with those provided on Canvas.
for i in new_table.index:
    update1 = new_table["Candidate"][i] + ":", format(new_table["pCounts"][i],"0.3f") + "%", new_table["Counts"][i]
# print(update1)

# Determining the overall winner of the election based on highest number of votes.
index_winner = new_table.Counts.idxmax()
winner = str(new_table["Candidate"][index_winner])

#print(winner)

# Printing the results of our analysis.
print("Election Results")
print("-------------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------------")
print(str(new_table["Candidate"][0] + ":") + " " + str(format(new_table["pCounts"][0],"0.3f")) + "%" + " " + "("+ str(new_table["Counts"][0])+")")
print(str(new_table["Candidate"][1] + ":") + " " + str(format(new_table["pCounts"][1],"0.3f")) + "%" + " " + "("+ str(new_table["Counts"][1])+")")
print(str(new_table["Candidate"][2] + ":") + " " + str(format(new_table["pCounts"][2],"0.3f")) + "%" + " " + "("+ str(new_table["Counts"][2])+")")
print("-------------------------------------------")
print("Winner: " + str(winner))

# Writing a text file containing the results of the town's electoral analysis.
f = open("PyPoll.txt", "w")
with open("PyPoll.txt", 'a') as f:
    line1 = "Election Results \n \n"
    line2 = "---------------------------------------- \n \n"
    line3 = "Total Votes: " + str(total_votes)
    line4 = "\n \n"
    line5 = "---------------------------------------- \n \n"
    line6 = str(new_table["Candidate"][0] + ":") + " " + str(format(new_table["pCounts"][0],"0.3f")) + "%" + " " + "("+ str(new_table["Counts"][0])+")"
    line7 = "\n"
    line8 = str(new_table["Candidate"][1] + ":") + " " + str(format(new_table["pCounts"][1],"0.3f")) + "%" + " " + "("+ str(new_table["Counts"][1])+")"
    line9 = "\n"
    line10 = str(new_table["Candidate"][2] + ":") + " " + str(format(new_table["pCounts"][2],"0.3f")) + "%" + " " + "("+ str(new_table["Counts"][2])+")"
    line11 = "\n \n"
    line12 = "---------------------------------------- \n \n"
    line13 = "Winner: " + str(winner)
    f.writelines([line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13])
f.close()