def max_contig_sum(L):
    

    if(len(L) == 1):
        return L[0]
    elif(len(L) == 0):
        return 0
    
    maxval = L[0]
    for i in range(1, len(L)):
        if (L[i] > maxval + L[i]):
            maxval = L[i]
        else:
            maxval += L[i]

    maxval -= L[-1]
    if (L[-1] > maxval + L[-1]):
        maxval = L[-1]
    elif(L[-1] + maxval > maxval):
        maxval += L[-1]

    if (max(L) > maxval):
        maxval = max(L)

    return maxval

    



            
val =  [3, 4, -8, 3, 3, 1, -7, 15, -1, 2]

print(max_contig_sum(val))