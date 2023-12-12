import os
import csv

election_data_csv = os.path.join("..", "Resources", "election_data.csv")
output_file = os.path.join("..", "analysis", "election_results.txt")

with open(output_file, "w") as f:
    f.write("Election Results\n")
    f.write("-" * 20 + "\n")

    # declaring variables
    total_votes = 0
    candidate_votes = {}   
    winner = []   
    max_votes = 0   

    # starting the csv
    with open(election_data_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

        #code to remove the header
        csv_header = next(csv_reader)

        for row in csv_reader:
            total_votes = total_votes + 1
            candidate_name = row[2]   

            # counting candidate votes with conditional statement 
            if candidate_name in candidate_votes:
                candidate_votes[candidate_name] += 1
            else:
                candidate_votes[candidate_name] = 1

            if candidate_votes[candidate_name] > max_votes:
                max_votes = candidate_votes[candidate_name]
                winner = candidate_name

    # exporting the results to outside the code
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-" * 20 + "\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        f.write(f"{candidate}: {(round(percentage,3))}% ({votes})\n")
    
    f.write("-" * 20 + "\n")
    f.write(f"Winner: {winner}\n")
    f.write("-" * 20 + "\n")

print("")
print("Election Results")
print("")
print("------------------------------")
print("")
print(f"Total Votes: {total_votes}")
print("")
print("------------------------------")
print("")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {(round(percentage,3))}% ({votes})")
print("")
print("------------------------------")
print("")
print(f"Winner: {winner}")
print("")
print("------------------------------")
print("")
print("Your file was created!")


