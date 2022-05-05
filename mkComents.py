def verifyAllComent(linguica):
    acc1 = linguica
    i = 0
    
    while verifyComent(acc1) != -1 :
        i += 1
        acc1 = verifyComent(acc1)
        if acc1 == 400:
            return (400)
    
    return acc1

def verifyComent(linguica):
    i = 0
    j = 0
    k = 0

    startComent = 0
    finishComent = 0
    coment = ""
    
    for m in linguica:
        if m == '#':
            k += 1
    
    
    for n in linguica:
        if n == '#' and i < 1:
            startComent = j
            i += 1
        else:
            if n == '#' and i > 0:
                finishComent = j
                coment = linguica[(startComent + 1):(finishComent)]
                linguica = linguica[:startComent] + linguica[finishComent + 1:]
                print("\n\nComentario removido\n ", coment, j)    
                if k % 2 != 0:
                    return 400
                else:
                    return linguica
        j += 1
    return -1