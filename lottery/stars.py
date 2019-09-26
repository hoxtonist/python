import random
counters = [0] * 12
lucky = [0] * 2
runs = int(input("number of runs? "))
for loop in range(runs):
	for pos in range(2):
		ball = random.randint(1, 12)
		if (ball) not in lucky:
			lucky[pos] = ball
			counters[ball - 1] += 1
print(counters)
counters2 = counters
highest = []
while len(highest) <= 1:
	most=max(counters2)
	for i in range(12):
		if (counters2[i] == most) and (len(highest) <= 1):
			highest.append(i + 1)
			counters2[i] *= -1
print(sorted(highest))