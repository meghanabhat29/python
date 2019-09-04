
#task 1
mylist=["Music","Dance","Literature",21,"Art","Academics"]
print("The list is :",mylist)
print("The length of the list is:",len(mylist))

Literature=["Books",123456,"Authors"]

print(mylist[2:])
mylist[1]="Apple"
print("The second element in the list has been replaced by the name of a fruit.")
list1=[21,"Abc"]
list2=mylist+list1
print("The concatenated list : ",list2)

list3=list.copy(mylist)
print("The copy of the first list :",list3)

list4=Literature[0:]
print("The copy of the list-literature",list4)


#task 2
mytuple=(21,29.10,3,15,6,26,31,8)
print(mytuple[0])

#task3
mylist=list(mytuple)
print(mylist)


