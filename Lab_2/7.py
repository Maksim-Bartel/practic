x1 = int(input("Введите x1:"))
y1 = int(input("Введите y1:"))
x2 = int(input("Введите x2:"))
y2 = int(input("Введите y2:"))

color1 = 'White' if (x1 + y1) % 2 == 0 else 'Black'

color2 = 'White' if (x2 + y2) % 2 == 0 else 'Black'

if color1 == color2:
    print("YES")
    print(color1)
else:
    print("NO")
    print(color2)

