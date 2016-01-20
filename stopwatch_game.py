# template for "Stopwatch: The Game"
import simplegui
# define global variables
interval=100
t=0
x=0
y=0
last_t=0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A=t / 600
    B=(t-A*600)/100
    C=(t-A*600-B*100)/10
    global D
    D=t % 10
    return str(A)+":"+str(B)+str(C)+"."+str(D) 
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_handler_1():
    timer.start()
def button_handler_2():
    global t,last_t
#print t,last_t
    if t-last_t !=0:
        global x,y
        y+=1
        if str(D)=='0':
            x+=1
    last_t=t
#print t,last_t
    timer.stop()
    
def button_handler_3():
    timer.stop()
    global t,x,y
    t=x=y=0

def timer_handler():
    global t
    t+=1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(t),(50,150),50,"green")
    canvas.draw_text(str(x)+"/"+str(y),(250,50),30,"red")
# create frame
frame=simplegui.create_frame("stopwatch",300,300)
timer=simplegui.create_timer(interval,timer_handler)
# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("start",button_handler_1)
frame.add_button("stop",button_handler_2)
frame.add_button("reset",button_handler_3)



# start frame
frame.start()

# Please remember to review the grading rubric

