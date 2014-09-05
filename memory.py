# implementation of card game - Memory

import simplegui
import random

l1 = range(0, 8)
l2 = range(0, 8)

deck = l1 + l2
random.shuffle(deck)

exposed = [False, False, False, False, False,
           False, False, False, False, False,
           False, False, False, False, False,
           False]

state = 0
turns = 0
card_1 = 0
card_2 = 0

# helper function to initialize globals
def new_game():
    global deck, turns, state, card_1, card_2, exposed

    for card in range(len(exposed)):
        if exposed[card]:
            exposed[card] = False
    random.shuffle(deck)
    turns = 0
    label.set_text("Number of Turns = " + str(turns))
    state = 0



# define event handlers
def mouseclick(pos):
    global exposed, state, card_1, card_2, turns
    index = pos[0] // 50

    if exposed[index] == True:
        return

    elif state == 0:
        exposed[index] = True
        card_1 = index

        state = 1

    elif state == 1:
        exposed[index] = True
        card_2 = index

        state = 2

    else:
        if deck[card_1] == deck[card_2]:
            exposed[index] = True
            card_1 = index
            turns += 1
            label.set_text("Number of Turns = " + str(turns))

            state = 1

        else:
            exposed[card_1] = False
            exposed[card_2] = False
            exposed[index] = True
            card_1 = index
            turns += 1
            label.set_text("Number of Turns = " + str(turns))

            state = 1





# cards are logically 50x100 pixels in size
def draw(canvas):
    global deck
    global exposed

    for card in range(len(exposed)):

        if exposed[card]:
            pos = card*50
            canvas.draw_text(str(deck[card]), (pos + 10, 70), 70, 'White')
        elif exposed[card] == False:
            x = card*50
            canvas.draw_line((x + 25, 0), (x + 25, 100), 48, 'Green')

        #draw white lines separating cards
        l = card*50
        canvas.draw_line((l + 50, 0), (l + 50, 100), 2, 'White')

    #draw white border
    canvas.draw_polygon([(0,0), (0,100), (800, 100), (800,0)], 2, 'White')





# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Number of Turns = 0")



# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric