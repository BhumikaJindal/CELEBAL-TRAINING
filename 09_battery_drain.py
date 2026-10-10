drain = float(input())

battery = 100
minutes = 0

while battery > 0:
    battery = battery - drain
    minutes += 1

print(minutes)