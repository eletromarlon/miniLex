import mkTokens
#import analisador
arq = open("teste.txt")
linhas = arq.readlines()

#print(linhas)

cabecalho = mkTokens.verificaInt(linhas)
pontuacao = mkTokens.verificaPontuacao(linhas)
atribuicao = mkTokens.verificaAtribuicao(linhas)
funcao = mkTokens.verificaMain(linhas)
negacao = mkTokens.verificaNegacao(linhas)

for n in cabecalho:
    print(n)
for n in pontuacao:
    print(n)
for n in atribuicao:
    print(n)
for n in funcao:
    print(n)
for n in negacao:
    print(n)
    
#for linha in linhas:
#    print(linha)

