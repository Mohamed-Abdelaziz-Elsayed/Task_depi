inital=int(input())
end=int(input())
for i in range (inital, end):
    for j in range (inital,i):
      if i%j==0 :
         break
    else:
         print(i)