def n1():
    a=int(input())
    if a%3==0:
        return "делится"
    else:
        return "не делится"

def delna100(a):
    if isinstance(a,str)==1 and  a.isdigit()==0:
        a100="ValueError"
    elif int(a)==0:
        a100="ZeroDivisionError"
    else:
        a100=100/int(a)
    return a100
def n2():
    a=input()
    print(delna100(a))

def n3():
    a=input("Введите дату в формате дд/мм/гггг: ")
    ad=int(a[:2])
    am = int(a[3:5])
    ay = int(a[6:])
    if ad>31 or am>12: return "неверный формат даты"
    if ad*am==ay%100:
        return "True"
    else:
        return "False"

def n4():
    a = input("Введите номер билета: ")
    l=len(a)
    if l%2==1: return "количество цифр должно быть четным"
    sum1=0
    sum2=0
    for i in range (int(l/2)):
        sum1=sum1+int(a[i])
        j=(i+1)*(-1)
        sum2 = sum2 + int(a[j])
    if sum1==sum2:
        return "билет является счастливым"
    else:
        return "билет не является счастливым"

print(n4())
