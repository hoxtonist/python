import random

counters = []
for i in range(50):
    counters.append(0)
lucky = []
for i in range(6):
    lucky.append(0)
runs = int(input("number of runs? "))
loop = 1
while loop <= runs:
    pos = 0
    while pos <= 4:
        ball = random.randint(1, 50)
        if (ball) not in lucky:
            lucky[pos] = ball
            pos += 1
            counters[ball - 1] += 1
    loop += 1
print(counters)
highest = []
for i in range(5):
    highest.append(0)
for lucky2 in range(50):
    if counters[lucky2] > highest[0]:
        for shift in range(4):
            highest[shift] = highest[shift + 1]
        highest[4] = lucky2
    print(highest)

