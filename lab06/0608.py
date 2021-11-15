M = [[1, 1, 1, 1, 1, 1, 1], [1, 2, 1, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 3, 1], [1, 1, 1, 1, 1, 1, 1]]
stepsToDeath = 20

def printM(M):
	for i in range(len(M)):
		print(M[i])

def getPlayerPosition(M):
	for i in range(len(M)):
		for j in range(len(M)):
			if (M[i][j] == 2):
				return [i, j]
	return False

def getGoalPosition(M):
	for i in range(len(M)):
		for j in range(len(M)):
			if (M[i][j] == 3):
				return [i, j]
	return False

print(getGoalPosition(M))
print(getPlayerPosition(M))

won = False
while (not won and stepsToDeath>0):
	printM(M)
	pPos = getPlayerPosition(M)
	gPos = getGoalPosition(M)

	playerInput = input()
	if playerInput == ',':
		if(pPos[0]>1 and M[pPos[0]-1][pPos[1]] != 1):
			M[pPos[0]][pPos[1]]=0
			M[pPos[0]-1][pPos[1]]=2
	elif playerInput =='o':
		if(pPos[0]<6 and M[pPos[0]+1][pPos[1]] != 1):
			M[pPos[0]][pPos[1]]=0
			M[pPos[0]+1][pPos[1]]=2
	elif playerInput == 'a':
		if(pPos[1]>1 and M[pPos[0]][pPos[1]-1] != 1):
			M[pPos[0]][pPos[1]]=0
			M[pPos[0]][pPos[1]-1]=2
	elif playerInput == 'e':
		if(pPos[1]<6 and M[pPos[0]][pPos[1]+1] != 1):
			M[pPos[0]][pPos[1]]=0
			M[pPos[0]][pPos[1]+1]=2

	if not getGoalPosition(M):
		won = True
	stepsToDeath-=1

if (stepsToDeath == 0):
	print('You\'re dead, ain\'t that a surprise?')
else:
	print('You won!')
