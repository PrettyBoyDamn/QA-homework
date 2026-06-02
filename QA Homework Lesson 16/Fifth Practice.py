age = int(input("Enter your age: "))
if age < 0:
    correct_age = 0
    print ("Congratulations! You were just born!")
if age > 120:
    correct_age = 120
    print("Congratulations! You are the oldest person alive! But you cannot be older than 120 years old.")
elif age > 0 and age <= 18:
    print("You are a teenager.")
elif age > 18 and age <= 120:
    print("You are an adult.")

password = input("Enter your password: ")
if len(password) > 8 and password[0] == "Z" and password[-1] == "$":
    print("STRONG PASSWORD.")
elif len(password) > 8 and password[0] == "C" and password[-1] == "$":
    print("STRONG PASSWORD.")
else:
    print("Your password is invalid. It must be longer than 8 characters, start with 'Z' or 'C', and end with '$'.")
