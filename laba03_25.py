import random
def n1():
    a = []
    for i in range(5):
        a.append(random.randint(1, 10))
    ap = int(input("введите число: "))
    print(a, ap)
    if ap in a:
        print("вы угадали")
    else:
        print("вы не угадали")

def n2():
    a = []
    spov=[]
    pov=0
    for i in range(50):
        a.append(random.randint(1, 100))
    if len(a) != len(set(a)):
        for i in range (len(a)):
            for j in range(i+1, len(a)):
                if a[i]==a[j]:
                    if a[i] in spov:
                        continue
                    spov.append(a[i])
                    pov=pov+1
        print("В списке ", a, "\nесть повторяющиеся элементы: ", spov, "\nих количество:", pov)
    else:
        print("В списке ", a, "\nнет повторяющихся элементов")

def n3():
    days = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
    a=int(input("Сколько дней вы хотите отдыхать? "))
    ldays=list(days)
    print("Ваши выходные дни: ", ldays[-a:],"\nВаши рабочие дни: ", ldays[:7-a])

def n4():
    a1=["Свириденко", "Токарева", "Поспелова", "Анисимов", "Овчинников", "Гусева", "Екимова", "Орел", "Зайцев", "Зотова"]
    a2 = ["Клубничный", "Шоколадная", "Карамельная", "Миндальный", "Банановый", "Йогуртовый", "Персиковая", "Виноградная", "Вишневый", "Медовая"]
    #a#
    team= tuple(random.sample(a1, 5)+random.sample(a2, 5))
    #b#
    print("1-MD-25: ", a1, "\n1-MD-20: ", a2, "\nКоманда: ", team)
    #c#
    print("Количество человек в команде: ", len(team))
    #d#
    lteam=list(team)
    lteam.sort()
    print("По алфавиту: ", lteam)
    #e#
    if "Свириденко" in team:
        print("Свириденко встречается в списке 1 раз")
    else:
        print("Свириденко не встречается в списке")

n4()



