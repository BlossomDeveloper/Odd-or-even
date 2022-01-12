# prompt the user to select a number

user = int(input('Think about a number between 1 and 1000 and write it: '))

# check if a number is odd or even

if 1 < user < 1000:
    if user % 2 == 1:
        print("The number you thought is odd.")
    else:
        print("The number you thought is even.")
else:
    print("Please enter a number between 1 and 1000.")

