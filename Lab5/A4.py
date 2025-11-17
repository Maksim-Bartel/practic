import string
import re

file_commands = 'commands.0.txt'
file_proteins = 'sequences.0.txt'

def read_command(filename):
    proteins = []
    file = open(filename, 'r', encoding='utf-8')

    for line in file:
        parts = line.strip().split('\t')
        protein_data = (
            parts[0].strip(),
            parts[1].strip(),
            parts[2].strip()
        )
        proteins.append(protein_data)
    return proteins

def read_commands_data(filename):
    commands=[]
    file = open(filename, 'r',encoding='utf-8')

    for line in file:
       parts=line.strip().split('\t')
       commands_data= (
         parts[0].strip(),
         parts[1].strip(),
         )
       commands.append(commands_data)
    return commands

def decode (werb):
    word=""
    for i in range(len(werb)):
        if werb.isdigit():
            word =word+werb[i+1]*int(werb[i]-1)
        else:
            word=word+werb[i]
    return word

def search_data (protein):
    search=""
    protein=decode(protein)
    proteins=read_command(file_proteins)
    for i in range(len(proteins)):
        if (protein[i])[2].find(protein):
            search=(proteins[i])[1]+" "+ (proteins[i])[2]
    if search=="":
        return 'NOT FOUND'
    else:
        return search
def mode (protein):
    
    proteins=read_command(file_proteins)
    mode_app=""
    
    for i in range(len(proteins)):
        if (proteins[0]) == protein:
            mode_app=(proteins[i])[2]
    if protein == "":
        return 'MISSING'
        
    letters = dict()
    for i in mode_app:
        letters[i]=letters.get(i,0)+1
    letters_app = max(letters,key=letters.get)
    max_ver = letters[letters_app]
    
    for i in sorted(letters):
        print(i)
        if letters[i]==max_ver:
              letters_app=i
              break
    return letters_app,max_ver     
def diff(protein1, protein2):
    proteins = read_protein_data (file_proteins)
    f_protein1=''
    f_protein2=''
    for i in range(len(proteins)):
            if (proteins[i])[0]==protein1:
                f_protein1 = (proteins[i])[2]
    if f_protein1=='':
        return 'MISSING'

    for i in range(len(proteins)):
            if (proteins[i])[0]==protein2:
                f_protein2 = (proteins[i])[2]
    if f_protein2=='':
        return 'MISSING'

    if len(f_protein1)>len(f_protein2):
        max_protein = f_protein1
        min_protein = f_protein2
    else:
        max_protein=f_protein2
        min_protein = f_protein1

    answer_diff = (len(max_protein)-len(min_protein))

    for i in range(len(min_protein)):
        if min_protein[i] != max_protein[i]:
            answer_diff = answer_diff + 1

    return answer_diff













