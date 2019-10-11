print("Enter the range")
x1=int(input("Integer 1: "))
x2=int(input("Integer 2: "))
def Odd(x1,x2):
	newlist=[]
	for i in range(x1,x2):
		if i%2!=0:
			newlist.append(i)
	print(newlist)
	return newlist
Odd(x1,x2)
	 

