# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
result="what"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
        
class Hand:
    def __init__(self):
        self.handlist=[]	# create Hand object

    def __str__(self):
        ans = ""
        for i in range(len(self.handlist)):
            ans += str(self.handlist[i])
        return ans# return a string representation of a hand

    def add_card(self, card):
        self.handlist.append(card)	# add a card object to a hand

    def get_value(self):
        global sum
        sum=0
        for i in self.handlist:
            sum+=VALUES[i.rank]
        for i in self.handlist:
            if i.rank == 'A':
                if sum+10<=21:
                    sum+=10 #count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        return sum# compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
            #global idx
            idx=0
            for i in self.handlist:
                card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(i.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(i.suit))
                canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0]+idx*72+ CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                idx+=1 # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.decklist=[]
        for s_idx in SUITS:
            for r_idx in RANKS:
                self.decklist.append(Card(s_idx,r_idx))# create a Deck object

    def shuffle(self):
        random.shuffle(self.decklist)
        # shuffle the deck 
            # use random.shuffle()

    def deal_card(self):
        return self.decklist.pop()	# deal a card object from the deck
    
    def __str__(self):
        ans = ""
        for i in range(len(self.decklist)):
            ans += str(self.decklist[i])
        return ans	# return a string representing the deck

#define event handlers for buttons
def deal():
    global outcome, in_play,deck,player,dealer,result,score
    if in_play==True:
        score-=1
    result=""
    deck=Deck()
    deck.shuffle()
    player=Hand()
    dealer=Hand()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    outcome="Hit or Stand?"
    in_play = True
     

def hit():
    global outcome,result,score,in_play
    if in_play:
        if player.get_value() <21 :
            player.add_card(deck.deal_card())
            if player.get_value() ==21:
                result="You wins!You lucky bastard!"
                outcome="New Deal?"
                in_play=False
                score+=1
            elif player.get_value() > 21:
            
                in_play=False
                result= 'You have busted and you lose it loser'  # replace with your code below
                outcome='New Deal?'
                score-=1
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome,result,score,in_play
    if in_play:
        
        while dealer.get_value() <17 :
            dealer.add_card(deck.deal_card())
        # replace with your code below
        if dealer.get_value() >21 :
            result= "Dealer has busted and you wins"
            score+=1
        else:
            if player.get_value()<=dealer.get_value():
                result= "Dealer wins"
                score-=1
                in_play=False
                outcome='New Deal?'
            else:
                result= "Player wins"
                score+=1
                in_play=False
                outcome='New Deal?'
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    #global player
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Blackjack',(100,50),32,'blue')
    canvas.draw_text('Dealer',(80,180),32,'pink')
    canvas.draw_text('Player',(80,380),32,'pink')
    canvas.draw_text(outcome,(400,380),20,'black')
    canvas.draw_text(result,(300,150),20,'black')
    canvas.draw_text('score='+str(score),(500,100),20,'black')

    player.draw(canvas,[100,400])
    dealer.draw(canvas,[100,200])
    if in_play==True:
        card_loc = (CARD_BACK_CENTER[0], 
                    CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [100 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric