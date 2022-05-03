def verificaComents(linguica):
    i = 0
    j = 0
    startComent = 0
    finishComent = 0
    coment = ""
    
    for n in linguica:
        if n == '#' and i < 1:
            startComent = j
            i += 1
            #print(n, j, startComent)
        else:
            if n == '#' and i > 0:
                finishComent = j
            #print(n, j, finishComent)
        j += 1
    
    coment = linguica[(startComent + 1):(finishComent)]
    
    linguica = linguica[:startComent] + linguica[finishComent + 1:]
    
    # j = startComent
    # for k in range(finishComent - startComent):
    #     linguica.pop(0)
    #     j += 1 
    
    print(coment, "\n" ,linguica)
    
    # for m in code:
    #     sizeM = m.length()
    #     print(sizeM)
    #     for n in m:
    #         if n == '#' and i < 1:
    #             startComent = j
    #             i += 1
    #         if n == '#' and i > 0:
                
    #     j += 1
    # return guarda