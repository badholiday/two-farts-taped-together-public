import sys, time, random

##player traits
player_name = ""
player_is_male = False
player_is_white = False
player_recognizes = False

##game over states
game_over = "GAME OVER"
follow_prompt = "Follow the prompt!"

##functions
typing_speed = 130 #wpm

def slow_type(t):
    print(t)
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ("")


##the game
def choose_your_own_adventure():
    introduction()


def introduction():
    global player_name
    global player_is_male
    global player_is_white

    slow_type("Welcome to Bryan's Choose Your Own Adventure adventure! My name is Bryan and I will be your guide. You play the game by typing out the options spelled in the CAPITAL letters. Make sure you type it correctly! Before we begin, let me ask you a few questions. ")
    
    player_name = input("First: what is your name?\n:")
    player_is_male = input("Second: are you MALE or FEMALE?\n:")
    player_is_white = input("And third: are you white? YES or NO?\n:")

    if player_is_male.upper() == 'MALE':
        player_is_male = True
    elif player_is_male.upper() == 'FEMALE':
        player_is_male = False
    else:
        slow_type(follow_prompt)
        #restart or
        quit() 
    
    if player_is_white.upper() == 'YES':
        player_is_white = True
    elif player_is_white.upper() == 'NO':
        player_is_white = False
    else:
        slow_type(follow_prompt)
        quit()
    beat1()

### ACT I
####
#### beat1

def beat1():
    global player_name
    global player_is_male
    global player_is_white
    global player_recognizes
    
    slow_type(f"Hello {player_name}, it's nice to meet you. Let's begin!")
    ###this story beat_option sucks!! change it. Everyone knows Rosy D
    slow_type("You wake up in the middle of a field with no recollection of who you are or how you got there. As you stand up you notice the big fat dead lady that was lying next to you! Do you recognize her?")
    beat1_options = input("YES or NO?\n:") 
    if beat1_options.upper() == 'YES':
        player_recognizes = True
        beat2()
    elif beat1_options.upper() == 'NO':
        player_recognizes = False
        beat2()
    else:
        slow_type("follow the prompt!")
        quit()

###
### beat2

def beat2():
    global player_is_white
    global player_recognizes
    global beat2_options
    
    if player_recognizes:
        slow_type("You are pretty sure that the dead lady is America's favorite racist, Rosy O'Donnell! As you stand there pondering how you could have possibly landed yourself in this situation, you hear police sirens quickly approaching.")
    elif not player_recognizes:
        slow_type("Although there is a faint sense of recognition, you ultimately have no idea who this dead elephant-sized person is... As you stand there pondering how you could have possibly landed yourself in this situation, you hear police sirens quickly approaching!")
    
    beat2_options = input("Do you RUN or STAY?\n:")
    if beat2_options.upper() == 'RUN':
        beat3a()
    elif beat2_options.upper() == 'STAY' and player_is_white:
        beat3b()
    elif beat2_options.upper() == 'STAY' and not player_is_white:
        beat3c() #game over
    else:
        slow_type(follow_prompt)
    
###
### beat3

def beat3a(): #RUN from beat2
    global player_is_white
    global player_recognizes

    slow_type("You sprint off into the forest towards home as fast as you can. As you run, some of your memories return: first you remember that you are a member of the white supremecist group Kavalry, and second you remember that you are Rosy O'Donnell's bodyguard. Then you have a series of flashbacks: you remember walking with Rosy O'Donnell and then blinding light and then you have a brief vision of her Rosy's face as you are choking her to death. The bits and pieces that you remember confuse the hell out of you and you ponder them until you get home. When you get near the house, you notice a police cruiser parked down the block.")
    

    beat3a_options = input("Do you want to go INSIDE the house or stay OUTSIDE?\n:")
    if beat3a_options.upper() == 'INSIDE':
        beat4a()
    elif beat3a_options.upper() == 'OUTSIDE':
        beat4b()
    else:
        print(follow_prompt)
        quit()

def beat3b(): #STAY and player_is_white from beat2
    slow_type("The police come charging onto the scene with their weapons raised and you hear someone yell: OPEN FIRE! You defensively raise your hand to your forehead, cover your eyes, and brace yourself for the gun shots... but they never come. You open your eyes to see that the two police officers have lowered their weapons and have raised the sign of the cyclops to their foreheads, just like you. One of the officers says: you know the sign, are you Kavalry?")

    beat3c_options = input("say YES or NO?\n:")
    if beat3c_options.upper() == 'YES':
        beat4c()
    if beat3c_options.upper() == 'NO':
        beat4d()
    else:
        print(follow_prompt)
        quit()
    
def beat3c(): #STAY and not player_is_white from beat2
    slow_type("The police arrive and you are suddenly very concious that you are a non-white person with bloody hands standing next to a dead white lady... Before you can say: don't shoot, I'm innocent! The police shoot you one hundred and sixty nine times.")
    slow_type(game_over)
    quit()

###
### beat4

def beat4a(): #INSIDE from beat3a
    slow_type("You walk right up to the front door, unlock it, and step inside. You close the dooor, stand in the foyer, listening for activity. You hear nothing, so you step into the kitchen. You look down and start as you notice a machine gun sitting on the counter. You pick  up the gun, and are examining it when you hear the toilet flush. The bathroom door opens and a man wearing a black suit steps out. He raises his arms in suprise and you aim the machine gun at him.")
    
    beat4a_options = input("Do you SHOOT the man or SPARE him?\n:")
    if beat4a_options.upper() == 'SHOOT':
        beat5a()
    if beat4a_options.upper() == 'SPARE':
        beat5b()
    else:
        print(follow_prompt)
        quit()


def beat4b(): #OUTSIDE from beat3a
    slow_type("You decide you don't want to go inside just yet, you want to make sure it's safe first. You walk around the house, looking for any suspicious activity while trying not to draw any suspicion, yourself. You peer through windows of the house looking for signs of activity, you also look up and down the street and you look through the windows of the cars near by. After two sweeps, you can see nothing suspicious.")
    
    beat4a()


def beat4c(): #YES from beat3b
    slow_type(f"You tell them that you are a member of Kavalry and they step closer. The Kavalry officer stands where he can see your face in the light and says: oh shit, {player_name}, I couldn't tell that was you in the dark!")
    
    beat5c() 
    

def beat4d(): #NO from beat3b
    slow_type(f"You tell the officers that you are not Kavalry and they step closer. The Kavalry officer stands where he can see your face in the light and says: you're a real crack up, {player_name}, you've been a member for years!")
    
    beat5c()

###
### beat5

def beat5a(): #SHOOT from beat4a
    slow_type("Before the strange man can say a word, you pull the trigger. You brace yourself for the recoil but none comes. The machine gun just clicks. Realizing you were about to kill him, he looks at you in suprise as he pulls a pistol out and shoots you right in the fucking head.")
    print(game_over)
    quit()


def beat5b(): #SPARE from beat4a
    global player_is_male
    
    slow_type(f"You keep the machine gun pointed at the man and demand: who are you and what are you doing here. The strange man keeps his arms raised and says: whoa there, {player_name} dont shoot, just listen to me, I think you've been hypnotized, you look like you've been hypnotized. The man says: {player_name}, you are a member of Kavalry but have secretly defected to the Black Panthers. You have been feeding us inside information for months, but I think you've been found out and framed for murder!")

def beat5c(): #ANY from beat4c AND beat4d
    slow_type("Upon hearing your name, some of your memories return: first you remember that you are indeed a member of the white supremecist group Kavalry, and second you remember that you are Rosy O'Donnell's bodyguard. Then you have a series of flashbacks: you remember walking with Rosy O'Donnell and then blinding light and then you have a brief vision of her Rosy's face as you are choking her to death. You snap out of your reverie and shake your head to clear it. The Kavalry officer asks: do you know who killed her?")
    beat5c_options = input("Do you say that you DO or DONT?\n:")
    if beat5c_options.upper() == 'DO':
        beat6X()
    if beat5c_options.upper() == 'DONT':
        beat6X()


### ACT II
###
### beat6

#def beat6X(): #DO from beat5c()

#def beat6X(): #DONT from beat5c()


choose_your_own_adventure()

    



