# although inefficient, this is done using lists and indices as practice!

import csv
import os

# normalized practice should be
# File_path = os.path.join(input("please indicate file location")
File_path = os.path.join('..','..','Instructions','PyPoll','Resources','election_data.csv')

with open(File_path, 'r') as Election_file:
    Election_data = csv.reader(Election_file)
    Header = next(Election_file)

    # this entire section needs to be redone as a dictionary
    Total_voter_count = 0
    Candidate_name_list = []
    Khan_count = 0
    Correy_count = 0
    Li_count = 0
    Otooley_count = 0

    for rows in Election_data:    
        if rows[2] not in Candidate_name_list:
            Candidate_name_list.append(rows[2])
        Total_voter_count += 1

        if rows[2] == "Khan":
            Khan_count += 1
        elif rows[2] == "Correy":
            Correy_count += 1
        elif rows[2] == "Li":
            Li_count += 1
        else:
            Otooley_count += 1

Candidate_count_list = [Khan_count,Correy_count,Li_count,Otooley_count]
Winner = max(Candidate_count_list)
Winner_index = Candidate_count_list.index(Winner)

Candidate_percentage_list = []
for i in range(len(Candidate_count_list)):
    Percentage = round((Candidate_count_list[i]/Total_voter_count)*100, 4)
    Candidate_percentage_list.append(Percentage)

print(f"Election Results\n------------------------------")
print(f"Total Votes: {Total_voter_count}\n------------------------------")
for i in range(len(Candidate_name_list)):
    print(f"{Candidate_name_list[i]}: {Candidate_percentage_list[i]}% ({Candidate_count_list[i]})")
print(f"------------------------------\nWinner: {Candidate_name_list[Winner_index]}\n------------------------------")

Output_path = os.path.join('..', '..', 'Instructions', 'PyPoll', 'Resources')
f = open('fin_output.txt', "w")

f.write(f"Election Results\n------------------------------\n")
f.write(f"Total Votes: {Total_voter_count}\n------------------------------\n")
for i in range(len(Candidate_name_list)):
    f.write(f"{Candidate_name_list[i]}: {Candidate_percentage_list[i]}% ({Candidate_count_list[i]})\n")
f.write(f"------------------------------\nWinner: {Candidate_name_list[Winner_index]}\n------------------------------")

f.close()

# Voter_ID_list = []
# County_list = []
# Candidate_name_list = []

# for row in Election_data:
#     Voter_ID_list.append(row[0])
#     County_list.append(row[1])
#     Candidate_name_list.append(row[2])
