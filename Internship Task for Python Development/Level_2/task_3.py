# Task-3: Password Strength Checker

import string

def check_password_strength(password):
    """
    Evaluates the strength of a password based on:
    - Length (>= 8 characters)
    - Uppercase letters
    - Lowercase letters
    - Digits
    - Special characters
    """
    # Criteria checks
    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    # Count how many criteria are met
    criteria_met = sum([length_ok, has_upper, has_lower, has_digit, has_special])

    # Strength classification
    if criteria_met == 5:
        return "Strong password ✅"
    elif 3 <= criteria_met < 5:
        return "Moderate password ⚠️"
    else:
        return "Weak password ❌"


# Example usage
user_password = input("Enter a password to check its strength: ")
print(check_password_strength(user_password))
