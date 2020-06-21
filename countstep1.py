# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
county_options = []
county_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_county = ""
winning_count_county = 0
winning_percentage_county = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        county_total_votes += 1
        # Get the candidate name from each row.
        county_name = row[1]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if county_name not in county_options:
            # Add the candidate name to the candidate list.
            county_options.append(county_name)
            # And begin tracking that candidate's voter count.
            county_votes[county_name] = 0
        # Add a vote to that candidate's count
        county_votes[county_name] += 1
        # Save the Results to our text file.
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal.
    county_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(county_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(county_results)
        
    for county in county_votes:
        # Retrieve vote count and percentage.
        votes = county_votes[county]
        county_vote_percentage = float(votes) / float(county_total_votes) * 100
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        county_results = (f"{county}: {county_vote_percentage:.1f}% ({votes:,})\n")

        print(county_results)
        txt_file.write(county_results)
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > county_winning_count) and (county_vote_percentage > county_winning_percentage):
            county_winning_count = votes
            county_winning_candidate = county
            county_winning_percentage = county_vote_percentage
        # Print the winning candidates' results to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Winner: {county_winning}\n"
        f"Winning Vote Count: {county_winning_count:,}\n"
        f"Winning Percentage: {county_winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_county_summary)
    txt_file.write(winning_county_summary)