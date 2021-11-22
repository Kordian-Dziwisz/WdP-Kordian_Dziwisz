M = [[1, 1, 1, 1, 1, 1, 1], [1, 2, 1, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 3, 1], [1, 1, 1, 1, 1, 1, 1]]
stepsToDeath = 20

def rysujLabirynt(macierz, puste=0, sciana=1, ludzik=2, drzwi=3):
	labirynthElements = [puste, sciana, ludzik, drzwi]
	for i in range(len(macierz)):
		line=''
		for j in range(len(macierz[i])):
			line+=labirynthElements[macierz[i][j]]
		print(line)



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

def aktualizujLabirynt(M, ruch):
	pPos = getPlayerPosition(M)
	gPos = getGoalPosition(M)
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
			M[pPos[0]][pPos[1] + 1] = 2

	if not getGoalPosition(M):
		return False


	rysujLabirynt(M, ' ', 'X', '0', 'G')
	return True


won = False
while (not won and stepsToDeath>0):
	rysujLabirynt(M, ' ', 'X', '0', 'G')

	playerInput = input()
	if (not aktualizujLabirynt(M, playerInput)):
		won = True
	else:
		stepsToDeath-=1

if (stepsToDeath == 0):
	print('You\'re dead, ain\'t that a surprise?')
else:
	print('You won!')
