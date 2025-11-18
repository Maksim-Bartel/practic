
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
       if parts[0]=='mode' or parts[0]=='search':
        commands_data= (
         parts[0].strip(),
         parts[1].strip(),
         )
       else:
           commands_data = (
               parts[0].strip(),
               parts[1].strip(),
               parts[2].strip()
           )
       commands.append(commands_data)
    return commands

def decode (werb):
    word=""
    for i in range(len(werb)):
        if werb[i].isdigit():
            word =word+werb[i+1]*int(werb[i]-1)
        else:
            word=word+werb[i]
    return word

def search_data (protein):
    search=""
    protein=decode(protein)
    proteins=read_command(file_proteins)
    for i in range(len(proteins)):
        if protein in (proteins[i])[2]:
            search=(proteins[i])[1]+" "+ (proteins[i])[0]
    return search
    if search=="": 
     return 'NOT FOUND'
    


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
        if letters[i]==max_ver:
              letters_app=i
              break
    return letters_app,max_ver

def diff(protein1, protein2):
    proteins = read_command (file_proteins)
    protein1_1=''
    protein2_2=''
    for i in range(len(proteins)):
            if (proteins[i])[0]==protein1:
                protein1_1 = (proteins[i])[2]
    if protein1_1=='':
        return 'MISSING'

    for i in range(len(proteins)):
            if (proteins[i])[0]==protein2_2:
                protein2_2 = (proteins[i])[2]
    if protein2_2=='':
        return 'MISSING'

    if len(protein1_1)>len(protein2_2):
        max_protein = protein1_1
        min_protein = protein2_2
    else:
        max_protein = protein2_2
        min_protein = protein1_1

    diff_ans = (len(max_protein)-len(min_protein))

    for i in range(len(min_protein)):
        if min_protein[i] != max_protein[i]:
            diff_ans += 1

    return diff_ans
file = open('genedata.txt','w')
file.write('Bartel Maksim\n')
file.write('Genetic Searching')
file.write('-'*50)
commands = read_commands_data(file_commands)
counter = 1
for i in range(len(commands)):
    if (commands[i])[0] == 'search':
        file.write("00"+str(counter))
        file.write(commands[i][0]+" "+decode(commands[i][1])+"\n")
        file.write('organism'+'protein''\n')
        file.write(search_data(commands[i]))
        file.write(mode((commands[i])[1])+'\n')
        file.write("-------------------------------------------------------------------------------------\n")
        counter+=1

        if commands[i][0]=="mode":
            file.write("00"+str(counter)+"  ")
            file.write(commands[i][0]+"  "+commands[i][1]+"  "+commands[i][2]+"\n")
            file.write('amino-acids difference:\n')
            file.write(str(diff(commands[i][1],commands[i][2]))+'\n')
            file.write("-------------------------------------------------------------------------------------\n")
            counter+=1















