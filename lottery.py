import random
counters = [0] * 50
lucky = [0] * 5
runs = int(input("number of runs? "))
for loop in range(runs):
    for pos in range(5):
    	ball = random.randint(1, 50)
    	if (ball) not in lucky:
        	lucky[pos] = ball
        	counters[ball - 1] += 1
print(counters)
