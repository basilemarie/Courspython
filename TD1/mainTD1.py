#Definition of all the items needed for tests

available_words = []
file = open("frenchssaccent.dic",'r')
for row in file:
    available_words.append(row[0:len(row)-1])
file.close()

points = {'a' : 1, 'e' : 1,'i' : 1,'l' : 1,'n' : 1,'o' : 1,'r' : 1,'s' : 1,'t' : 1,'u' : 1,'d' : 2,'g' : 2,'m' : 2,'b' : 3,'c' : 3,'p' : 3,'f' : 4,'h' : 4,'v' : 4,'j' : 8,'q' : 8,'k' : 10,'w' : 10,'x' : 10,'y' : 10,'z' : 10,'-':0, '?':0}

#Exercise 2
#Code of the exercise 1

def lexical(tirage,words):
    max = 0  
    useful = 1
    for word in words:
        letters = tirage.copy()
        if len(word)>max: #not useful to seek for words smaller than the max 
            count = 0 #counter for the number of letters 
            for letter in word:
                if letter in letters:
                    count = count+1 #no condition on the repaetition of a letter 
                else:
                    useful = 0
            if count>max and useful ==1: #no letters can be missed and the words are only constituted by letters of the lexic
                solution = word
                max = count  
                
    return(solution)

final = lexical(['b', 'p', 'd', 'w', 's', 'y', 'w', 'i'],['bis', 'bd','wsibpa','bisi']) 
print('Le mot le plus long pouvant être écris avec les lettres du tirage est', final)

#Exercice 3 

#Construction programm

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



#Upgrade of the first exercice's code
#I prefer to use point as a variable in my function for a better adaptation 

def high_score(tirage,words,point): 
    max = 0
    for word in words:#be certain to cover all the words
        letters = list(tirage) #making sure that tirage isn't changed
        useful = 1
        for letter in word:
            if letter not in letters: #we can't use the word
                useful = 0
        if useful==1 and score(word,point)> max: #no letters can be missed and the words are only constituted by letters of the lexic 
            max = score(word,point)
            solution = word
    return (solution,max)

r = high_score(['a', 'r', 'b', 'g', 'e', 's', 'c', 'j'],available_words,points)
print((r))

#the result here is ('jacasser', 17)



#I don't truly understand if we have the authorization to use the same letter more than once in one word
#Here an alternative of high score providing the use of the same letter more than once

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


#the result here is ('jaser', 12)

#Exercice 4
#We'll use the same code with a slight modification 

def joker(tirage,words,point): 
    max = 0
    for word in words:#be certain to cover all the words
        letters = list(tirage) #making sure that tirage isn't changed
        useful = 1
        print(word)
        for letter in word:
            if letter not in letters: #we can't use the word
                useful = 0
            elif letter == '?': 
                letters.remove(letter) #Not possible to use '?' more than once however it is possible with the other letters
        if useful==1 and score(word,point)> max: #no letters can be missed and the words are only constituted by letters of the lexic 
            max = score(word,point)
            solution = word
    return (solution,max)

final = joker(['b', 'p', 'd', 's', 'y', 'w', 'i','?'],['bis', 'bd','wsibpa','bisi','bpdw?yi','bpdws?y?wi'],points)
print(final)
