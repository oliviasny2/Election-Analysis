candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (f"You received {candidate_votes:,} number of votes. "
                        f"The total number of votes in the election was {total_votes:,}."
                        f"You received {candidate_votes/total_votes*100:.2f}% of the total votes. ")
print(message_to_candidate)

## If you use double quotation marks for the f-strings containing the keys, then be sure to use single quotation marks for the keys and values for the dictionary
