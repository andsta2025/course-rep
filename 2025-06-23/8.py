from collections import Counter
import string
filename = input("Enter file name (with extention): ")
try:
    with open(filename, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print(f"File '{filename}' not found.")
    exit(1)
text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))
words = text.split()
most_common = Counter(words).most_common(10)
print("Most common words:")
for word, count in most_common:
    print(f"{word}: {count}")
print(f"Total words: {len(words)}")
print(f"Total unique words: {len(set(words))}")
print(f"Total characters (excluding spaces): {len(text.replace(' ', ''))}")
print(f"Total lines: {text.count('\\n') + 1}")
print(f"Total characters (including spaces): {len(text)}")

