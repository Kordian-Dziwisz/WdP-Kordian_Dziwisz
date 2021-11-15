userInput = input()
end = 0
output = 0
while (end<len(userInput)):
	output+=int(userInput[end])
	end+=1

print(output)