data = [
{"hostname": "10.16.08.09", "Candidate": "Rajat", "password": "asdadwf"},
{"hostname": "", "Candidate": "Rajat1", "password": ""},
{"hostname": "", "Candidate": "Rajat1", "password": ""},
{"hostname": "", "Candidate": "Rajat1", "password": ""},
# Add more dictionaries to the list as needed
]
from collections import Counter
# Extract candidate names from the "Candidate" key in each dictionary
candidates = [item["Candidate"] for item in data if "Candidate" in item]
# Use Counter to count occurrences of each candidate
print(candidates,"sss")
candidate_counts = Counter(candidates)
print(candidate_counts,"candidate_counts")
# Find the most frequent candidates
most_frequent_candidate = candidate_counts.most_common(1)
print(most_frequent_candidate)
# Print the result
print("Most frequent candidate:", most_frequent_candidate[0][0] if
most_frequent_candidate else "No candidates found")