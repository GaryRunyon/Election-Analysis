#Add dependencies
import csv
import os
#Assign a variable for the file to load and the path 
file_to_load = 'Resources/election_results.csv'
# Create a filename variable to a direct path to the file
file_to_save = 'analysis/election_analysis.txt'

# Initialize a totale vote counter.
total_votes = 0

#Candidate options
candidate_options = []

# County options
county_options = []

# Make an empty dictionary for candidate votes
candidate_votes = {}

# Make an empty dictionary for county votes 
county_votes = {}

# Winning candidate and winning count variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file. 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        # Add the total vote count
        total_votes +=1

        #Print the candidate name from each row 
        candidate_name = row[2]

        # If the candidate name does not match any current candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Track the candidate's vote count 
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count 
        candidate_votes[candidate_name] += 1

with open (file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes:  {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #Save the final count to text file
    txt_file.write(election_results)
        # Determine the percentage of votes for each candidate by looping through the counts
        # Iterate through the candidate list

    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Caulculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print each candidate's name, vote count and percentage 


        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")


        print(candidate_results)

        txt_file.write(candidate_results)


        if (votes > winning_count) and (vote_percentage > winning_percentage):


            winning_count = votes
            winning_percentage = vote_percentage
            #Set the winning candidate equal to the candidate's name
            winning_candidate = candidate
            #Print the candidate name and percentage of votes
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        
        txt_file.write(winning_candidate_summary)




Challenge 

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# County Options
county_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the county name from each row.
        county_name = row[1]

        if county_name not in county_options:
            #add it to the list of counties.
            county_options.append(county_name)
            #and begin tracking that county's voter count
            county_votes[county_name]=0
        #add a vote to that county's count.
        county_votes[county_name] += 1

print(county_votes)

### {'Jefferson': 38855, 'Denver': 306055, 'Arapahoe': 24801}

















































