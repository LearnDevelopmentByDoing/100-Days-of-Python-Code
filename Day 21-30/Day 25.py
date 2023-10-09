import re

text = input("Enter a text: ")
text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())

if text == text[::-1]:
    print("It's a valid palindrome.")
else:
    print("It's not a valid palindrome.")
