def HourMinute(num):
	hour=0
	x=num
	while int(x)>=60:
		x=int(x)-60
		hour=hour+1
	print(hour)
	
	minutes=x
	return minutes
time=input("Enter the time consumed in minutes : ")
x=HourMinute(time)
print(x)

