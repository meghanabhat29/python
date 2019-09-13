#Program to read a list of numbers
#One line comprehension to a create a new list
#Create another list reversing the elements

S=[x**2 for x in range(10)]
M=[x for x in S if x%2==0]
M.reverse()
