# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")

# initialize some useful global variables
player_turn = False
outcome = "Your Move - Hit or Stand?"
score = 0
deck = []
player_hand = []
dealer_hand = []
message = "New Deal?"

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
        self.cards = []

    def __str__(self):
        if not self.cards:
            return "Hand Contains"
        return "Hand contains " + " ".join(str(card) for card in self.cards)

    def add_card(self, card):
        self.cards.append(card)


    def get_value(self):
        sum = 0
        if not self.cards:
            return sum

        for card in self.cards:
            sum += VALUES[card.get_rank()]

        if "A" not in [self.cards[i].get_rank() for i in range(len(self.cards))]:
            return sum
        else:
            if sum + 10 <= 21:
                return sum + 10
            else:
                return sum

    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas, pos)
            pos[0] += 20


# define deck class
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]


    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __str__(self):
        return "Deck contains " + " ".join(str(card) for card in self.cards)



# define event handlers for buttons
def deal():
    global outcome, player_turn, deck, player_hand, dealer_hand, message, score
    outcome = "Your Move - Hit or Stand?"

    if player_turn:
        outcome = "Player Forfeits Hand"

        if score > 0:
            score -= 1
        player_hand = False

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())

    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())


    print "Player " + str(player_hand)
    print "Dealer " + str(dealer_hand)

    player_turn = True
    message = ""


def hit():
    global player_hand, deck, outcome, player_turn, score, message

    if not player_turn:
        return

    if player_hand.get_value() <= 21:
        player_hand.add_card(deck.deal_card())

    if player_hand.get_value() > 21:
        outcome = "You have busted!"
        if score > 0:
            score -= 1
        player_turn = False


        message = "New Deal?"


def stand():
    global dealer_hand, deck, player_turn, score, outcome, message

    if not player_turn:
        return

    player_turn = False

    while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())


    if dealer_hand.get_value() > 21:
        outcome = "Dealer busted! You win!"
        score += 1
        message = "New Deal?"


    else:
        if player_hand.get_value() <= dealer_hand.get_value():
            outcome = "Dealer Wins!"
            if score > 0:
                score -= 1

            message = "New Deal?"


        else:
            outcome = "Player Wins!"
            score += 1
            message = "New Deal?"


# draw handler
def draw(canvas):
    global player_hand, dealer_hand, outcome, score, player_turn

    dealer_hand.draw(canvas, [150, 250])
    player_hand.draw(canvas, [360, 250])
    canvas.draw_polygon([(105,1), (105,50), (500, 50), (500,1)], 2, 'Black', 'White')
    canvas.draw_text("Welcome to Blackjack!", (130,30), 35, 'Black')
    canvas.draw_polygon([(100, 500), (100, 540), (510, 540), (510, 500)], 2, 'Black', 'White')
    canvas.draw_text("Dealer Hand", (110, 200), 30, 'White')
    canvas.draw_text("Player Hand", (350, 200), 30, 'White')
    canvas.draw_text(outcome, (110,530), 35, 'Red')
    canvas.draw_text(message, (230,580), 30, 'White')
    canvas.draw_text("Score This Round = " + str(score), (180, 110), 25, 'Black')

    if player_turn:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (206,300), (71,96))

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