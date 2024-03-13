def lexical(tirage,words):
    max = 0  
    for word in words:
        if len(word)>max: #not useful to seek for words smaller than the max 
            count = 0 #counter for the number of letters 
            for letters in word:
                if letters in tirage:
                    count = count+1
            if count>max and count == len(word): #no letters can be missed and the words are only constituted by letters of the lexic
                solution = word
                max = count
    return(solution)

assert(lexical(['b', 'p', 'd', 'w', 's', 'y', 'w', 'i'],['bis', 'bd'])=='bis')

