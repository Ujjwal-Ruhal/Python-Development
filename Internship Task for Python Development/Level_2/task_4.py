# Task-4: Fibonacci Sequence

def fibonacci(n):
    # Handle small cases
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]  # Starting values
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

# Get user input
terms = int(input("Enter how many terms of Fibonacci you want: "))

print(f"Fibonacci sequence ({terms} terms): {fibonacci(terms)}")
