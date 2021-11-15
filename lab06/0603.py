import math
userNum = int(input())
nums = []
i = 1
while (i < userNum):
	nums.append(i)
	i += 1
i = 2
while i < userNum:
	j = 2*i
	while j < userNum:
		try:
			nums.remove(j)
		except:
			False
		j += i
	i+=1

print(nums)