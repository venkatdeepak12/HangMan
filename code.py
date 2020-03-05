import random
def getword():
    words=['beautiful','meaningful','gentle','possessive','generous','relation','photography','image','ban','eyes','spoon','bent','oven','lean','interest','blue-eyed','shelter','delight','machine','time','word','talent','righteous','lamentable','lovable','kind','honesty']
    return random.choice(words).upper()
import time
name = input("Enter your NICK n@me : ")
game=1
w=0
f=0
games=0
while game==1:
    games+=1
    print(" <<....HELLO....>> " + name, "Get ready....!")
    time.sleep(1)
    print(" ...START... ")
    time.sleep(0.5)
    word =getword()
    guesses = ''
    turns = 10
    while turns > 0:         
        failed = 0             
        for char in word:      
            if char in guesses:    
                print(char,end=" ")    
            else:
                print ("*",end=" ")    
                failed += 1    
        if failed == 0:
            w+=1
            print ("Yayy...! YOU NAILED IT....... :)")
            break              
        guess = input("Guess an alphabet : ")
        guess=guess.upper()
        guesses += guess                    
        if guess not in word:  
     
         
            turns -= 1        
     
        
            print ("WRONG")    
     
        
            print("You got still ", + turns, ' turns ') 
     
        
            if turns == 0:           
        
                f+=1
                print("You didn't make it...... :( ")
                print("The Word is ",word)
    game1=input("Wanna try again...... Type  YES or NO ")
    game1=game1.upper()
    if game1=='YES':
        game=1
    else:
        game=0
print("-----------GAME SUMMARY--------------") 
print()
print(".......Total No of games played : ",games)
print(".......Total No of games you won : ",w)
print(".......Total No of games you lose : ",f) 



