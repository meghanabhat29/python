from datetime import date

def age(x):
	today=date.today()
	a=today.year - x.year - ((today.month,today.day) < (x.month,x.day))
	return a


dob=input("Enter your date of birth [dd/mm/yyyy] : ")
d=int(dob[0:2])
m=int(dob[3:5])
y=int(dob[6:])
print("You are",age(date(y,m,d)),"years old")
