print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.\n")

while True:
    try:
        number1 = input('\nEnter the first number.')
        if number1 == 'q':
            break
        
        num1 = int(number1)

        number2 = input('Enter the second number.')
        if number2 == 'q':
            break
        
        num2 = int(number2)

    except ValueError:
        print('You have entered text instead of a number. please check your input.')

    else:
        answer = int(number1) + int(number2)
        print(f'The sum of {number1} and {number2} is {answer}.')