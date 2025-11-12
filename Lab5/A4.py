def read_text (filename):

  text={}
  file = open(filename, 'r')

  for line in file:
     part=line.strip().split('\t')
     if len(part) == 3:
          protein, organism, sequence = part
          text[protein]={'organism':organism,'sequence':sequence}
  file.close()
  return text


