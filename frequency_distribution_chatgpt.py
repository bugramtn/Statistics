# Step 1: Take scores from the user and store them in a list
scores = input("Enter the scores separated by spaces: ").split()
scores = [int(score) for score in scores]

# Step 2: Create a dictionary to store frequencies
frequency_dict = {}
for score in scores:
    if score in frequency_dict:
        frequency_dict[score] += 1
    else:
        frequency_dict[score] = 1

# Step 3: Calculate total number of scores for relative frequency calculation
total_scores = len(scores)

# Step 4: Sort the dictionary by keys (scores) in ascending order
sorted_frequency_dict = dict(sorted(frequency_dict.items()))

# Initialize cumulative frequencies
cumulative_frequency = 0
cumulative_relative_frequency = 0.0

# Step 5: Print the header for the table
print(f"{'Score':<10} {'Frequency':<10} {'Relative Frequency':<20} {'Percentage (%)':<15} {'Cumulative Frequency':<25} {'Cumulative Rel. Frequency'}")

# Step 6: Display the sorted frequency distribution with all desired values
for score, frequency in sorted_frequency_dict.items():
    # Relative frequency as a decimal
    relative_frequency = frequency / total_scores
    
    # Percentage as an integer
    percentage = relative_frequency * 100
    
    # Cumulative frequency
    cumulative_frequency += frequency
    
    # Cumulative relative frequency as a decimal
    cumulative_relative_frequency = cumulative_frequency / total_scores
    
    # Print the results for each score with the updated formatting
    print(f"{score:<10} {frequency:<10} {relative_frequency:<20.2f} {percentage:<15.0f} {cumulative_frequency:<25} {cumulative_relative_frequency:.2f}")
