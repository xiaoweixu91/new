# implementation of card game - Memory

import simplegui
import random
turn=0
# helper function to initialize globals
def new_game():
    global l,exposed,state,ti,t2,turn
    turn=0
    label.set_text('Turns='+str(turn))
    state=0
    l=[]
    l1=[]
    for i in range(8):
        l.append(i)
        l1.append(i)
    l.extend(l1)
    random.shuffle(l)
    exposed=[False,False,False,False,False,False,False,False, \
             False,False,False,False,False,False,False,False]
     
# define event handlers
def mouseclick(pos):
    global exposed,idx,state,t1,t2,turn
    if state==0:
        exposed[pos[0]//50]=True
        t1=pos[0]//50
        state=1
    elif state==1 and exposed[pos[0]//50]==False:
        exposed[pos[0]//50]=True
        t2=pos[0]//50
        state=2
    elif state==2 and exposed[pos[0]//50]==False:
        if not(l[t1]==l[t2]):
            exposed[t1]=False
            exposed[t2]=False
        exposed[pos[0]//50]=True
        t1=pos[0]//50
        turn+=1
        state=1
    label.set_text('Turns='+str(turn))

        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(l)):
        if exposed[i]:
            canvas.draw_text(str(l[i]),(20+i*50,60),25,'red')
        else:
            canvas.draw_polygon([[0+i*50,0],[50+i*50,0],[50+i*50,99],[0+i*50,99]],1,'brown','green')
        


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label=frame.add_label("Turns=0")
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric