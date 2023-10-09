vowels = ["e", "o", "a", "u", "i"]
word = str(input("Enter a word: "))
count = 0

for vowel in word:
    if vowel in vowels:
        count = count + 1

print(count)
