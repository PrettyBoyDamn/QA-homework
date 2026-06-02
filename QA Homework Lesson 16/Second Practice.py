string = input("enter a word: ")

First = string[0]
Middle = len(string) // 2
Last = string[-1]

print("First letter: ", First)
print("Middle letter: ", string[Middle])
print("Last letter: ", Last)

string2 = input("enter a sentence: ")

New_string = string2[3:]
replace_string = string2.replace(" ", "-")
print("New string: ", New_string)
print("Length of string: ", len(string2))
print("String with spaces replaced: ", replace_string)