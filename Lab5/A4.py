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

def decode (werb):
    for i in range(len(werb)):
        if werb.isdigit():
            werb =werb.replace(werb[i],werb[i]*int(werb[i])-1)
    return werb









