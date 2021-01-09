print("Enter a letter")
n: str = input()
letters = ['a','e','i','o','u']
if n in letters:
    print("It is a vowel")
elif len(n) >= 2:
    print("Please give a single letter")
else:
    print("It is a Consonant")
