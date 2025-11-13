import re

text = 'He jests at scars. That never felt a wound!   Hello, friend!   Are you OK?'
sen = re.split(r'(?<=[.?!]) +', text)

def print_sen(items):
    for item in items:
        print(item)
        

print_sen(sen)
print(f'Предложений в тексте: {len(sen)}')


