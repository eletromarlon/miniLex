def verifyAllComent(linguica):
    acc1 = linguica
    i = 0
    k = 0
    
    for m in linguica:
        if m == '#':
            k += 1
    
    while (k/2) > 0 :
        i += 1
        k -= 2
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
    coment = []
    
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
                coment.append(linguica[(startComent + 1):(finishComent)]) 
                linguica = linguica[:startComent] + linguica[finishComent + 1:]
                #print(coment)
                if k % 2 != 0:
                    return 400
                else:
                    print(coment)
                    return linguica
        j += 1
    return -1