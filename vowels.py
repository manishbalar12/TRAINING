s=input()
vow="aeiouAEIOU"
for char in s:
  if char in vow:
    s=s.replace(char,"")
print(s)
