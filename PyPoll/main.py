import os
import csv
import fileinput

budget_csv = os.path.join('Resources', 'election_data.csv')

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

#   candidate = []
#    for row in csvreader:
#        if row[2] not in candidate:
#            candidate.append(row[2])
#    print(candidate)

    lines = 0
    khan_lines = 0
    correy_lines = 0
    li_lines = 0
    otooley_lines = 0
    other_lines = 0

    pct_list = []

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

    names = ["Correy","Li","O'Tooley","Khan"]

    pct_list.append(correy_pct)
    pct_list.append(li_pct)
    pct_list.append(otooley_pct)
    pct_list.append(khan_pct)

    candidate_stats = zip(names, pct_list)

summary_file = os.path.join("Resources","summary.csv")

with open(summary_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Name", "PctOfVotes"])
    writer.writerows(candidate_stats)

with open(summary_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    pct_max = max(csvreader, key=lambda row: float(row[1]))


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

output_path = os.path.join("analysis", "PyPoll_ElectionResults.txt")

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



