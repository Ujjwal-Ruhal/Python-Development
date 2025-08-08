# Task 4: Calculator Program

# Define supported operators
operator_add, operator_sub, operator_mul, operator_div, operator_mod = "+", "-", "*", "/", "%"

print('\n*******************************************\n')

# Take user input for numbers
number_1 = int(input("Please enter first number : "))
number_2 = int(input("Please enter second number : "))

print('\n*******************************************\n')

# Take operator input from user
operator = input("Please select the operator ( + , - , * , / , % ) : ")

# Perform operation based on user choice
if operator == operator_add:
    print(f"The sum of {number_1} and {number_2} is : {number_1 + number_2}")

elif operator == operator_sub:
    print(f"The subtraction of {number_1} and {number_2} is : {number_1 - number_2}")

elif operator == operator_mul:
    print(f"The multiplication of {number_1} and {number_2} is : {number_1 * number_2}")

elif operator == operator_div:
    if number_2 != 0:
        print(f"The division of {number_1} and {number_2} is : {number_1 / number_2}")
    else:
        print("Error: Division by zero is not allowed.")

elif operator == operator_mod:
    if number_2 != 0:
        print(f"The modulus of {number_1} and {number_2} is : {number_1 % number_2}")
    else:
        print("Error: Modulus by zero is not allowed.")

else:
    print('Invalid operator. Please try again. Thank you.')
