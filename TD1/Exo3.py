#We can use a dictionnary to represent the points of each letters

def score(words,point):
    score = 0
    for letter in words : 
        score += point[letter]
    return(score)

assert(score('ab',{'a':1,'b':2})==3) #Rapid verification


def max_score(words,point):
    score_max = 0
    for word in words:
        result = score(word,point) #maximum technic
        if result>score_max:
            score_max = result 
            solution = word
    return(solution,score_max)

assert(max_score(['rte', 'ver', 'ce'],{'r':2,'v':6,'e':1,'c':4,'t':4})==('ver',9))

#r = max_score(['rte', 'ver', 'ce','vatu'],{'r':2,'v':6,'e':1,'c':4,'t':4,'a':10,'u':15})
#print(r)

def high_score(tirage,words,point): 
    value = len(words)
    for interation in range(value):#be certain to cover all the words
        letters = tirage.copy()
        useful = 1
        (word, scoring) = max_score(words,point)
        print(letters)
        for letter in word:
            if letter not in letters:
                useful = 0
            else:
                letters.remove(letter)

        if useful==1: #no letters can be missed and the words are only constituted by letters of the lexic
            bestword = word
            bestscore = scoring
            return((bestword,bestscore))
        elif useful ==0:
            words.remove(word)
    

r = high_score(['r','t','e','c','v'],['rte', 'ver', 'ce','vatu','verre'],{'r':2,'v':6,'e':1,'c':4,'t':4,'a':10,'u':15})
print((r))
