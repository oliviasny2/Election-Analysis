print("Hello World")
#counties = ["Arapahoe","Denver", "Jefferson"]
#if counties[1] == 'Denver' :
    #print(counties[1])
## The double equal sign means "equal to" and is a boolean operator

# If-else statements: used when we need an outcome for both the true and false conditions. AKA dual-alternate decision statement
## Some rules for If-else statements
### 1. Make sure the if statement and the else statement are aligned
### 2. Make sure the statements under the if and else statements are consistently indented

# 3.2.9 Membership and Logical Operators
## Membership Operators: used to test if an object, like a string, integer, or other data type is present in an expression, list, tuple, or dictionary
### In: returns true if a sequence with the specified value is present in the object
### not in: returns true if a sequence with the specified value is not present in the object

#if "El Paso" in counties:
    #print("El Paso is in the list of counties.")
#else:
    #print("El Paso is not in the list of counties.")

## Logical Operators: allows us to connect multiple comparison expressions to create a compound expression
### and: evaluates two boolean expressions into one compound expression. The compound expressions is true if both boolean expressions are true
### or: evaluates two boolean expressions into one compound expression. The compound expression is true if either boolean expression is true
### not: evalutes a boolean expression. the expression is true if the conditional is false

#if "Arapahoe" in counties and "El Paso" in counties:
    #print("Arapahoe and El Paso are in the list of counties.")
#else:
    #print("Arapahoe or El Paso is not in the list of counties.")

#if "Arapahoe" in counties or "El Paso" in counties:
    #print("Arapahoe or El Paso is in the list of counties")
#else:
    #print("Arapahoe and El Paso are not in the list of counties.")


# Coming back from loops.py

#Iterate through lists and tuples

#for county in counties:
    #print(county)
# this code declares the county variable as each variable in the counties list

# range function can simplify things for us

#numbers = [0,1,2,3,4]
#for num in numbers:
    #print(num)

#for num in range(5):
    #print(num)

#for i in range (len(counties)):
    #print(counties[i])
# You can use any variable, i is just used in this example

# Iterate through a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# Get the keys for the dictionary: two methods

#for county in counties_dict:
    #print(county)

#for county in counties_dict.keys():
    #print(county)

# Get the values for the dictionary: 3 methods

#for voters in counties_dict.values():
    #print(voters)

#for county in counties_dict:
    #print(counties_dict[county])

#for county in counties_dict:
    #print(counties_dict.get(county))

# get the key-value pairs from the dictionary

#for county, voters in counties_dict.items():
    #print(county, voters)

# Iterate through a list of dictionaries

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver","registered_voters": 463353},
                {"county":"Jefferson","registered_voters": 432438}]

#for county_dict in voting_data:
    #print(county_dict)

#Print the counties from the voting_data list
#for i in range(len(voting_data)):
    #print(voting_data[i]["county"])

#Print the counties and number of registered voters
#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)

#Print the number of registered voters in each dictionary
#for voters in voting_data:
    #print(voters["registered_voters"])

# Module 3.2.11

## Print() function: two things that it will print
    # 1. A string, or a sentence displayed between quotes
    # 2. A string with integer values converted to a string using concatenation  with the "+" sign
        # Ex: print("Your interest for the year is $" + str(interest))

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+ "% of the total votes. ")

## F-strings: formatted string literals
    # begins with an f followed by a string contained within quotes
    # In the f-string, curly braces are used to add variables or expressions to the f-string

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes/total_votes * 100}% of the total votes")

# Using F-strings with Dictionaries

## Using concatenation
#for county, voters in counties_dict.items():
    #print(county + " county has " + str(voters) + " registered voters.")

##Using F string
#for county, voters in counties_dict.items():
    #print(f"{county} county has {voters} registered voters")

# Multiline F-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (f"You received {candidate_votes} number of votes. "
                        f"The total number of votes in the election was {total_votes}."
                        f"You received {candidate_votes/total_votes*100}% of the total votes. ")
#print(message_to_candidate)

#Format Floating-Point Decimals
## general format for a float in an f-string is f'{value:{width}.{precision}}'
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidates = (
        #f"You received {candidate_votes:,} number of votes. "
        #f"The total number of votes in the election was {total_votes:,}. "
        #f"You received {candidate_votes / total_votes * 100:.2f} of the total votes. ")

#Move to Printing Formats.py