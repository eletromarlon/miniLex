def verifyOneComents(linguica):
    l = 0
    k = 0

    for m in linguica:
        if m == '#' and l == 0:
            k += 1
    
    l += 1
       
    #print("l: ",l ," k: ",k ," i: ", i," j: " ,j  )
    
    def verifyComent(linguica):
        i = 0
        j = 0
     
        startComent = 0
        finishComent = 0
        coment = ""
        
        print("passou")
        
        for n in linguica:
            if n == '#' and i < 1:
                startComent = j
                i += 1
                #print(n, j, startComent)
            else:
                if n == '#' and i > 0:
                    finishComent = j
                    coment = linguica[(startComent + 1):(finishComent)]
                    linguica = linguica[:startComent] + linguica[finishComent + 1:]
                    print(coment, "posicao ", j)
                    if k / 2 != 0:
                        print(linguica)
                        verifyComent(linguica)
                    else:
                        if k % 2 != 0:
                            print("Erro")
                            return -1  
                    #print(linguica)
                    return linguica 
                
                #print(n, j, finishComent)
            j += 1
    return "Erro Geral em mkComents.py"
    
    
    # j = startComent
    # for k in range(finishComent - startComent):
    #     linguica.pop(0)
    #     j += 1 
    
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