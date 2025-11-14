def read_protein_data (filename):

  proteins=[]
  file = open(filename, 'r',encoding='utf-8')

  for line in file:
     parts=line.strip().split('\t')
     protein_data= (
         parts[0].strip(), 
         parts[1].strip(),
         parts[2].strip() 
         )
     proteins.append(protein_data)
  return proteins
  
def encode (sequence):
    if not sequence:
        return ''
    encoded = ''
    counter = 1
    char=sequence[0]
  
    for i in range(1,len(sequence)):
        if sequence[i] == char:
            counter+=1
        else:
            if counter>2:
                encoded += str(counter)+char
            else:
                encoded += char * counter
            counter=1
            char=sequence[i]
    if counter > 2:
        encoded += str(counter) + char
    else:
        encoded += char * counter

    return encoded  




