import mkTokens
import mkComents

def geradorTable(code):
    outTable = []
    
    coments = mkComents.verifyAllComent(code)
    
    if coments == -1 or coments == 400:
        return("Erro em fechamento de comentario", ' ')
    linhas = coments.split("\n")

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
        condicional = mkTokens.verificaIf(linhas)
        identificador = mkTokens.verificaId(linhas)
        digito = mkTokens.verificaDigito(linhas)

    return (
        intCabecalho,
        parenteses,
        chaves,
        outros,
        reservedWord,
        atribuicao,
        aritmetico,
        negacao,
        logicos,
        condicional,
        identificador,
        digito
    )
#verifyFechamento.verifyChaves(pontuacao)

# print(parenteses)
# print(chaves)
# print(outros)
# print(reservedWord)
# print(intCabecalho)
# print(atribuicao)
# print(aritmetico)
# print(negacao)
# print(logicos)
# print(condicional)
# print(identificador)
# print(digito)