# implementation of card game - Memory

import simplegui
import random

#Global Variables
m1 = [] 
m2 = []
state=0
card1=0
card2=0
turn_count=0 

for n in range(1,9):
    m1.append(n)
    m2.append(n) 

merged_list = m1+m2 
print merged_list 
exposed = []

for i in range(len(merged_list)):
    exposed.append(False)	




#Can't print the method random.shuffle. 
random.shuffle(merged_list)
print merged_list

# helper function to initialize globals
def new_game():
    global exposed, merged_list, turn_count 
    for i in range(len(merged_list)):
        exposed.insert(i, False)	
    turn_count=0 
    label1 = label.set_text("Turns: "+str(turn_count))
# define event handlers
def mouseclick(pos):
    global exposed, state, card1, card2, merged_list, turn_count  
    
    #computes the card index 
    x = pos[0]//50 
   
    #game logic
    if state==0 and exposed[x] == False:
        exposed[x]=True
        card1=x
        state=1
        print "state: "+str(state)
    elif state==1 and exposed[x] == False:
        exposed[x]=True
        card2=x
        state=2 
        turn_count=turn_count+1 
        print str(turn_count) 
    elif state==2:
        if merged_list[card1] != merged_list[card2]:
            exposed[card1]=False
            exposed[card2]=False
            print "card 1 is "+str(card1)+" and card 2 is "+str(card2) 
            exposed[x]=True
            card1=x
            state=1
            print "state is "+str(state)
        elif merged_list[card1] == merged_list[card2]:
            exposed[x]=True
            card1=x
            state=1
            print "state is "+str(state)
        
    label1 = label.set_text("Turns: "+str(turn_count))       
        
    
                   

            
            

            
            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(merged_list)):
        if exposed[i] == True:   
            canvas.draw_text(str(merged_list[i]), (50*i+15, 60), 35, "White")
            
        elif exposed[i] == False:
            canvas.draw_polygon(([i*50, 0], [i*50,100],[(i+1)*50,100], [(i+1)*50, 0]), 1, 'black', 'green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = ")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric