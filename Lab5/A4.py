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











