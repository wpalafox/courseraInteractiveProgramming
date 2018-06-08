# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

#Pad Globals
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 38
paddle2_vel = 38

LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [1,1] # pixels per update (1/60 seconds)

# Score for Player 1 and Player 2
score1 = 0
score2 = 0

#button function
def reset():
    global score1, score2
    score1 = 0
    score2 = 0

    left_or_right = ['left','right']
    CHOICE = random.choice(left_or_right)
    spawn_ball(CHOICE)

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists

    #Ball velocity
    if direction == 'left':
        LEFT = True
        RIGHT = False
        #print CHOICE
        ball_vel = [-(random.randrange(2,4)),-(random.randrange(1,3))]

    elif direction == 'right':
        RIGHT = True
        LEFT = False

        ball_vel = [(random.randrange(2,4)),-(random.randrange(1,3))]


    ball_pos = [WIDTH/2, HEIGHT/2]
    #ball_vel = [0,-1] # pixels per update (1/60 seconds)

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    #draw score
    canvas.draw_text(str(score1), [250, 50], 50, "Red")
    canvas.draw_text(str(score2), [300, 50], 50, "Green")

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]



    #paddle1_pos-HALF_PAD_HEIGHT<=ball_pos[1]<=paddle1_pos+HALF_PAD_HEIGHT




    # collide and reflect off top and bottom of canvas

    if ball_pos[1]+PAD_WIDTH <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT-BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # collide and reflect off left and right paddles

    if ball_pos[0]-BALL_RADIUS <= PAD_WIDTH and paddle1_pos-HALF_PAD_HEIGHT<=ball_pos[1]<=paddle1_pos+HALF_PAD_HEIGHT:
        ball_vel[0] = - (ball_vel[0]*1.1)
    elif ball_pos[0]+BALL_RADIUS >= WIDTH - PAD_WIDTH and paddle2_pos-HALF_PAD_HEIGHT<=ball_pos[1]<=paddle2_pos+HALF_PAD_HEIGHT:
        ball_vel[0] = - (ball_vel[0]*1.1)
    #collide and reflect off left and right CANVAS
    elif ball_pos[0] <= BALL_RADIUS:
        spawn_ball('right')
        score2+=1
    elif ball_pos[0] >= WIDTH-BALL_RADIUS-PAD_WIDTH:
        spawn_ball('left')
        score1+=1





    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Green", "White")


    # update paddle's vertical position, keep paddle on the screen



    # draw paddles
    canvas.draw_polygon([(0,paddle1_pos-HALF_PAD_HEIGHT),(PAD_WIDTH, paddle1_pos-HALF_PAD_HEIGHT),
                         (PAD_WIDTH, paddle1_pos+ HALF_PAD_HEIGHT), (0, paddle1_pos+HALF_PAD_HEIGHT)], 10, 'red', 'red')

    canvas.draw_polygon([(WIDTH, paddle2_pos-HALF_PAD_HEIGHT), (WIDTH-PAD_WIDTH, paddle2_pos-HALF_PAD_HEIGHT),(WIDTH, paddle2_pos+HALF_PAD_HEIGHT),(WIDTH-PAD_WIDTH, paddle2_pos+HALF_PAD_HEIGHT)], 10, 'green', 'green')

    # determine whether paddle and ball collide

    # draw scores

def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if paddle1_pos+80<=400:
        if key == simplegui.KEY_MAP["s"]:
            paddle1_pos += paddle1_vel
    if paddle2_pos-80>=0:
        if key == simplegui.KEY_MAP["up"]:
            paddle2_pos -= paddle2_vel


def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if paddle1_pos-80>=0:
        if key == simplegui.KEY_MAP["w"]:
            paddle1_pos -= paddle1_vel
    if paddle2_pos+80<=400:
        if key == simplegui.KEY_MAP["down"]:
            paddle2_pos += paddle2_vel

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', reset)
#spawn_ball(LEFT)
# start frame
new_game()
frame.start()
