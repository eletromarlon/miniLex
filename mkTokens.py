

def verificaInt(code):
    i = 0
    j = 0
    header = "int"
    guarda = []

    for m in code:
        for n in m:
            if header[i] == n:
                #print(i)
                if n == 't':
                    guarda.append(("< tipo, int >", "int", (j + 1)))
                    break
                i += 1
            else:
                i=0
        j += 1
    return guarda

def verificaPontuacao(code):
    j = 0
    header = "{}():,"
    guarda = []

    for m in code:
        i = 0
        for n in m:
            #print(header.find(n), j, n)
            if header.find(n) > -1:
            #if header[i] == n and k < 1:
            #    print(header.find(n))
                guarda.append(("< tipo, " + n + " >", n, (j + 1)))
                
        j += 1
    return guarda
    
def verificaAtribuicao(code):
    j = 0
    header = "="
    guarda = []

    for m in code:
        i = 0
        for n in m:
            #print(header.find(n), j, n)
            if header.find(n) > -1:
            #if header[i] == n and k < 1:
            #    print(header.find(n))
                guarda.append(("< tipo, " + n + " >", n, (j + 1)))
            
        j += 1
    return guarda


def verificaMain(code):
    j = 0
    k = 0
    header = "main"
    guarda = []

    for m in code:
        i = 0
        for n in m:
            if header[i] == n:
                #print(i)
                if n == 'n':
                    guarda.append(("< tipo, main >", "main", (j + 1)))
                    break
                if i < 4:
                    i += 1
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
                guarda.append(("< tipo, " + n + " >", n, (j + 1)))
        j += 1
    return guarda

'''def automatoOpenEscopo(code):
    i = 0
    j = 0

    for m in code:
        for n in m:
            if n == '{':
                return ("token", "lexema", (j + 1))
        j += 1

def automatoCloseEscopo(code):
    i = 0
    j = 0

    for m in code:
        for n in m:
            if n == '}':
                return ("token", "lexema", (j + 1))
        j += 1

def automatoDeclaracao(code):
    i = 0
    j = 0
    header = "int"

    #for m in code:
    #    for n in m:
    #        print(n)

    for m in code:
        for n in m:
            if header[i] == n:
                #print(i)
                if n == ')':
                    return ("token", "lexema", (j + 1))
                i += 1
            else:
                i=0
        #else:
        #    l += 1
        j += 1
        '''