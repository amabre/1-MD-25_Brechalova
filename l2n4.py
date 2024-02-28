import random
err=0
pr=0
while err!=3:
    x1=random.randint(1,10)
    x2=random.randint(1, 10)
    ps=int(input(f"{x1}+{x2}="))
    if ps==x1+x2:
        pr=pr+1
        print(":)")
    else:
        err=err+1
        print(":(")
print (f"Игра окончена. Правильных ответов: {pr}")
