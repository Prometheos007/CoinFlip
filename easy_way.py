T = 2 #No. of times
G = 3 #No. of Games
I = 1 #Heads or Tails initial
N = 5 #No. of coins (& rounds)
Q = 1 #Which One is needed

while __name__ == '__main__':
	inState = [I]*N
	outState = []

	if G%2 == 0:
		outState = inState
	else:
		for i in range(N):

			if i%2 == 0:
				outState += str(inState[i])
			elif inState[i] == 1:
				outState += '0'
			else:
				outState += '1'
	print(outState)
	break
