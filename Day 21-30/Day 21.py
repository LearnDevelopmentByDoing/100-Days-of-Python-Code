import re

email = input("Enter an email address: ")

if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
    print("Valid email address")
else:
    print("Invalid email address")
