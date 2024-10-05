import statistics
import math
import matplotlib.pyplot as plt

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

# Step 4: Sort the dictionary by keys (scores) in descending order
sorted_frequency_dict = dict(sorted(frequency_dict.items(), reverse=True))

# Initialize reverse cumulative frequencies (starting from total)
reverse_cumulative_frequency = total_scores
cumulative_relative_frequency = 1.0

# Step 5: Print the header for the table
print(f"{'Score':<10} {'Frequency':<10} {'Relative Frequency':<20} {'Percentage (%)':<15} {'Cumulative Frequency':<25} {'Cumulative Rel. Frequency'}")

# Step 6: Display the sorted frequency distribution with all desired values
for score, frequency in sorted_frequency_dict.items():
    # Relative frequency as a decimal
    relative_frequency = frequency / total_scores
    
    # Percentage as an integer
    percentage = relative_frequency * 100
    
    # Print the results for each score with the updated formatting
    print(f"{score:<10} {frequency:<10} {relative_frequency:<20.2f} {percentage:<15.0f} {reverse_cumulative_frequency:<25} {cumulative_relative_frequency:.2f}")
    
    # Decrease reverse cumulative frequency by the current frequency
    reverse_cumulative_frequency -= frequency
    
    # Update cumulative relative frequency
    cumulative_relative_frequency = reverse_cumulative_frequency / total_scores

# Step 7: Calculate Mode, Median, and Mean
# Mode: Most frequent score(s)
try:
    mode = statistics.multimode(scores)  # Use multimode to handle cases with more than one mode
except statistics.StatisticsError:
    mode = "No mode"

# Median: Middle score or average of two middle scores
median = statistics.median(scores)  # Automatically handles odd/even counts and duplications

# Mean: Average of the scores
mean = statistics.mean(scores)

# Step 8: Calculate Sum of Squares, Variance, and Standard Deviation
# Sum of Squares (SS): sum of (score - mean)^2
sum_of_squares = sum((x - mean) ** 2 for x in scores)

# Variance: sum_of_squares / (n - 1) for sample variance (unbiased estimate)
variance = statistics.variance(scores)

# Standard Deviation: Square root of the variance
standard_deviation = math.sqrt(variance)

# Step 9: Print Mode, Median, Mean, Sum of Squares, Variance, and Standard Deviation
print("\nStatistics:")
print(f"Mode: {', '.join(map(str, mode)) if mode else 'No mode'}")
print(f"Median: {median}")
print(f"Mean: {mean:.2f}")
print(f"Sum of Squares: {sum_of_squares:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Standard Deviation: {standard_deviation:.2f}")

# Step 10: Function to draw frequency histogram
def plot_histogram(scores, frequency_dict):
    # Prepare the data for plotting
    scores_list = list(frequency_dict.keys())
    frequencies = list(frequency_dict.values())
    
    # Plot histogram
    plt.bar(scores_list, frequencies, color='skyblue', edgecolor='black')
    plt.xlabel('Scores')
    plt.ylabel('Frequency')
    plt.title('Frequency Histogram of Scores')
    
    # Show the histogram
    plt.show()

# Call the function to plot the histogram
plot_histogram(scores, frequency_dict)
