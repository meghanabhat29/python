#Menu driven program to convert degree F to degree C or vise versa and save it as list of tuples

temps = []

def CtoF():
	temp = input("Enter the temperature ")
	f = (temp*9/5) + 32
	temps.append((temp+"C :"+f+"F"))
	print(temp,"degree C = ",f,"degree F")
	

def FtoC():
	temp = input("Enter the temperature ")
	c = (temp - 32) * 5/9
	temps.append((temp+"F : "+c+"C"))
	print(temp,"degree C = ",f,"degree F")
	




while True:
	option = input("Enter C to enter temperature in Celsius or F to enter temp in Farenheit or 0 to quit: ")
	#compute(option)
	if option == "C":
		CtoF()
	if option == "F":
		FtoC()
	if option == "0":
		exit()
	else:
		print("Invalid input")
	
