number = int(input("enter a number: "))
if number > 0 and number % 2 == 0:
    print("The number is positive and even.")
elif number > 0 and number % 2 != 0:
    print("The number is positive and odd.")
elif number < 0 and number % 2 == 0:
    print("The number is negative and even.")
elif number < 0 and number % 2 != 0:
    print("The number is negative and odd.")
else:
    print("The number is zero.")