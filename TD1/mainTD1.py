#Definition of all the items needed for tests

available_words = []
file = open("frenchssaccent.dic",'r')
for row in file:
    available_words.append(row[0:len(row)-1])
file.close()

#all the dictionnaries needed for the codes

tirage = ['b', 'p', 'd', 'w', 's', 'y', 'w', 'i']
points = {'a' : 1, 'e' : 1,'i' : 1,'l' : 1,'n' : 1,'o' : 1,'r' : 1,'s' : 1,'t' : 1,'u' : 1,'d' : 2,'g' : 2,'m' : 2,'b' : 3,'c' : 3,'p' : 3,'f' : 4,'h' : 4,'v' : 4,'j' : 8,'q' : 8,'k' : 10,'w' : 10,'x' : 10,'y' : 10,'z' : 10,'-':0, '?':0}
alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}


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


#Exercice 3 

#Construction programm

def score(words):
    score = 0
    for letter in words : 
        score = score + points[letter]
    return(score)


def max_score(words):
    score_max = 0
    for word in words:
        result = score(word) #maximum technic
        if result>score_max:
            score_max = result 
            solution = word
    return(solution,score_max)


#Upgrade of the first exercice's code
#I tend to use a variable called point in my codes but it is not asked in the exercise

def high_score(tirage,words): 
    max = 0
    for word in words:#be certain to cover all the words
        letters = list(tirage) #making sure that tirage isn't changed
        useful = 1
        for letter in word:
            if letter not in letters: #we can't use the word
                useful = 0
        if useful==1 and score(word)> max: #no letters can be missed and the words are only constituted by letters of the lexic 
            max = score(word)
            solution = word
    return (solution,max)


#the result here is ('jacasser', 17)


#I don't truly understand if we have the authorization to use the same letter more than once in one word
#Here an alternative of high score providing the use of the same letter more than once

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

#highestscore = high_score(['a', 'r', 'b', 'g', 'e', 's', 'c', 'j'],available_words)
#print((highestscore))

#the result here is ('jaser', 12)



#Exercice 4 

def joker(tirage,words): 
    bestscore = 0
    tirage.remove('?')
    for letter in alphabet:
        letters = list(tirage)
        letters.append(letter) #we have to try all the letter 
        print(letters)
        word,score = high_score(letters,words)
        if score >bestscore: #comparing the results between all the letters 
            solution = word
            bestscore = score
    return (solution, bestscore)

#jokerword = joker(['x', 'z', 'c', 'v', 'r', 'r', 't','?'],available_words)
#print(jokerword)

#return ('czar',15) like in the exercice