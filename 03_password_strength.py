password = input()

digit = False
uppercase = False

for char in password:
    if char.isdigit():
        digit = True
    if char.isupper():
        uppercase = True

if len(password) >= 8 and digit and uppercase:
    print("STRONG")
else:
    print("WEAK")