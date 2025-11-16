def read_sequences(filename):

    proteins = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) >= 3:
                    protein_data = (
                        parts[0].strip(),
                        parts[1].strip(),
                        parts[2].strip()
                    )
                    proteins.append(protein_data)
        return proteins
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        return []


filename = "genedata.0.txt"
proteins = read_sequences(filename)
print(proteins)
for i, protein in enumerate(proteins, 1):
    name, organism, sequence = protein
    print(f"Белок:{i}")
    print(f"Название:{name}")
    print(f"Организм:{organism}")
    print(f"Аминокислоты:{sequence}")

def decode_rle(encoded_sequence):
    decoded = ""
    i = 0
    n = len(encoded_sequence)

    while i < n:
        char = encoded_sequence[i]

        if char.isdigit():
            count = int(char)

            next_char = encoded_sequence[i + 1] if i + 1 < n else ""
            decoded += next_char * count
            i += 2
        else:

            decoded += char
            i += 1

    return decoded
decoded_sequence = decode_rle(proteins)
print(decoded_sequence)


def search_data(seq, pattern: str):
    decoded_pattern = decode_rle(pattern)
    result = []
    for protein_tuple in seq:
        name, organism, sequence = protein_tuple
        if pattern in sequence:
            result.append(f'{organism} \t {name}')
    return result if result else ["NOT FOUND"]


sequences = read_sequences("genedata.0.txt")
print(f"Прочитано белков: {len(sequences)}")

results = search_data(sequences, "SIIK")
print(f"Результат: {results}")

def diff_operation(proteins, protein1,protein2):

    protein1_data = None
    protein2_data = None
    for protein in proteins:
        name, organism, sequence = protein
        if name == protein1:
            protein1_data = (name, organism, sequence)
        if name == protein2:
            protein2_data = (name, organism, sequence)

    missing = []
    if protein1_data is None:
        missing.append(protein1)
    if protein2_data is None:
        missing.append(protein2)
    if missing:
        return f"MISSING: {', '.join(missing)}"

    name1, org1, seq1 = protein1_data
    name2, org2, seq2 = protein2_data
    diff = 0
    length = min(len(seq1)),len(seq2)

    for i in range(length):
        if seq1[i] != seq2[i]:
            diff += 1
    diff = abs(len(seq1) - len(seq2))
    return str(diff)
def mode (proteins, protein_name):

    target_protein=None

    for protein in proteins:
        name, organism, sequence = protein
        if name == protein_name:
            target_protein = (name, organism, sequence)
            break

    if target_protein is None:
        return "NOT FOUND"

    name, organism , sequence  = target_protein

    counter_amino={}

    for amino in sequence:
        counter_amino[amino] = counter_amino.get(amino, 0) + 1
    count=0

    most_amino = ''
    for amino,counts in counter_amino.items():
        if counts > count or (counts == count and amino < most_amino):
            most_amino = amino
            count = counts

    return (f'{most_amino} {count}')

def process_commands(sequences_file, commands_file, output_file):
   

    proteins = read_sequences(sequences_file)
    if not proteins:
        print("Нет данных для обработки")
        return

    try:
        with open(commands_file, 'r', encoding='utf-8') as file:
            commands = file.readlines()
    except FileNotFoundError:
        print(f"Ошибка: файл {commands_file} не найден")
        return

    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write("Ваше Имя\n")
        out_file.write("Генетический поиск\n")


        for i, command_line in enumerate(commands, 1):
            parts = command_line.strip().split('\t')
            operation = parts[0]

            out_file.write(f"{i:03d}\n")
            out_file.write("-" * 50 + "\n")

            if operation == "search":
                if len(parts) >= 2:
                    pattern = parts[1]
                    results = search_data(proteins, pattern)
                    for result in results:
                        out_file.write(result + "\n")

            elif operation == "diff":
                if len(parts) >= 3:
                    protein1 = parts[1]
                    protein2 = parts[2]
                    result = diff_operation(proteins, protein1, protein2)
                    out_file.write(f"amino-acids difference: {result}\n")

            elif operation == "mode":
                if len(parts) >= 2:
                    protein_name = parts[1]
                    result = mode(proteins, protein_name)
                    out_file.write(f"amino-acid occurs: {result}\n")

            out_file.write("-" * 50 + "\n")

    print(f"Обработка завершена. Результат в файле {output_file}")

process_commands("sequences.txt", "commands.txt", "genedata.0.txt")







