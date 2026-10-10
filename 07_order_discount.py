amount = float(input())

if amount >= 5000:
    payable = amount * 0.80
elif amount >= 3000:
    payable = amount * 0.90
elif amount >= 1000:
    payable = amount * 0.95
else:
    payable = amount

print(int(payable) if payable.is_integer() else payable)