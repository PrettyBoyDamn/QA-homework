def double_number(number):
    return number * 2


def double_word_length(word):
    return len(word) * 2


number = int(input("Enter a number: "))
print("Doubled number:", double_number(number))

word = input("Enter a word: ")
print("Doubled length:", double_word_length(word))

def last_letter_appears_before(word):
    return word[-1] in word[:-1]


word = input("Enter a word: ")

if last_letter_appears_before(word):
    print("TRUE")
else:
    print("FALSE")