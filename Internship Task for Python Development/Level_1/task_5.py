# Task 5: Palindrome Checker

"""
Check if the given string is a palindrome.
This function ignores case and spaces.
"""
def is_palindrome(text):
    # Step 1: Normalize text (lowercase + remove spaces)
    cleaned_text = text.lower().replace(" ", "")

    # Step 2: Compare string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example's:
word1 = "madam"
word2 = "racecar"
word3 = "hello"

print(f"\nThe word '{word1}' is a palindrome → {'Yes' if is_palindrome(word1) else 'No'}")
print(f"The word '{word2}' is a palindrome → {'Yes' if is_palindrome(word2) else 'No'}")
print(f"The word '{word3}' is a palindrome → {'Yes' if is_palindrome(word3) else 'No'}")

# User input
user_word = input("\nEnter a word to check: ")
print(f"'{user_word}' is a palindrome → {'Yes' if is_palindrome(user_word) else 'No'}")

# that's it, thank you