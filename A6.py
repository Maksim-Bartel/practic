n=int(input("Введите количество секунд"))
hours=(n//3600)%24
minutes=(n//3600)%60
seconds=n%60
if len(str(hours)) == 1:
    hours = "0" + str(hours)
if len(str(minutes)) == 1:
     minutes = "0" + str(minutes)
if len(str(seconds)) == 1:
    seconds = "0" + str(seconds)
print(f"{hours}:{minutes}:{seconds}")

