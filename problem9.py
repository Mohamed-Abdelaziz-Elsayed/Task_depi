num=int(input())
digit=0
while num!=0:
    digit=num%10+digit
    num=num//10
print(digit)    