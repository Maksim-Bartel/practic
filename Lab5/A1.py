text=str(input())
def crez (text):
 while '(' in text:
    left=text.find('(')
    right=text.find(')',left)
    if right !=1 :
        text=text.replace(text[left:right + 1], '')
    else :
        text=text[:left]
 return text

print(crez(text))
