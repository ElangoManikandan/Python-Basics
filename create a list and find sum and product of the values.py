a=[]
sum=0
product=1
print("Enter the no of elements:")
n=int(input())
for i in range(n):
    print("Enter the value",i+1)
    j=int(input())
    a.append(j)
    sum=sum + j
    product=product*j
    i=i+1
print("Sum of the elements:",sum)
print("Product of the elements:",product)

    

    
               
