#We can use a dictionnary to represent the points of each letters

def score(words,point):
    score = 0
    for letter in words : 
        score = score + point[letter]
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

#r = max_score(['rte', 'ver', 'ce'],{'r':2,'v':6,'e':1,'c':4,'t':4})
#print(r)

def high_score(tirage,words,point):
    word,maxpoint = max_score(words,point)
    for letter in word:
        if letter not in tirage:
            words.remove(word)
            high_score(tirage,words,point)
    return(word) #we're sure that the letter of the word are in tirage and the word is the highest in score

r = high_score(['r','t','e','c','v'],['rte', 'ver', 'ce','vatu'],{'r':2,'v':6,'e':1,'c':4,'t':4,'a':10,'u':15})
print((r))
