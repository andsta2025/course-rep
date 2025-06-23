from collections import Counter
import string

# Read data from a file
filename = "file.txt"  # Replace with your file path

try:
    with open(filename, 'r') as file:
        text = file.read()

    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()

    # Split text into words
    words = text.split()

    # Count word frequencies using Counter
    word_counts = Counter(words)

    # Print the 10 most common words
    print("Top 10 most common words:")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")

except FileNotFoundError:
    print(f"File '{filename}' not found.")