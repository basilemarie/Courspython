#We can use a dictionnary to represent the points of each letters
available_words = []
file = open("frenchssaccent.dic",'r')
for row in file:
    available_words.append(row[0:len(row)-1])
file.close()

points = {'a' : 1, 'e' : 1,'i' : 1,'l' : 1,'n' : 1,'o' : 1,'r' : 1,'s' : 1,'t' : 1,'u' : 1,'d' : 2,'g' : 2,'m' : 2,'b' : 3,'c' : 3,'p' : 3,'f' : 4,'h' : 4,'v' : 4,'j' : 8,'q' : 8,'k' : 10,'w' : 10,'x' : 10,'y' : 10,'z' : 10,'-':0}


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

#r = max_score(['rte', 'ver', 'ce','vatu'],{'r':2,'v':6,'e':1,'c':4,'t':4,'a':10,'u':15})
#print(r)

def high_score(tirage,words,point): 
    max = 0
    for word in words:#be certain to cover all the words
        letters = list(tirage) #making sure that tirage isn't changed
        useful = 1
        for letter in word:
            if letter not in letters: #we can't use the word
                useful = 0
            else:
                letters.remove(letter) #making sure that one letter is not repeted in the word 

        if useful==1 and score(word,point)> max: #no letters can be missed and the words are only constituted by letters of the lexic 
            max = score(word,point)
            solution = word
    return (solution,max)
    

r = high_score(['a', 'r', 'b', 'g', 'e', 's', 'c', 'j'],available_words,points)
print((r))
