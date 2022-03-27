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
with open(file_to_load) as election_data:
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
    #or just put on one line 
    #txt_file.write("Arapahoe\nDenver\nJefferson")
    file_reader = csv.reader(election_data)
#outfile.close()
    #for row in file_reader:
        #print(row)
    header = next(file_reader)
    print(header)
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
