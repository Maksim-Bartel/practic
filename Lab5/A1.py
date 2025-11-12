text=" Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь)() (())"

while '(' in text:
    left=text.find('(')
    right=text.find(')',left)
    if right !=1:
             text=text.replace(text[left:right+1],'')
    else :
        text=text[:left]


print(text)