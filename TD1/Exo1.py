def lexical(tirage,words):
    max = 0  
    useful = 1
    for word in words:
        letters = tirage.copy()
        if len(word)>max: #not useful to seek for words smaller than the max 
            count = 0 #counter for the number of letters 
            for letter in word:
                if letter in letters:
                    count = count+1
                    letters.remove(letter)
                else:
                    useful = 0
            if count>max and useful ==1: #no letters can be missed and the words are only constituted by letters of the lexic
                solution = word
                max = count  
                
    return(solution)

final = lexical(['b', 'p', 'd', 'w', 's', 'y', 'w', 'i'],['bis', 'bd','wsibpa','bisi'])
print('Le mot le plus long pouvant être écris avec les lettres du tirage est', final)



