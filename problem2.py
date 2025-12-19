word=input()
length=len(word)
count=0
for i in range(length):
    if (word[i]=="a"or word[i]=="o" or word[i]=="i" or word[i]=="e" or word[i]=="u"):
        count+=1
print(count)        