import random
import math
err=0
pr=0
while err!=3:
    x1=random.randint(-10,10)
    x2=random.randint(-10, 10)
    if x2/math.fabs(x2)==-1:
        ps = int(input(f"{x1}-{int(math.fabs(x2))}="))
    else:
        ps=int(input(f"{x1}+{x2}="))
    if ps==x1+x2:
        pr=pr+1
        print(":)")
    else:
        err=err+1
        print(":(")
print (f"Игра окончена. Правильных ответов: {pr}")
