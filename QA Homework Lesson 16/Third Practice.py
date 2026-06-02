number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

string = input("Enter a word: ")
if string and string[0] == "A":
    string = "a" + string[1:]
    print("Modified string: ", string)

mail = input("Enter your email: ")
if len(mail) < 4 or mail[0] == "@" or mail[-1] == "@":
    print("Invalid email address.")
else:
    print("Valid email address.")