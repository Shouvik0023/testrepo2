def findsum(n):
 sum=0
 for num in range(1,n+1):
         sum=sum+num
         
         return sum

t=int(input("enter a number-"))

sums=findsum(t)
print(sums)
