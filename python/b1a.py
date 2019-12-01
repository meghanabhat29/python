list1= []
n=int(input("Enter the number of elements : "))
for i in range(0,n):
	x=int(input("Enter the element : "))
	list1.append(x)
list2=[]
def remove(list1):
	for i in list1:
		if i not in list2:
			list2.append(i)
	return list2

remove(list1)	
print("Original list : ",list1)
print("The list with duplicates removed : ",list2)

