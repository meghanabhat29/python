students={ '1MS17IS147':'Meghana','1MS17IS152':'Pavana','1MS17IS156':'Jayashree'}
list=['value1','value2','value3','value4']
list2=[]
j=0

#The output has the elements in a different order due to hashing that happens within, the hash values in the hash tables are different
for i in students:
	print("Key is ",i, "Value is ",students[i])
	list[j]=students[i]
	j=j+1

print(list)
print(students.keys())
print(students.values())
print(students.items())
