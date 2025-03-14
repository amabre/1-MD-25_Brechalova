a=int(input())
if a>36 and a<55:
    mes="боковое"
    print(mes)
elif a>0 and a<37:
    mes="в купе,"
    if a%2==0:
        pozi="верхнее"
    else:
        pozi = "нижнее"
    print(mes,pozi)
else:
    print("ошибка")
