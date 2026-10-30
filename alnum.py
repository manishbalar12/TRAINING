s=input()
numcount=alphacount=False
for i in s:
  if i.isalpha():
    alphacount=True
  elif i.isdigit():
    numcount=True
  if alphacount and numcount:
    break
if alphacount and numcount:
  print("true")
else:
  print("false")
  
