print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.\n")

while True:

    number1 = input('Enter the first number.\n')
    if number1 == 'q':
        break

    number2 = input('Enter the second number.\n')
    if number2 == 'q':
        break

    try:
        answer = int(number1) + int(number2)
    except ValueError:
        print('You have entered text instead of a number. please check your input.')
        break
    else:
        print(f'The sum of {number1} and {number2} is {answer}.')
        break