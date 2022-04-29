import time
import random

#poker table color
app.background = rgb(53, 101, 77) 
Rect(0, 0, 400, 400, fill = None, border = 'gold')

#Card Symbols
app.urlH = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Heart_coraz%C3%B3n.svg/1200px-Heart_coraz%C3%B3n.svg.png"
app.urlS = 'https://cdn-icons-png.flaticon.com/512/44/44672.png'
app.urlD = 'https://cdn.iconscout.com/icon/free/png-256/diamond-suit-card-37936.png'
app.urlC = 'https://cdn2.iconfinder.com/data/icons/casino-gambling-and-card-games/120/1c-512.png'

#List of card symbols
symbol = [app.urlH, app.urlS, app.urlD, app.urlC]
#Image(random.choice(symbol), 170, 170, width = 20, height = 20)

#List of card values
value = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
v = Label('', 0,0, size = 20)

#colors of buttons
app.colors = ['gold', 'gray']

#hearts image
app.url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Heart_coraz%C3%B3n.svg/1200px-Heart_coraz%C3%B3n.svg.png"

#J card
J = Group(
    Rect(165, 140, 70, 100, fill = 'white', border = 'black', borderWidth = 1),
    Label("J", 177, 155, size = 25, fill = 'red'),
    Image(app.url, 170, 170, width = 20, height = 20)
    )
J.centerX = 195
J.centerY = 170
J.rotateAngle = -20

#spades image
app.url = 'https://cdn-icons-png.flaticon.com/512/44/44672.png'

#A card
A = Group(
    Rect(165, 140, 70, 100, fill = 'white', border = 'black', borderWidth = 1),
    Label("A", 177, 155, size = 25, fill = 'black'),
    Image(app.url, 170, 170, width = 20, height = 20),
    )
A.centerX = 215
A.centerY = 170
A.rotateAngle = 5

#Black Arc
arc = Arc(200, 230, 100, 300, 0, 180, fill='black',
    border=None, borderWidth=2, opacity=100, rotateAngle=270, dashes=False,
    visible=True)

#BlackJack title
title = Label("BlackJack", 200, 200, fill = 'gold', size = 75, font = 'grenze', bold = True)

#21
twentyone = Label("21", 335, 60, fill = 'gold', size = 80, font = 'cinzel', bold = True) 

#play button
playButt = Group(
    Rect(50, 300, 120, 50, fill = 'gold', border = 'black'),
    Label("PLAY", 110, 325, size = 40, font = 'grenze')
    )
    
#rules button    
rules = Group(
    Rect(230, 300, 120, 50, fill = 'gold', border = 'black'),
    Label("RULES", 290, 325, size = 40, font = 'grenze')
    )
    
#Home page Group    
home = Group(J, A, arc, title, playButt, rules, twentyone)
 
#Title    
r = Label("RULES", 200, 40, size = 40, font = 'grenze', fill = 'gold')

#Rectangle
h = Rect(25, 70, 350, 125, fill = None, border='black', borderWidth=4)

#Jack Card
card1 = Rect(0, 0, 50, 75, fill = 'white', border = 'black', borderWidth = 1)
card1.centerX = 80
card1.centerY = 120
s1 = Image(app.urlS, 70, 120, width = 20, height = 20)
j = Label('J', 80,100, size = 20)

#Queen Card
card2 = Rect(0, 0, 50, 75, fill = 'white', border = 'black', borderWidth = 1)
card2.centerX = 140
card2.centerY = 120
s2 = Image(app.urlS, 130, 120, width = 20, height = 20)
q = Label('Q', 140,100, size = 20)

#King Card
card3 = Rect(0, 0, 50, 75, fill = 'white', border = 'black', borderWidth = 1)
card3.centerX = 200
card3.centerY = 120
s3 = Image(app.urlS, 190, 120, width = 20, height = 20)
k = Label('K', 200,100, size = 20)

#10 point value
ten = Label('+10', 140,175, size = 20, fill = 'gold')

#A card
card4 = Rect(0, 0, 50, 75, fill = 'white', border = 'black', borderWidth = 1)
card4.centerX = 300
card4.centerY = 120
s4 = Image(app.urlS, 290, 120, width = 20, height = 20)
a = Label('A', 300,100, size = 20)
#1 - 11 point value
one = Label('+11', 300,175, size = 20, fill = 'gold')

#instructions
d1 = Label("*Cards 2 - 10 all have the same value as what is shown on the card*", 200, 215, size = 10, fill = 'gold')
d2 = Label(" - The goal is beat the dealer's hand without going over 21.", 200, 250, size = 15, fill = 'white')
d3 = Label(" - You will start with 2 cards and the dealer will have one    ", 200, 265, size = 15, fill = 'white')
d4 = Label(" face down and one face up.                                           ", 200, 280, size = 15, fill = 'white')
d5 = Label("   - If you go over 21 you bust and the dealer automatically    ", 200, 295, size = 15, fill = 'white')
d6 = Label(" wins!                                                                               ", 200, 310, size = 15, fill = 'white')

#homeButton
homeButt = Group(
        Rect(50, 300, 120, 50, fill = 'gold', border = 'black'),
        Label("HOME", 110, 325, size = 40, font = 'grenze')
        )
#homeButt.visible = False

#home button on the bottom
homeButt.visible = True
homeButt.centerX = 200
homeButt.centerY = 350

#rules page group
rulesPage = Group(r, h, card1, s1, j, card2, s2, q, card3, s3, k, ten, card4, s4, a, one, d1, d2, d3, d4, d5, d6, homeButt)
rulesPage.visible = False 

#Dealer Label
dealerL = Label("Dealer", 200, 30, size = 30, font = 'cinzel', fill = 'gold')

#Bets Label
betsL = Label("Bets", 50, 100, size = 25, font = 'cinzel', fill = 'gold')

#$1 Chip
oneChip = Circle(50, 150, 15, fill = 'gold', border = 'black')
oneL = Label("1", 50, 150, size = 20, font = 'cinzel', fill = 'black')

#$5 Chip
fiveChip = Circle(50, 200, 15, fill = 'gold', border = 'black')
fiveL = Label("5", 50, 200, size = 20, font = 'cinzel', fill = 'black')

#$10 Chip
tenChip = Circle(50, 250, 15, fill = 'gold', border = 'black')
tenL = Label("10", 50, 250, size = 20, font = 'cinzel', fill = 'black')

#Moves Label
movesL = Label("Moves", 340, 100, size = 25, font = 'cinzel', fill = 'gold')

#Deal Button
dealButt = Group(
    Rect(200, 300, 80, 30, fill = 'gold', border = 'black'),
    Label("DEAL", 240, 315, size = 15, font = 'cinzel', bold = True)
    )

dealButt.centerX = 340
dealButt.centerY = 150

#Show Button
showButt = Group(
    Rect(200, 300, 80, 30, fill = 'gold', border = 'black'),
    Label("SHOW", 240, 315, size = 15, font = 'cinzel', bold = True)
    )

showButt.centerX = 340
showButt.centerY = 200

#Start Button
startButt = Group(
    Rect(200, 300, 80, 30, fill = 'gold', border = 'black'),
    Label("START", 240, 315, size = 15, font = 'cinzel', bold = True)
    )

startButt.centerX = 200
startButt.centerY = 200

#Result Button
resultButt = Group(
    Rect(200, 300, 80, 30, fill = 'gold', border = 'black'),
    Label("RESULT", 240, 315, size = 15, font = 'cinzel', bold = True)
    )

resultButt.centerX = 340
resultButt.centerY = 250
resultButt.visible = False

#Player Label
playerL = Label("Player", 200, 340, size = 30, font = 'cinzel', fill = 'gold')
#Player Vault
personAmount = Label(10, 200, 370, size = 25, font = 'cinzel', fill = 'gold')

#Betting
betSquare = Rect(170, 280, 60, 40, fill = None, border = 'white')
betAmount = Label(0, 200, 300, size = 20, font = 'cinzel', fill = 'white')

#Play page group
play = Group(dealerL, betsL, oneChip, oneL, fiveChip, fiveL, tenChip, tenL, movesL, dealButt, showButt, startButt, resultButt, playerL, personAmount, betSquare, betAmount)
play.visible = False

switch = Circle(200, 200, 10, fill = rgb(53, 101, 77))
switch.visible = False

#total to compare to against 21 and the dealer
sum = 0

#--------PLAYER SECTION--------
#First card dealt when 'Start' is pressed ~ for player
cardP1 = Rect(0, 0, 50, 75, fill = 'white', border = 'black', borderWidth = 2, opacity=100)
cardP1.centerX = 100
cardP1.centerY = 235
p1 = Label('', 0,0, size = 20)
p1.centerX = 100
p1.centerY = 220
v1 = choice(value)
p1.value = v1
#assigning the value 10 to letter cards 
if(v1 == 'J' or v1 == 'Q' or v1 == 'K'):
    sum += 10
#assigning the value 11 to 'A' 
elif(v1 == 'A'):
    sum += 11
#keep the value that's not a letter card
else:
    sum += v1
#random symbol
p1I = Image(choice(symbol), 90, 240, width = 20, height = 20)
print(v1)
print(sum)

#Second card dealt when 'Start' is pressed ~ for player
cardP2 = Rect(0, 0, 50, 75, fill = 'white', border = 'black', borderWidth = 2)
cardP2.centerX = 155
cardP2.centerY = 235
p2 = Label('', 0,0, size = 20)
p2.centerX = 155
p2.centerY = 220
v2 = choice(value)
p2.value = v2
#assigning the value 10 to letter cards 
if(v2 == 'J' or v2 == 'Q' or v2 == 'K'):
    sum += 10
#assigning the value 11 to 'A' 
elif(v2 == 'A'):
    sum += 11
#keep the value that's not a letter card
else:
    sum += v2
print(v2)
print(sum)
#random symbol
p2I = Image(choice(symbol), 145, 240, width = 20, height = 20)


#------DEALER SECTION-------
#total to compare to against 21 and the dealer
total = 0

#First card dealt when 'Start' is pressed ~ for player
cardD1 = Rect(0, 0, 50, 75, fill = 'white', border = 'black', borderWidth = 2, opacity=100)
cardD1.centerX = 110
cardD1.centerY = 100
d1 = Label('', 0,0, size = 20)
d1.centerX = 110
d1.centerY = 85
vd1 = choice(value)
d1.value = vd1
#assigning the value 10 to letter cards 
if(vd1 == 'J' or vd1 == 'Q' or vd1 == 'K'):
    total += 10
#assigning the value 11 to 'A' 
elif(vd1 == 'A'):
    total += 11
#keep the value that's not a letter card
else:
    total += vd1
#random symbol
d1I = Image(choice(symbol), 100, 105, width = 20, height = 20)
print(vd1)
print(total)

#Second card dealt when 'Start' is pressed ~ for player
cardD2 = Rect(0, 0, 50, 75, fill = 'white', border = 'black', borderWidth = 2)
cardD2.centerX = 165
cardD2.centerY = 100
d2 = Label('', 0,0, size = 20)
d2.centerX = 165
d2.centerY = 85
vd2 = choice(value)
d2.value = vd2
#assigning the value 10 to letter cards 
if(vd2 == 'J' or vd2 == 'Q' or vd2 == 'K'):
    total += 10
#assigning the value 11 to 'A' 
elif(vd2 == 'A'):
    total += 11
#keep the value that's not a letter card
else:
    total += vd2
print(vd2)
print(total)
#random symbol
d2I = Image(choice(symbol), 155, 105, width = 20, height = 20)

#startGame group
startGame = Group(cardP1, p1, p1I, cardP2, p2, p2I, cardD1, d1, d1I, cardD2, d2, d2I)
startGame.visible = False

#back of the second dealer card
backD2 = Rect(0, 0, 50, 75, fill = 'black', border = 'gold', borderWidth = 2)
backD2.centerX = 165
backD2.centerY = 100
B = Label("B", 155, 85, size = 45, font = 'grenze', fill = 'gold')
J = Label("J", 175, 105, size = 45, font = 'grenze', fill = 'gold')

backCard = Group(backD2, B, J)
backCard.visible = False

#------PLAYER SECTION-------

#first time clicking deal
val = choice(value)
dealCard = Group(
    Rect(185, 198, 50, 75, fill = 'white', border = 'black', borderWidth = 2),
    Label(val, 210, 220, size = 20),
    Image(choice(symbol), 200, 240, width = 20, height = 20)
    )
dealCard.visible = False

#values adding to the sum
s = 0
if(val == 'J' or val == 'Q' or val == 'K'):
    s += 10
elif(val == 'A'):
    s += 11
else:
    s += val

print(val)
print(s)

#updates sum when called
def updateCount(x):
    return x + s

#second time clicking deal
val2 = choice(value)
dealCard2 = Group(
    Rect(240, 198, 50, 75, fill = 'white', border = 'black', borderWidth = 2),
    Label(val2, 265,220, size = 20),
    Image(choice(symbol), 255, 240, width = 20, height = 20),
    )
dealCard2.visible = False
#values adding to the sum
s2 = 0
if(val2 == 'J' or val2 == 'Q' or val2 == 'K'):
    s2 += 10
elif(val2 == 'A'):
    s2 += 11
else:
    s2 += val2
    
print(val2)
print(sum)

#updates sum when called
def updateCount2(y):
    return y + s2

#invisible conditions (alternate to global variables)
sumSwitch = Circle(50, 350, 10, fill = rgb(53, 101, 77))
sumSwitch.visible = False

#invisible conditions (alternate to global variables)
SS = Circle(50, 350, 10, fill = rgb(53, 101, 77))
SS.visible = False

#-------DEALER SECTION---------

#first time clicking deal
point = choice(value)
dealersCard = Group(
    Rect(195, 63, 50, 75, fill = 'white', border = 'black', borderWidth = 2),
    Label(point, 220, 85, size = 20),
    Image(choice(symbol), 210, 105, width = 20, height = 20)
    )
dealersCard.visible = False

#values adding to the sum
t = 0
if(point == 'J' or point == 'Q' or point == 'K'):
    t += 10
elif(val == 'A'):
    t += 11
else:
    t += point

print(point)
print(total)

#updates total when called
def updateDealCount(x, checker):
    statement = []
    #for loop to add sayings into the list
    for i in range(3):
        if(not "blackjack or bust?" in statement): #if the saying is already added it will not add it again
            statement.append("blackjack or bust?")
        elif(not "drum roll please!!" in statement):
            statement.append("drum roll please!!")
        elif(not "ready for the reveal!" in statement):
            statement.append("ready for the reveal!")
    #print label
    say = Label(choice(statement), 200, 170, size = 25, font = 'grenze', fill = 'white') 
    say.visible = False
    
    #checker is a boolean that turns True or False depending on the place it gets called
    if(checker == True):
        say.visible = True
         
    return x + t #returns t value and x from another method

#second time clicking deal
point2 = choice(value)
dealersCard2 = Group(
    Rect(200, 63, 50, 75, fill = 'white', border = 'black', borderWidth = 2),
    Label(point2, 265,85, size = 20),
    Image(choice(symbol), 255, 240, width = 20, height = 20),
    )
dealersCard2.visible = False
#values adding to the sum
t2 = 0
if(point2 == 'J' or point2 == 'Q' or point2 == 'K'):
    t2 += 10
elif(point2 == 'A'):
    t2 += 11
else:
    t2 += point2
    
print(point2)
print(total)

#updates total2 when called
def updateDealCount2(y, check): #same as updateDealCount except for the y value at t2
    statement = []
    
    for i in range(3):
        if(not "blackjack or bust?" in statement):
            statement.append("blackjack or bust?")
        elif(not "drum roll please!!" in statement):
            statement.append("drum roll please!!")
        elif(not "ready for the reveal!" in statement):
            statement.append("ready for the reveal!")
    
    say = Label(choice(statement), 200, 170, size = 25, font = 'grenze', fill = 'white')
    say.visible = False
    
    if(check == True):
        say.visible = True
         
    return y + t2


#winning screen
won = Group(
    Rect(105, 105, 205, 205, border = 'gold', borderWidth = 4),
    Label('BLACKJACK', 205, 175, size = 30, fill = 'gold', font = 'cinzel'),
    Label('YOU WIN!', 205, 225, size = 30, fill = 'gold', font = 'cinzel')
    )
won.visible = False
   
#bust screen
bustLabel = Group(
    Rect(10, 150, 360, 100, rotateAngle = -25),
    Label('BUST', 200, 200, size = 50, fill = 'gold', font = 'grenze', rotateAngle = -25),
    )
bustLabel.visible = False

#tie screen
tie = Group(
    Rect(10, 150, 360, 100),
    Label('TIE', 200, 200, size = 50, fill = 'red', font = 'grenze', rotateAngle = -25),
    )
tie.visible = False

#Users Controls    
def onMousePress(mouseX, mouseY):
    
    #calling sums upon mouse update
    sum2 = updateCount(0)
    print("sum2", sum2)
    sum3 = updateCount2(0)
    print("sum3", sum3)
    #calling totals upon mouse update
    total2 = updateDealCount(0, False)
    total3 = updateDealCount2(0, False)
    
    if(rules.hits(mouseX, mouseY) == True): #Rules button is hit go to Rules Page
        home.visible = False
        rulesPage.visible = True 
        play.visible = False
    
    if(homeButt.hits(mouseX, mouseY) == True): #Home button is hit go to Home Page
        rulesPage.visible = False
        home.visible = True  
        rulesPage.visible = False
    
    if(playButt.hits(mouseX, mouseY)): #Play button is hit go to Play Page
        home.visible = False
        rulesPage.visible = False
        rules.visible = False
        playButt.visible = False
        play.visible = True
        homeButt.visible = False
    
    if(oneChip.hits(mouseX, mouseY)): #Bet $1 only if allowed
        if(personAmount.value > 0):
            betAmount.value += 1
            personAmount.value -= 1
    
    if(fiveChip.hits(mouseX, mouseY)): #Bet $5 only if allowed
        if(personAmount.value > 4):
            betAmount.value += 5
            personAmount.value -= 5
    
    if(tenChip.hits(mouseX, mouseY)): #Bet $10 only if allowed
        if(personAmount.value > 9):
            betAmount.value += 10
            personAmount.value -= 10
    
    if(betAmount.value > 0):
        if(startButt.hits(mouseX, mouseY)): #Deals player & dealer
            startGame.visible = True #starts the game
            startButt.visible = False
            backCard.visible = True #TURN THIS BACK TO TRUE        

    if(startGame.visible == True): #when game starts
        #player cards
        if(dealButt.hits(mouseX, mouseY) and switch.visible == False): #first dealt card to player
            dealCard.visible = True
            sum2 = updateCount(sum)
            print(sum2)
            switch.visible = True
            sumSwitch.visible = True
        elif(dealButt.hits(mouseX, mouseY) and switch.visible == True): #second dealt card to player
            dealCard2.visible = True
            sum3 = updateCount2(sum)
            print(updateCount2(sum3))
            SS.visible = True
       
        #dealer cards
        if(showButt.hits(mouseX, mouseY)): #when show button is pressed
            backCard.visible = False #flips the card to the face side
            
            #conditions for dealer --> dealer deals cards to themselves until they hit 17
            if(total <= 17): #dealer's card less than or equal to 17 --> draw card
                dealersCard.visible = True 
                total2 = updateDealCount(total, True) #update total
                if(total + total2 <= 17): #dealer's cards less than or equal to 17 --> draw card
                    dealersCard2.visible = True
                    total3 = updateDealCount2(total2, True) #update total
            
            print("total", total)
            print("total2", total2)
            print("total3", total3)
            print("point2", point)
        
        #result of the game    
        if(resultButt.hits(mouseX, mouseY) and sumSwitch.visible == False and backCard.visible == False): #if no extra card is dealt
            
            #****Comments****
            #-
            #This section has a lot of repetitive arithmetic that changes very slightly
            #The bets calculation stays the same, so it's explained in the first section, but it applies to all 3
            #First Section: When no extra cards are dealt to the player
            #Second Section: When 1 extra card is dealt to the player
            #Third Section: When 2 extra cards are dealt to the player
            #-
            #****Comments End****    
            
#****F I R S T  S E C T I O N ****#            
            print("sum")
            if(dealersCard2.visible == False and dealersCard.visible == True): #dealer has a total of 3 cards
                if(total + total2 <= 21 and sum <= 21):  #dealer and player less than 21 
                    if(sum > total + total2): #win
                        won.visible = True
                        won.toFront()
                        personAmount.value += (betAmount.value*2) #multiply the bet by 2 and add it to the player's vault
                        print(sum, "d1")
                    if(sum < total + total2): #player is less than dealer --> lose
                        print("BUST")
                        bustLabel.visible = True
                        bustLabel.toFront()
                        #personAmount.value -= betAmount.value #subtract bet from player's amount
                        betAmount.value = 0 #set bet back to 0
                        print(sum, "e1")
                elif(sum > 21): #player is greater than 21 --> lose
                    print("BUST")
                    bustLabel.visible = True
                    bustLabel.toFront()
                    #personAmount.value -= betAmount.value #subtract bet from player's amount
                    betAmount.value = 0 #set bet back to 0
                    print(sum, "f1")
                elif(sum == total + total2): #player equals dealer --> tie
                    print("TIE")
                    tie.visible = True
                    tie.toFront()
                    personAmount.value = 10 #no change in the player's vault
                    betAmount.value = 0 #bet is back to 0
                else:  #no other condition is met --> win
                    won.visible = True
                    won.toFront()  
                    personAmount.value += (betAmount.value*2)
                    print(sum, "g1")
            
            elif(dealersCard.visible == False and dealersCard.visible == False): #dealer has a total of 2 cards
                if(total <= 21 and sum <= 21):  
                    if(sum > total): 
                        won.visible = True
                        won.toFront()
                        personAmount.value += (betAmount.value*2)
                        print(sum, "d2")
                    if(sum < total):
                        print("BUST")
                        bustLabel.visible = True
                        bustLabel.toFront()
                        #personAmount.value -= betAmount.value
                        betAmount.value = 0
                        print(sum, "e2")
                elif(sum > 21):
                    print("BUST")
                    bustLabel.visible = True
                    bustLabel.toFront()
                    #personAmount.value -= betAmount.value
                    betAmount.value = 0
                    print(sum, "f3") 
                elif(sum == total):
                    print("TIE")
                    tie.visible = True
                    tie.toFront()
                    personAmount.value = 10
                    betAmount.value = 0
                    print(sum + sum2, "if2")
                    print(total + total2, "if2")
                else:
                    won.visible = True
                    won.toFront()  
                    personAmount.value += (betAmount.value*2)
                    print(sum, "g2")
            else:                                                                #dealer has a total of 4 cards
                if(total + total2 + total3 <= 21):
                    if(sum > total + total2 + total3): 
                        won.visible = True
                        won.toFront() 
                        personAmount.value += (betAmount.value*2)
                        print(sum, "d3")
                    if(sum < total + total2 + total3):
                        print("BUST")
                        bustLabel.visible = True
                        bustLabel.toFront()
                        #personAmount.value -= betAmount.value
                        betAmount.value = 0
                        print(sum, "e3")
                elif(sum > 21):
                    print("BUST")
                    bustLabel.visible = True
                    bustLabel.toFront()
                    #personAmount.value -= betAmount.value
                    betAmount.value = 0
                    print(sum, "f3")  
                elif(sum == total + total2 + total3):
                    print("TIE")
                    tie.visible = True
                    tie.toFront()
                    personAmount.value = 10
                    betAmount.value = 0
                else:
                    won.visible = True
                    won.toFront()   
                    personAmount.value += (betAmount.value*2)
                    print(sum, "g3")

#**** S E C O N D  S E C T I O N ****#          
        elif(resultButt.hits(mouseX, mouseY) and sumSwitch.visible == True and SS.visible == False and backCard.visible == False): #if one extra card is dealt
            print("sum2")
            if(dealersCard2.visible == False and dealersCard.visible == True):
                if(total + total2 <= 21 and sum + sum2 <= 21):  
                    if(sum + sum2 > total + total2): 
                        won.visible = True
                        won.toFront()   
                        personAmount.value += (betAmount.value*2)
                        print(sum + sum2, "a1")
                    if(sum + sum2 < total + total2):
                        print("BUST")
                        bustLabel.visible = True
                        bustLabel.toFront()
                        #personAmount.value -= betAmount.value
                        betAmount.value = 0
                        print(sum + sum2, "b1")
                elif(sum + sum2 > 21):
                    print("BUST")
                    bustLabel.visible = True
                    bustLabel.toFront()
                    #personAmount.value -= betAmount.value
                    betAmount.value = 0
                    print(sum + sum2, "c1")
                elif(sum + sum2 == total + total2):
                    print("TIE")
                    tie.visible = True
                    tie.toFront()
                    personAmount.value = 10
                    betAmount.value = 0
                    print(sum + sum2, "e1")
                    print(total + total2, "e1")
                else:
                    won.visible = True
                    won.toFront() 
                    personAmount.value += (betAmount.value*2)
                    print(sum + sum2, "d1")
            elif(dealersCard.visible == False and dealersCard.visible == False):
                if(total <= 21 and sum + sum2 <= 21):  
                    if(sum + sum2 > total): 
                        won.visible = True
                        won.toFront()   
                        personAmount.value += (betAmount.value*2)
                        print(sum + sum2, "a2")
                    if(sum < total):
                        print("BUST")
                        bustLabel.visible = True
                        bustLabel.toFront()
                        #personAmount.value -= betAmount.value
                        betAmount.value = 0
                        print(sum + sum2, "b2")
                elif(sum + sum2 > 21):
                    print("BUST")
                    bustLabel.visible = True
                    bustLabel.toFront()
                    #personAmount.value -= betAmount.value
                    betAmount.value = 0
                    print(sum + sum2, "c2")
                elif(sum + sum2 == total):
                    print("TIE")
                    tie.visible = True
                    tie.toFront()
                    personAmount.value = 10
                    betAmount.value = 0
                    print(sum + sum2, "e2")
                    print(total + total2, "e2")
                else:
                    won.visible = True
                    won.toFront()  
                    personAmount.value += (betAmount.value*2)
                    print(sum + sum2, "d2")
            else:
                if(total + total2 + total3 <= 21):
                    if(sum + sum2 > total + total2 + total3): 
                        won.visible = True
                        won.toFront()   
                        personAmount.value += (betAmount.value*2)
                        print(sum + sum2, "a3")
                    if(sum + sum2 < total + total2 + total3):
                        print("BUST")
                        bustLabel.visible = True
                        bustLabel.toFront()
                        #personAmount.value -= betAmount.value
                        betAmount.value = 0
                        print(sum + sum2, "b3")
                elif(sum + sum2 > 21):
                    print("BUST")
                    bustLabel.visible = True
                    bustLabel.toFront()
                    #personAmount.value -= betAmount.value
                    betAmount.value = 0
                    print(sum + sum2, "c3")        
                elif(sum + sum2 == total + total2 + total3):
                    print("TIE")
                    tie.visible = True
                    tie.toFront()
                    personAmount.value = 10
                    betAmount.value = 0
                    print(sum + sum2, "e3")
                    print(total + total2, "e3")
                else:
                    won.visible = True
                    won.toFront()   
                    personAmount.value += (betAmount.value*2)
                    print(sum + sum2, "d3")

#**** T H I R D  S E C T I O N ***#            
        elif(resultButt.hits(mouseX, mouseY) and sumSwitch.visible == True and SS.visible == True and backCard.visible == False): #if two extra card is dealt
            print("sum2")
            if(dealersCard2.visible == False and dealersCard.visible == True):
                if(total + total2 <= 21 and sum + sum2 + sum3 <= 21):  
                    if(sum + sum2 + sum3 > total + total2): 
                        won.visible = True
                        won.toFront()   
                        personAmount.value += (betAmount.value*2)
                        print(sum + sum2 + sum3, "a1")
                    if(sum + sum2 + sum3< total + total2):
                        print("BUST")
                        bustLabel.visible = True
                        bustLabel.toFront()
                        #personAmount.value -= betAmount.value
                        betAmount.value = 0
                        print(sum + sum2 + sum3, "b1")
                elif(sum + sum2 + sum3 > 21):
                    print("BUST")
                    bustLabel.visible = True
                    bustLabel.toFront()
                    #personAmount.value -= betAmount.value
                    betAmount.value = 0
                    print(sum + sum2 + sum3, "c1")
                elif(sum + sum2 + sum3 == total + total2):
                    print("TIE")
                    tie.visible = True
                    tie.toFront()
                    personAmount.value = 10
                    betAmount.value = 0
                else:
                    won.visible = True
                    won.toFront()  
                    personAmount.value += (betAmount.value*2)
                    print(sum + sum2 + sum3, "d1")
            elif(dealersCard.visible == False and dealersCard.visible == False):
                if(total <= 21 and sum + sum2 + sum3 <= 21):  
                    if(sum + sum2 > total): 
                        won.visible = True
                        won.toFront()   
                        personAmount.value += (betAmount.value*2)
                        print(sum + sum2 + sum3, "a2")
                    if(sum + sum2 + sum3 < total):
                        print("BUST")
                        bustLabel.visible = True
                        bustLabel.toFront()
                        #personAmount.value -= betAmount.value
                        betAmount.value = 0
                        print(sum + sum2 + sum3, "b2")
                elif(sum + sum2 + sum3 > 21):
                    print("BUST")
                    bustLabel.visible = True
                    bustLabel.toFront()
                    #personAmount.value -= betAmount.value
                    betAmount.value = 0
                    print(sum + sum2 + sum3, "c2")
                elif(sum + sum2 + sum3 == total):
                    print("TIE")
                    tie.visible = True
                    tie.toFront()
                    personAmount.value = 10
                    betAmount.value = 0
                else:
                    won.visible = True
                    won.toFront() 
                    personAmount.value += (betAmount.value*2)
                    print(sum + sum2 + sum3, "d2")
            else:
                if(total + total2 + total3 <= 21):
                    if(sum + sum2 + sum3 > total + total2 + total3): 
                        won.visible = True
                        won.toFront()   
                        personAmount.value += (betAmount.value*2)
                        print(sum + sum2 + sum3, "a3")
                    if(sum + sum2 + sum3 < total + total2 + total3):
                        print("BUST")
                        bustLabel.visible = True
                        bustLabel.toFront()
                        #personAmount.value -= betAmount.value
                        betAmount.value = 0
                        print(sum + sum2 + sum3, "b3")
                elif(sum + sum2 + sum3 > 21):
                    print("BUST")
                    bustLabel.visible = True
                    bustLabel.toFront()
                    #personAmount.value -= betAmount.value
                    betAmount.value = 0
                    print(sum + sum2 + sum3, "c3")        
                elif(sum + sum2 + sum3 == total + total2 + total3):
                    print("TIE")
                    tie.visible = True
                    tie.toFront()
                    personAmount.value = 10
                    betAmount.value = 0
                else:
                    won.visible = True
                    won.toFront()   
                    personAmount.value += (betAmount.value*2)
                    print(sum + sum2 + sum3, "d3")
        