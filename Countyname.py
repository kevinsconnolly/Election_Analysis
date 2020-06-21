# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0

#county options, county votes
county_options = []
county_votes = {}

# Track the winning County, vote count, and percentage.
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the County name from each row.
        county_name = row[1]
        # If the county does not match any existing county add it the
        # the county list.
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)
            # And begin tracking that county's voter count.
            county_votes[county_name] = 0
        # Add a vote to that county's count
        county_votes[county_name] += 1
        # Save the Results to our text file.
with open(file_to_save, "w") as txt_file:

           
    for county in county_votes:
        # Retrieve vote count and percentage.
        votes = county_votes[county]
        county_vote_percentage = float(county_votes) / float(total_votes) * 100
        # Print each county, their voter count, and percentage to the
        # terminal.
        county_results = (f"{county}: {county_vote_percentage:.1f}% ({votes:,})\n")

        print(county_results)
        txt_file.write(county_results)
        # Determine winning vote count, winning percentage, and county.
        if (county_votes > winning_county) and (county_vote_percentage > winning_percentage):
            winning_county_count = votes
            winning_county = county
            winning_percentage = county_vote_percentage
        # Print the winning county' results to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Winner: {winning_county}\n"
        f"Winning Vote Count: {winning_county_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_county_summary)
    txt_file.write(winning_county_summary)



# Candidate options, candidate votes
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        # Save the Results to our text file.
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
        
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
        # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)