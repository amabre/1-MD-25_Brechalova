s=input()
n=0
i=len(s)-1
while i!=-1:
    if s[i]=="ф" or s[i]=="Ф":
        n = 1
    i=i-1
"""for i in s:
    if i=="ф" or i=="Ф":
        n=1 """
if n==1:
    print("Ого! Это редкое слово!")
else:
    print("Эх, это не очень редкое слово...")