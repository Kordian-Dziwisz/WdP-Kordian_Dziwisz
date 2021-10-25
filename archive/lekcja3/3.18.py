import math
numOfPithagoreanTriples=0
for i in range(1, 50):
	for j in range(i, 50):
		if(i!=j and math.sqrt(i*i+j*j)%1==0 and math.sqrt(i*i+j*j)<50):
			print(i, j, int(math.sqrt(i * i + j * j)))
			numOfPithagoreanTriples += 1
print(numOfPithagoreanTriples)