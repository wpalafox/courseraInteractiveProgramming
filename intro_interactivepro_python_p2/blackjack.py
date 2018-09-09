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
in_play = True
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
print "*--------------------------------------------------------*"

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
    
    def draw_reverse(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0]+CARD_BACK_CENTER[0], pos[1]+CARD_BACK_CENTER[1]], CARD_SIZE)

# Student should insert code for Hand class here
class Hand:
    def __init__(self):
        self.hand = [] 

    def __str__(self):
        if self.hand == []:
            return "Hand contains nothing" 
        elif self.hand != []:
            current_hand = [] 
            i=0
            while i < len(self.hand):
                current_hand.append((str(self.hand[i].get_suit()+self.hand[i].get_rank())))
                i+=1
            joined_hand=""
            
            for i in range(len(current_hand)):
                joined_hand= joined_hand+current_hand[i]+" "
            
            return "hand contains: "+joined_hand          

    
    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card) 
     
        
    def get_value(self):
        #determines the value of the hand
        #will Ace as 1 if an Ace already exists in hand
        #aces are worth 1 or 11
        state_value=0
        ace_present= False
        #cycles through the cards and extracts the rank
        for card in self.hand:
            rank = card.get_rank()
            state_value += VALUES[rank]
            if rank == 'A':
                ace_present = True
            if ace_present and state_value < 12:
                state_value += 10
        return state_value 
   
    def draw(self, canvas, pos):
        #pass #draw a hand on the canvas, use the draw method for cards    
        for card in self.hand:
            pos[0] = pos[0] + CARD_SIZE[0]+45
            card.draw(canvas, pos) 
            
        
# define deck class 
class Deck:
    def __init__(self):
        deck = []
        self.deck = deck
        
        for suit in SUITS:
            for rank in RANKS: 
                deck.append((Card(suit, rank)))
        
    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck) 

    def deal_card(self):
        # deal a card object from the deck
        # it's popping a string at the end
        return self.deck.pop()
    def __str__(self):
        if self.deck == []:
            return "Deck contains nothing"
        elif self.deck != []:
            current_deck=[]
            i=0
            while i < len(self.deck):
                current_deck.append(str(self.deck[i]))
                i += 1
            joined_deck=""
            
            for i in range(len(current_deck)):
                joined_deck = joined_deck+current_deck[i]+" "
            return "Deck contains: "+joined_deck



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, player_score
   
    # your code goes here
    #1. 
    #str(deck.shuffle)
    #1. Create a new player and dealer hands
    if in_play:
        #1. Create dealer and player hands
        player_hand = Hand() 
        dealer_hand = Hand()
        deck = Deck()
        outcome="Hit or Stand?"
        
        #2. Should shuffle the deck (stored as global)
        deck.shuffle() 
        
        #3. Add two cards to the dealer AND player hands
            #-to transfer a card from the deck to a hand
            #a. use deal_card method of the Deck class
            #b. use the add_card method of the Hand class
            #^in combination 
            #The resulting hands should be printed to the console
            #with an appropriate message 
    
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card()) 
        player_score=player_hand.get_value()
       
        print "Player's "+str(player_hand)
        print "Player's score: "+str(player_score)
    
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_score=dealer_hand.get_value()
        print "Dealer's "+str(dealer_hand)
        
        print "Dealer's score: "+str(dealer_score)
        print "*--------------------------------------------------------*"
        in_play = True 
    
    elif in_play == False:
        print "-------------------------------------------------"
        print "Not in play"
        outcome="New Game"
        in_play=True
        deal()
  
    

    
     
    

def hit():
    global score, in_play, deck, player_hand, outcome
    
    if in_play:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card()) 
            if player_hand.get_value()>21:
                print "Player's score "+str(player_hand.get_value()) 
                print "You have busted!"
                outcome="You have busted! New Deal?"
                in_play = False 
                score -= 1
                
    
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    global score, in_play, deck, dealer_hand, outcome
    if in_play:
        in_play=False 
        while dealer_hand.get_value() <= 17:
            dealer_hand.add_card(deck.deal_card())
            print "Dealer's "+str(dealer_hand)
        if dealer_hand.get_value()>21:
            print "Dealer Busts!"
            outcome="Dealer Bust! New Deal?"
            score+=1  
        elif dealer_hand.get_value()<=21:
            if player_hand.get_value() > dealer_hand.get_value():
                score += 1 
                print "Player wins!"
                outcome="Player wins! New Deal?"
            elif player_hand.get_value() < dealer_hand.get_value():
                score -= 1
                print "Dealer wins!" 
                outcome="Dealer wins! New Deal?"
            elif player_hand.get_value == dealer_hand.get_value():
                score -= 1
                print "Tie... Dealer wins!"
                outcome="Tie... Dealer wins! New Deal?"
        print "Dealer's score: "+str(dealer_hand.get_value())
    elif in_play and dealer_hand.get_value() >= 17:
        print "Dealer stands"
    elif in_play == False:
        "You have busted!"
        outcome="You have busted! New Deal?"
        
        
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global score, outcome
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    canvas.draw_text(outcome, (50, 100), 45, 'Red')
    canvas.draw_text("Blackjack", (200,50), 55, 'Black')
    canvas.draw_text("Dealer's Hand", (80, 180), 45, 'Black')
    dealer_hand.draw(canvas, [-35, 200]) 
    canvas.draw_text("Player's Hand", (80, 380), 45, 'Red')
    player_hand.draw(canvas, [-35, 400])
    
    canvas.draw_text(str(score), (450, 340), 75, 'White')
    if in_play:
        dealer_hand.hand[0].draw_reverse(canvas, [82,200])
    

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
