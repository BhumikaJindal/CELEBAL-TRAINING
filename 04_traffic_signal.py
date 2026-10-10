t = int(input())

t = (t - 1) % 90 + 1

if t <= 30:
    print("RED")
elif t <= 45:
    print("YELLOW")
else:
    print("GREEN")