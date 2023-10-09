import random

n = random.randint(0, 100)
tries = 10

for _ in range(tries):
    guess = int(input("Enter your guess: "))
    if guess == n:
        print(f"Congratulations! You guessed the number {n} in {tries - _} attempts.")
        break
    elif guess < n:
        print("Too low.")
    else:
        print("Too high.")
    print(f"You have {tries - _ - 1} attempts left.")
    if guess != n:
        print(f"Sorry, you ran out of attempts. The correct number was {n}.")
