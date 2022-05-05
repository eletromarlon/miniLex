import generatorMain
arq = open("teste.txt")
arquivo = arq.read()

table = generatorMain.geradorTable(arquivo)

for m in table:
    print(m)