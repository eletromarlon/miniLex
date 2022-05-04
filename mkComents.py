#import testeComentarioOK as coment

def verifyAllComent(linguica):
    acc1 = linguica
    
    while verifyComent(acc1) != -1:
        acc1 = verifyComent(acc1)
    
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
    
    #print("Codigo inicial\n", linguica)
    
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
                #print("\n\n\nComentario removido\n ", coment, "\nfechamento na string posicao ", j)    
                return linguica
            else:
                if k % 2 != 0:
                    print("valor de k", k)
                    return 400
        j += 1
    return -1

# def verifyOneComents(linguica):
#     l = 0
#     k = 0

#     for m in linguica:
#         if m == '#' and l == 0:
#             k += 1
    
#     l += 1
       
    
#     def verifyComent():
#         i = 0
#         j = 0
     
#         startComent = 0
#         finishComent = 0
#         coment = ""
        
#         print("passou")
        
#         for n in linguica:
#             if n == '#' and i < 1:
#                 startComent = j
#                 i += 1
#                 #print(n, j, startComent)
#             else:
#                 if n == '#' and i > 0:
#                     finishComent = j
#                     coment = linguica[(startComent + 1):(finishComent)]
#                     linguica = linguica[:startComent] + linguica[finishComent + 1:]
#                     print(coment, "posicao ", j)
#                     if k / 2 != 0:
#                         print(linguica)
#                         verifyComent(linguica)
#                     else:
#                         if k % 2 != 0:
#                             print("Erro")
#                             return -1  
#                     #print(linguica)
#                     return linguica 
                
#                 #print(n, j, finishComent)
#             j += 1
#     return verifyComent