
# סעיף א׳ - יצירת משתנים

user_name = "Iliya"
age = 21
is_connected = True
test_score = 99.5
print("\nFIRST USER")
print("\nUser:", user_name)
print("Age:", age)
print("Connected:", is_connected)
print("Test Score:", test_score)

# סעיף ב׳ - שינוי ערכים

user_name = "Arthur"
age = 54
is_connected = False
test_score = 95
print("\nSECOND USER")
print("\nUser:", user_name)
print("Age:", age)
print("Connected:", is_connected)
print("Test Score:", test_score)

# סעיף ג׳ - יצירת הזנת נתונים ליוזר

user_name = input("\nEnter your name: ")
age = input("Enter your age: ")
print("Hello", user_name)

# סעיף ד׳ - עוד הזנת נתונים

Tester = input("\nEnter your name: ")
Number_of_Tests = input("Enter the number of tests you've completed today: ")
print("tester", Tester, " has completed", Number_of_Tests, "tests today.")

# סעיף ה׳ - סעיף לבודקי תוכנה

test_passed = False
if test_passed:
    print("\nTest passed successfully!")
else:
    print("\nTest failed. Please check the details and try again.")