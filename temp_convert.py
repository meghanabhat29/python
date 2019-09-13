ch=0
list1=[]
while isdigit(ch):
	ch=input("Press 1 : Celsius to Fahrenheit and 2:Fahrenheit to Celsius,press E to exit :")
	if ch==1:
		c=int(input("\nEnter the temperature in celsius : ")
		list1.append(c)
		print("\n"+c+" degree Celsius = "+f+" degree Fahrenheit")
		list1.append("-->")
		list1.append(ctof(c))
		
	elif(ch==2):
		f=int(input("\nEnter the temperature in Fahrenheit : ")
		list1.append(f)
		print("\n"+f+" degree Fahrenheit = "+c+" degree Celsius")
		list1.append("-->")
		list1.append(ftoc(f))
	else:
		print("Invalid choice,try again\n")
def ctof(c):
	f=(c*(9/5))+32
	return f
def ftoc(f):
	c=(f-32)*5/9
	return c
