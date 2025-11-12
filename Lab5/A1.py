text=str(input())
def crez (text):
 while '(' in text:
    left=text.find('(')
    right=text.find(')',left)
    if right !=1 :
        text=text.replace(text[left:right + 1], '')
    else :
        text=text[:left]
    while ')' in text:
        right = text.find(')')
        text = text.replace(')', '', 1)
 return text

print(crez(text))

