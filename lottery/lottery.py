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

# comment

counters2 = counters
highest = []
while len(highest) <= 4:
	most=max(counters2)
	for i in range(50):
		if (counters2[i] == most) and (len(highest) <= 4):
			highest.append(i + 1)
			counters2[i] *= -1
print(sorted(highest))