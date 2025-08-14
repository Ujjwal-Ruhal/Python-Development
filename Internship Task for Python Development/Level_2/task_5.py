# Task-5: File Manipulation
import string

def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()  # Read file & convert to lowercase
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    # Remove punctuation for cleaner word counting
    for char in string.punctuation:
        text = text.replace(char, "")

    # Split into words
    words = text.split()

    # Count occurrences using a dictionary
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Sort alphabetically and display results
    for word in sorted(word_count):
        print(f"{word}: {word_count[word]}")


# Example usage
filename = input("Enter the file name: ")
count_words_in_file(filename)


# like that...