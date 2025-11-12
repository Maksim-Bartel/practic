
import re

texts = input()
text= re.split(r'(?<=[.?!]) ',texts)
clean=[]
for pos in text:
    sen=" ".join(pos.split())
    if sen:
        clean.append(sen)
print("\nПредложения:")
for pos in clean:
    print(pos)
print(f"\nПредложений в тексте: {len(clean)}")