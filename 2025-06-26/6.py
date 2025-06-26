import string

sentence = input("Enter sentence : ")

sentence = sentence.lower()
cleaned_sentence = ''.join(char for char in sentence if char not in string.punctuation)
letters_counts = {}
for char in cleaned_sentence:
    if char in letters_counts:
        letters_counts[char] += 1
    else:
        letters_counts[char] = 1

print("char counts:")
for char, count in sorted(letters_counts.items()):
    print(f"{char}: {count}")
