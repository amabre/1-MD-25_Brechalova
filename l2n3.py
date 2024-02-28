s=input()
n=0
for i in s:
    if i=="ф" or i=="Ф":
        n=1
if n==1:
    print("Ого! Это редкое слово!")
else:
    print("Эх, это не очень редкое слово...")