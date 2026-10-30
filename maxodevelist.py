#Find Maximum Odd and Even Elements in an Array
import sys
size=int(input())
array=list(map(int,input().split()))
oddmax=evenmax=-sys.maxsize-1
for x in array:
  if x%2==0:
    if x>evenmax:
      evenmax=x 
  else:
     if x>oddmax:
      oddmax=x 
      
if evenmax==-sys.maxsize-1:
  print("None")
else:
  print(evenmax)
if oddmax==-sys.maxsize-1:
  print("None")
else:
  print(oddmax)
