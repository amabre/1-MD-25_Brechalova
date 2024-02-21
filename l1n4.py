a=input()
b=input()
if a=="синий" and b=="желтый" or b=="синий" and a=="желтый":
    print("зеленый")
elif a=="красный" and b=="желтый" or b=="с=красный" and a=="желтый":
    print("оранжевый")
elif a=="синий" and b=="красный" or b=="синий" and a=="красный":
    print("фиолетовый")
else:
    print("ошибка")