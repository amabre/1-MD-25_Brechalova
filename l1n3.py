a=int(input())
if a%4==0:
    if a%100==0:
        if a % 400 == 0:
            v=1
        else:
            v=0
    else:v=1
else:
    v=0
if v==1:
    print("Год",a,"- високосный")
else: print("Этот год високосный")