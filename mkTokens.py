from os import remove


def verificaTipo(code):
    j = 0
    guarda = []

    for m in code:
        if 'int' in m:
            guarda.append(("< tipo, int >", "int", (j + 1)))
        else:
            if 'float' in m:
                guarda.append(("< tipo, float >", "float", (j + 1)))
            else:
                if 'bool' in m:
                    guarda.append(("< tipo, boolean >", "bool", (j + 1)))
                else:
                    if 'char' in m:
                        guarda.append(("< tipo, char >", "char", (j + 1)))
        j += 1
    return guarda

def verificaMain(code):
    j = 0
    guarda = []

    for m in code:
        i = 0
        if 'main' in m:
            guarda.append(("< reserved, main >", "main", (j + 1)))
        j += 1
    return guarda

def verificaIf(code):
    j = 0
    i = 0
    guarda = []

    for m in code:
        if 'if' in m:
            k = len(m)
            if ':' == m[k-1]:
                #guarda.append(("< condicional, if >", "if", (j + 1)))
                i += 1
        else:
            if i > 0 and ' ' in m[0]:
                if m[1] == ' ':
                    if m[2] == ' ':
                        if m[3] == ' ':
                            guarda.append(("< condicional, if >", "if", (j)))   # só j porque verificou
                            return guarda                                       # a linha seguinte
        j += 1
    return "Erro de identacao ou falta ':' na linha do if"

def verificaId(code):
    j = 0
    i = 0
    guarda = []

    for m in code:
        if 'int' in m:
            if 'main' in m:
                continue
            for n in m:
                i += 1
                if i > 4:
                    guarda.append(("< Id, "+ n +" >" , n, (j + 2)))# 2 por conta do continue
                    if n == ' ':
                        i = 0
        if 'float' in m:
            i = 0
            if 'main' in m:
                continue
            for n in m:
                i += 1
                if i > 6:
                    guarda.append(("< Id, "+ n +" >" , n, (j + 2)))# 2 por conta do continue
                    if n == ' ':
                        i = 0
        if 'bool' in m:
            i = 0
            if 'main' in m:
                continue
            for n in m:
                i += 1
                if i > 5:
                    guarda.append(("< Id, "+ n +" >" , n, (j + 2)))# 2 por conta do continue
                    if n == ' ':
                        break
        if 'char' in m:
            i = 0
            if 'main' in m:
                continue
            for n in m:
                i += 1
                if i > 5:
                    guarda.append(("< Id, "+ n +" >" , n, (j + 2))) # 2 por conta do continue
                    if n == ' ':
                        i = 0
        j += 1
    
    for e in guarda:
        if e[1] == ' ':
            guarda.remove(e)
    
    return guarda

def verificaDigito(code):
    j = 0
    i = 0
    guarda = []
    temp = []

    for m in code:
        if '=' in m:
            k = m.index('=')
            #print("valor de k ", k, "k + 1 ", m[k+1])
            temp = m[k+1:len(m)]
            if 'true' in temp or 'false' in temp:
                guarda.append(("< boolean, "+ temp +" >" , temp, (j + 1)))
                temp = []
            else:
                guarda.append(("< digito, "+ temp +" >" , temp, (j + 1)))
                temp = []
        j += 1
    return guarda

def verificaLogico(code):
    j = 0
    guarda = []

    for m in code:
        i = 0
        if 'and' in m:
            guarda.append(("< logic, and >", "and", (j + 1)))
        else:
            if 'or' in m:
                guarda.append(("< logic, or >", "or", (j + 1)))
        j += 1
    return guarda

def verificaParenteses(code):
    j = 0
    guarda = []
    i = 0
    
    for m in code:
        for n in m:
            if n == '(' and i < 1:
                guarda.append(("< pontuacao, " + n + " >", n, (j + 1)))
                i += 1
            else:
                if n == ')' and i > 0:
                    guarda.append(("< pontuacao, " + n + " >", n, (j + 1)))
                    i = 0
            
        j += 1
    return guarda

def verificaChaves(code):
    j = 0
    guarda = []
    i = 0
    
    for m in code:
        for n in m:
            if n == '{' and i < 1:
                guarda.append(("< pontuacao, " + n + " >", n, (j + 1)))
                i += 1
            else:
                if n == '}' and i > 0:
                    guarda.append(("< pontuacao, " + n + " >", n, (j + 1)))
                    i = 0
        j += 1
    return guarda

def verificaOutros(code):
    j = 0
    header = ":,"
    guarda = []

    for m in code:
        i = 0
        for n in m:
            if header.find(n) > -1:
                guarda.append(("< pontuacao, " + n + " >", n, (j + 1)))
                
        j += 1
    return guarda

def verificaAtribuicao(code):
    j = 0
    guarda = []

    for m in code:
        i = 0
        for n in m:
            if n == '=':
                guarda.append(("< relacional, " + n + " >", n, (j + 1)))
        j += 1
    return guarda

def verificaNegacao(code):
    j = 0
    header = "!"
    guarda = []

    for m in code:
        i = 0
        for n in m:
            if header.find(n) > -1:
                guarda.append(("< logico, " + n + " >", n, (j + 1)))
        j += 1
    return guarda

def verificaAritmetico(code):
    j = 0
    guarda = []

    for m in code:
        for n in m:
            if n == '+':
                guarda.append(("< aritmetico, " + n + " >", n, (j + 1)))
            else:
                if n == '-':
                    guarda.append(("< aritmetico, " + n + " >", n, (j + 1)))
                else:
                    if n == '*':
                        guarda.append(("< aritmetico, " + n + " >", n, (j + 1)))
                    else:
                        if n == '/':
                            guarda.append(("< aritmetico, " + n + " >", n, (j + 1)))
        j += 1
    return guarda