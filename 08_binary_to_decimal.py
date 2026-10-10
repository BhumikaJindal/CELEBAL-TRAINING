binary = input()

decimal = 0
power = 1

for digit in binary[::-1]:
    decimal = decimal + int(digit) * power
    power = power * 2

print(decimal)