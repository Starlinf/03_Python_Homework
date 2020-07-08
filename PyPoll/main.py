# Import Modules for reading CSV files
import os
import csv
import fileinput

# Save the inital data path
budget_csv = os.path.join('Resources', 'election_data.csv')

# Open and read csv
with open(budget_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)    
    csv_header = next(csvfile)

    # Set variables for loop
    lines = 0
    khan_lines = 0
    correy_lines = 0
    li_lines = 0
    otooley_lines = 0
    other_lines = 0

    # List to store percentages
    pct_list = []

    # Read through rows to calculate candidate counts and percentages
    for row in csvreader:
        lines += 1
        if row[2] == "Khan":
            khan_lines += 1
            khan_pct = (khan_lines / lines) * 100
        elif row[2] == "Correy":
            correy_lines += 1
            correy_pct = (correy_lines / lines) * 100
        elif row[2] == "Li":
            li_lines += 1
            li_pct = (li_lines / lines) * 100
        elif row[2] == "O'Tooley":
            otooley_lines += 1
            otooley_pct = (otooley_lines / lines) * 100
        else:
            other_lines += 1
            other_pct = (other_lines / lines) * 100

    # Store names list
    names = ["Correy","Li","O'Tooley","Khan"]

    # Add percentages to stored list pct_list
    pct_list.append(correy_pct)
    pct_list.append(li_pct)
    pct_list.append(otooley_pct)
    pct_list.append(khan_pct)

    # Zip names list and pct_list together into tuples
    candidate_stats = zip(names, pct_list)

# Save the summary path
summary_file = os.path.join("Resources","summary.csv")

# Open the summary file and write zipped rows 
with open(summary_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Name", "PctOfVotes"])
    writer.writerows(candidate_stats)

# Open the summary file and find the max percentage
with open(summary_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    pct_max = max(csvreader, key=lambda row: float(row[1]))

# Print analysis to terminal
print("Election Results")
print("------------------------")
print(f"Total Votes: {lines}")
print("------------------------")
print(f"Khan: {khan_pct:.03f}% ({khan_lines})")
print(f"Correy: {correy_pct:.03f}% ({correy_lines})")
print(f"Li: {li_pct:.03f}% ({li_lines})")
print(f"O'Tooley: {otooley_pct:.03f}% ({otooley_lines})")
print("------------------------")
print(f"Winner: {pct_max[0]}")
print("------------------------")

# Save text file path
output_path = os.path.join("analysis", "PyPoll_ElectionResults.txt")

# Export results to a text file
with open(output_path, "w") as textfile:
    textfile.writelines("Election Results" + '\n')
    textfile.writelines("------------------------" + '\n')
    textfile.writelines(f"Total Votes: {lines}" + '\n')
    textfile.writelines("------------------------" + '\n')
    textfile.writelines(f"Khan: {khan_pct:.03f}% ({khan_lines})" + '\n')
    textfile.writelines(f"Correy: {correy_pct:.03f}% ({correy_lines})" + '\n')
    textfile.writelines(f"Li: {li_pct:.03f}% ({li_lines})" + '\n')
    textfile.writelines(f"O'Tooley: {otooley_pct:.03f}% ({otooley_lines})" + '\n')
    textfile.writelines("------------------------" + '\n')
    textfile.writelines(f"Winner: {pct_max[0]}" + '\n')
    textfile.writelines("------------------------" + '\n')



