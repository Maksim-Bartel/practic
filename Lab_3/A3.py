
prev=int(input("Введите показания за предыдущий месяц"))
now=int(input("Введите показания за текщий месяц"))
if now>=prev:
 used = now - prev
else:
    used = (10000-prev)+ now
if used<=300:
    payment = 21.00
elif used <= 600:
    payment = 21.00 + (used - 300) * 0.06
elif used <= 800:
    payment = 21.00 + 300 * 0.06 + (used - 600) * 0.04
else:
    payment = 21.00 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025
if used > 0:
    price = payment / used
else:
    price = 0
print(f"{'Предыдущее':<12} {'Текущее':<8} {'Использовано':<12} {'К оплате':<10} {'Ср. цена m^3':<12}")
print(f"{prev:<12} {now:<8} {used:<12} {payment:<10.2f} {price:<12.2f}")

