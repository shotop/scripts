# Implementation of classic arcade game Pong

import pygame
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = []
ball_vel = []

paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT]
paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT]

paddle1_vel = 0
paddle2_vel = 0

player1_score = 0
player2_score = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]

    if direction == RIGHT:
        ball_vel = [random.randrange(3, 5), -random.randrange(3, 5)]

    elif direction == LEFT:
        ball_vel = [- random.randrange(3, 5), -random.randrange(3, 5)]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global player1_score, player2_score# these are ints
    spawn_ball(RIGHT)
    player1_score = 0
    player2_score = 0




def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel, player1_score, player2_score


    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[1] <= BALL_RADIUS: #top
        ball_vel[1] = - ball_vel[1]

    elif ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS: #bottom
        ball_vel[1] = - ball_vel[1]

    elif ball_pos[0] - BALL_RADIUS <= PAD_WIDTH: #left

        if ball_pos[1] > paddle1_pos[1] and ball_pos[1] < paddle1_pos[1] + PAD_HEIGHT:
            ball_vel[0] = ball_vel[0] + ball_vel[0]*.10
            ball_vel[0] = - ball_vel[0]
        else:
            spawn_ball(RIGHT)
            player2_score += 1


    elif ball_pos[0] >= (WIDTH -1) - BALL_RADIUS: #right
        if ball_pos[1] > paddle2_pos[1] and ball_pos[1] < paddle2_pos[1] + PAD_HEIGHT:
            ball_vel[0] = ball_vel[0] + ball_vel[0]*.10
            ball_vel[0] = - ball_vel[0]
        else:
            spawn_ball(LEFT)
            player1_score += 1

    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] <= 1:
        paddle1_pos[1] = 1
    elif paddle1_pos[1] >= HEIGHT - PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - PAD_HEIGHT

    paddle1_pos[1] += paddle1_vel

    if paddle2_pos[1] <= 1:
        paddle2_pos[1] = 1
    elif paddle2_pos[1] >= HEIGHT - PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - PAD_HEIGHT

    paddle2_pos[1] += paddle2_vel

    # draw paddles


    c.draw_line(paddle1_pos, [paddle1_pos[0], paddle1_pos[1] + PAD_HEIGHT + paddle1_vel], 7, 'White')
    c.draw_line(paddle2_pos, [paddle2_pos[0], paddle2_pos[1] + PAD_HEIGHT + paddle2_vel], 7, 'White')


    # draw scores
    c.draw_text(str(player1_score), [150, 50], 60, "White")
    c.draw_text(str(player2_score), [430, 50], 60, "White")

    # draw center court
    c.draw_circle([WIDTH / 2, HEIGHT / 2], 50, 2, "White")

def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 7
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc



def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', new_game, 150)


# start frame
new_game()
frame.start()