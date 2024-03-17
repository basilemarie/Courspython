#Exercice 4

available_words = []
file = open("frenchssaccent.dic",'r')
for row in file:
    available_words.append(row[0:len(row)-1])
file.close()

points = {'a' : 1, 'e' : 1,'i' : 1,'l' : 1,'n' : 1,'o' : 1,'r' : 1,'s' : 1,'t' : 1,'u' : 1,'d' : 2,'g' : 2,'m' : 2,'b' : 3,'c' : 3,'p' : 3,'f' : 4,'h' : 4,'v' : 4,'j' : 8,'q' : 8,'k' : 10,'w' : 10,'x' : 10,'y' : 10,'z' : 10,'-':0, '?':0}
alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
#algo needed for the main algo 

def score(words):
    score = 0
    for letter in words : 
        score = score + points[letter]
    return(score)

def max_score(words):
    score_max = 0
    for word in words:
        result = score(word,points) #maximum technic
        if result>score_max:
            score_max = result 
            solution = word
    return(solution,score_max)


def high_score(tirage,words): 
    max = 0
    for word in words:#be certain to cover all the words
        letters = list(tirage) #making sure that tirage isn't changed
        useful = 1
        for letter in word:
            if letter not in letters: #we can't use the word
                useful = 0
            else:
                letters.remove(letter) #making sure that one letter is not repeted in the word 

        if useful==1 and score(word)> max: #no letters can be missed and the words are only constituted by letters of the lexic 
            max = score(word)
            solution = word
    return (solution,max)



def joker(tirage,words): 
    bestscore = 0
    tirage.remove('?')
    for letter in alphabet:
        letters = list(tirage)
        letters.append(letter)
        word,score = high_score(letters,words)
        if score >bestscore:
            solution = word
            bestscore = score
    return (solution, bestscore)

final = joker(['x', 'z', 'c', 'v', 'r', 'r', 't','?'],available_words)
print(final)