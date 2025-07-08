import numpy as np
from scipy import stats

def analyze_csv_data(filename):
    try:
        # Load data from CSV file
        data = np.loadtxt(filename, delimiter=',')
        # Calculate basic statistics
        mean = np.mean(data)
        median = np.median(data)
        mode = stats.mode(data)[0][0]
        std_dev = np.std(data)  # Standard deviation
        variance = np.var(data)  # Variance
        max_value = np.max(data)  # Maximum value
        min_value = np.min(data)  # Minimum value
        # Print the results
        print(f"Data Analysis for {filename}:")
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Mode: {mode}")
        print(f"Standard Deviation: {std_dev}")
        print(f"Variance: {variance}")
        print(f"Maximum Value: {max_value}")
        print(f"Minimum Value: {min_value}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    filename = 'numbers.csv' 
    analyze_csv_data(filename)