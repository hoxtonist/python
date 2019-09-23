import random
counters = [0] * 50
lucky = [0] * 5
runs = int(input("number of runs? "))
loop = 1
while loop <= runs:
    pos = 0
    while pos <= 4:
        ball = random.randint(1, 50)
        if (ball) not in lucky:
        	lucky[pos] = ball
        	counters[ball - 1] += 1
        	pos += 1
    loop += 1
print(counters)
