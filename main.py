from soupsieve import comments
import mkTokens
import mkComents
arq = open("teste.txt")
arquivo = arq.read()

coments = mkComents.verifyAllComent(arquivo)

linhas = coments.split("\n")

#comentLine = coments.split("\n")

if coments != 400:
    intCabecalho = mkTokens.verificaTipo(linhas)
    parenteses = mkTokens.verificaParenteses(linhas)
    chaves = mkTokens.verificaChaves(linhas)
    outros = mkTokens.verificaOutros(linhas)
    reservedWord = mkTokens.verificaMain(linhas)
    atribuicao= mkTokens.verificaAtribuicao(linhas)
    aritmetico = mkTokens.verificaAritmetico(linhas)
    negacao = mkTokens.verificaNegacao(linhas)
    logicos = mkTokens.verificaLogico(linhas)

#verifyFechamento.verifyChaves(pontuacao)

print(parenteses)
print(chaves)
print(outros)
print(reservedWord)
print(intCabecalho)
print(atribuicao)
print(aritmetico)
print(negacao)
print(logicos)

# comentFuncionando = testeComentarioOK.verifyComent(arquivo)

# print("\n\nRestante do codigo sem o coment: \n", comentFuncionando)

#Antes de mandar para analisador, devo mandar para verificador de comentario mkComents.



# for n in cabecalho:
#     print(n)
# for n in pontuacao:
#     print(n)
# for n in atribuicao:
#     print(n)
# for n in funcao:
#     print(n)
# for n in negacao:
#     print(n)

#for linha in linhas:
#    print(linha)

