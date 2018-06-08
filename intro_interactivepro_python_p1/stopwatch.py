# template for "Stopwatch: The Game"
import simplegui
# define global variables
count = 0
sec = 0
stops = 0
perfect_stops = 0
is_stopped = True
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(count):
    sec = count/100.0
    min = int(sec/60)

    if sec%60 < 10:
        sec_a = "0"+str(sec%60)
        return str(min)+":"+str(sec_a)[:-1]
    elif sec >= 10:
        return str(min)+":"+str(sec%60)[:-1]
    else:
        return "Error"

# define event handlers for buttons; "Start", "Stop", "Reset"
def tick():

    global count

    count += 1
    sec = count/100
    print sec


def start():
    global is_stopped

    is_stopped = False
    timer.start()

def stop():
    global stops
    global perfect_stops
    global is_stopped


    if count%10 == 0 and is_stopped == False:
        is_stopped = True
        perfect_stops += 1
        stops += 1
        timer.stop()
    elif is_stopped == False:
        is_stopped = True
        stops += 1
        timer.stop()
    else:
        print "Watch already stopped"


def reset():
    global count, canvas, stops, perfect_stops
    timer.stop()
    count = 0
    stops = 0
    perfect_stops = 0





# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(10, tick)


#define draw handler
def draw(canvas):


    format_count = format(count)
    canvas.draw_text(str(format_count),[10,100],60, "red")

    canvas.draw_text(str(perfect_stops),[300,50],40, "red")
    canvas.draw_text("/",[330,50],40, "red")
    canvas.draw_text(str(stops),[350,50],40, "red")


# create frame
frame = simplegui.create_frame("Stopwatch: mini project", 400, 200)
frame.set_draw_handler(draw)
button1 = frame.add_button('Start', start)
button1 = frame.add_button('Stop', stop)
button1 = frame.add_button('Reset', reset)
# register event handlers


# start frame
frame.start()

# Please remembeasdfssfffddfr to asdasdasda grading rubric
