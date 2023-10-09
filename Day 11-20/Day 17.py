import string

sentence = input("Enter a sentence: ").lower()
alphabet = set(string.ascii_lowercase)

if set(sentence).intersection(alphabet) == alphabet:
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
