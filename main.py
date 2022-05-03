import mkTokens
import mkComents
import testeComentarioOK
#import analisador
arq = open("teste.txt")
arquivo = arq.read()
linhas = arq.readlines()

comentFuncionando = testeComentarioOK.verifyComent(arquivo)

print("\n\nRestante do codigo sem o coment: \n", comentFuncionando)

#Antes de mandar para analisador, devo mandar para verificador de comentario mkComents.

cabecalho = mkTokens.verificaInt(comentFuncionando.split("\n"))
pontuacao = mkTokens.verificaPontuacao(comentFuncionando.split("\n"))
atribuicao = mkTokens.verificaAtribuicao(comentFuncionando.split("\n"))
funcao = mkTokens.verificaMain(comentFuncionando.split("\n"))
negacao = mkTokens.verificaNegacao(comentFuncionando.split("\n"))

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

teste = mkComents.verifyOneComents(comentFuncionando)

print(teste)
#for linha in linhas:
#    print(linha)

