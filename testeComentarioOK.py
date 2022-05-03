def verifyComent(linguica):
    i = 0
    j = 0
    startComent = 0
    finishComent = 0
    coment = ""
    
    print("Codigo inicial\n", linguica)
    
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
                print("\n\n\nComentario removido\n ", coment, "\nfechamento na string posicao ", j)    
                return linguica
        j += 1