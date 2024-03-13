def lexical(tirage,words):
    max = 0
    for word in words:
        if len(word)>max:
            count = 0
            for letters in word:
                if letters in tirage:
                    count = count+1
            if count>max and count == len(word):
                solution = word
                max = count
    return(solution)

assert(lexical(['b', 'p', 'd', 'w', 's', 'y', 'w', 'i'],['bis', 'bd'])=='bis')

