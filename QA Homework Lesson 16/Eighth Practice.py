numbers = []

for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

negative_numbers = []

for n in numbers:
    if n < 0:
        negative_numbers.append(n)

print("Negative numbers:", negative_numbers)

words = ["cat", "dog", "bird", "fish"]
words[0], words[-1] = words[-1], words[0]
print("Swapped words:", words)

grades = [85, 92, 78, 60, 88]

passing_count = 0

for grade in grades:
    if grade >= 70:
        passing_count += 1

print("amount of students with passing grade:", passing_count)