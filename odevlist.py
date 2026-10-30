#Sum of Odd and Even Elements in an Array
size=int(input())
arr=list(map(int,input().split()))
oddsum=evensum=0
for x in arr:
  if x%2==0:
    evensum=evensum+x 
  else:
    oddsum=oddsum+x 
print(evensum,oddsum)
