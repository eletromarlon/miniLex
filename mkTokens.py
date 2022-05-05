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
                
        # for n in m:
        #     if header[i] == n:
        #         #print(i)
        #         if n == 't':
        #             guarda.append(("< tipo, int >", "int", (j + 1)))
        #             break
        #         i += 1
        #     else:
        #         i=0
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
            #print(header.find(n), j, n)
            if header.find(n) > -1:
            #if header[i] == n and k < 1:
            #    print(header.find(n))
                guarda.append(("< pontuacao, " + n + " >", n, (j + 1)))
                
        j += 1
    return guarda

def verificaAtribuicao(code):
    j = 0
    header = "="
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