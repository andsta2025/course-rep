import os
text = os.getenv("TEXT", "Hello, Docker!")
person = os.getenv("PERSON", "Unknown")
print(f"{text} - greetings from {person}")