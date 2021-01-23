#Functions



#making a function to invert the given string of bits till na specific number of elements
def changeState(b_array,num=1):

	#using a dictionary to store bit inverse 
	bitDict = {'0':'1', '1':'0'}

	#looping through the bit array 
	for element_index in range(num):
		#assigning temp var to the bit we want to change
		bit = b_array[element_index] 

		#using dictionary to inverse the bit 
		b_array[element_index] = bitDict[str(bit)]

	return b_array

#making a function which changes the state every round from 1 to N
def playRound(b_array):
	#loop for number of rounds (equal to no. of elements)
	
	for i in range(len(b_array)):
		#change state till that element
		b_array = changeState(b_array,i+1)

	return b_array 


