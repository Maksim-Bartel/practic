import re

texts = input()
text= re.split(r'(?<=[.?!]) ',texts)
clean=[]
for pos in text:
    sen=pos.split()

    res = ""

    for i in range(len(sen)):
        if i>0:
         res+=" "
        res+=sen[i]
    if res:
        clean.append(res)
print("\nПредложения:")
for pos in clean:
    print(pos)
print(f"\nПредложений в тексте: {len(clean)}")

