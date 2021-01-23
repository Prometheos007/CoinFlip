from Defs import *


#Coin flip


T = 1 #No. of times
G = 2 #No. of Games
I = 1 #Heads or Tails initial
N = 7 #No. of coins (& rounds)
Q = 1 #Which One is needed

 

while __name__ == "__main__":
	
	#No. of test cases
	for i in range(T):
		#take all the input here 
		
		#Starting : all same (0/1)
		coinstate = [I]*N

		#no. of games
		for j in range(G):
			coinstate = playRound(coinstate)
		print(coinstate)
	
	break


