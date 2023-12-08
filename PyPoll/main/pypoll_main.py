import os
import csv

election_data_csv = os.path.join("..", "Resources", "election_data.csv")
output_file = os.path.join("..", "analysis", "election_results.txt")

with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("------------------------------\n")

    # declaring variables
    total_votes = 0
    candidate_votes = {}   
    winner = []   
    max_votes = 0   

    # opening and reading csv
    with open(election_data_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

        #code to removing the header
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
    file.write(f"Total Votes: {total_votes}\n")
    file.write("------------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {(round(percentage,3))}% ({votes})\n")
    
    file.write("------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("------------------------------\n")

# printing the resultls in current code
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
print("Your file was successfully created!")
print("")


        
