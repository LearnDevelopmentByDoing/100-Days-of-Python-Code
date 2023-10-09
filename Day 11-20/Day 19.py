num = int(input("Enter a number: "))

if num >= 0 and int(num ** 0.5) ** 2 == num:
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
