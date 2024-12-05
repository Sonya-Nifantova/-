a=input("Введите месяц ")
s=int(input("Введите дату "))
if a=='декабрь' and s>=22 or a=="январь" and s<=19:
    print("козерок")
elif a=='январь' and s>=20 or a=='февраль' and s<=18:
    print("водолей")
elif a=='февраль' and s>=19 or a=='март' and s<=20:
    print("рыбы")
elif a=='март' and s>=21 or a=='апрель' and s<=19:
    print("овен")
elif a=='апрель' and s>=20 or a=='май' and s<=20:
    print("телец")
elif a=='май' and s>=21 or a=='июнь' and s<=20:
    print("близнецы")
elif a=='июнь' and s>=21 or a=='июль' and s<=22:
    print("рак")
elif a=='июль' and s>=23 or a=='август' and s<=22:
    print("лев")
elif a=='август' and s>=23 or a=='сентябрь' and s<=22:
    print("дева")
elif a=='сентябрь' and s>=23 or a=='октябрь' and s<=22:
    print("весы")
elif a=='октябрь' and s>=23 or a=='ноябрь' and s<=21:
    print("скорпион")
elif a=='ноябрь' and s>=22 or a=='декабрь' and s<=21:
    print("стрелец")
else:
    print("ошибка")
