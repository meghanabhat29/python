list1=list(map(int,input("Enter the numbers : ").split()))
n=len(list1)
def maximum(list1,n):
    if n==0:
        return list1[0]
    else:
        return max(list1[n-1],maximum(list1,n-1))
print("The maximum number is ",maximum(list1,n))  
