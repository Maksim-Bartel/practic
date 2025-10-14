x1=float(input("Введите координату"))
y1=float(input("Введите координату"))
x2=float(input("Введите координату"))
y2=float(input("Введите координату"))

if x1>0 and y1>0 and x2>0 and y2>0:
    print("Да , первая четверть")
elif x1<0 and y1>0 and x2<0 and y2>0:
    print("Да , вторая четверть")
elif x1<0 and y1<0 and x2<0 and y2<0:
    print("Да , третья четверть")
elif x1>0 and y1<0 and x2>0 and y2<0:
   print("Да , четвертая четверть")
else:
    print("NO")
