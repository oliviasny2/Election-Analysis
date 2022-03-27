# The data we need to retrieve
##direct file path method
###file_to_load = 'Resources\election_results.csv'
# Open the election results and read the file
###with open(file_to_load) as election_data:
    ###print(election_data)
# r mode, doesn't say what that is so IDK what to say about that
# must open and close the file to ensure data is properly updated, OR just use "with" instead (see above)
##indirect file path method
import csv
import os
file_to_load = os.path.join("Resources","election_results.csv")
#with open(file_to_load) as election_data:
    #print(election_data)

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")
#outfile = open(file_to_save, "w")
## Use "with" instead
#with open(file_to_load) as election_data:
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
    #or just put on one line 
    #txt_file.write("Arapahoe\nDenver\nJefferson")
    #file_reader = csv.reader(election_data)
#outfile.close()
    #for row in file_reader:
        #print(row)
    ## Going to initilize a variable, AKA accumulator
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
    ## Open  the election results and read the file
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    header = next(file_reader)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end = "")
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = (float(votes) / float(total_votes)) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes>winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------\n")
    txt_file.write(winning_candidate_summary)
    #print (winning_candidate_summary)

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
