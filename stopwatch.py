# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
stops = 0
precise_stops = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    minutes = time // 600
    tens_of_seconds = ((time // 10) % 60) // 10
    seconds = ((time // 10) % 60) % 10
    tenths_of_seconds = str(time)[-1]
    return str(minutes) + ":" + str(tens_of_seconds) + str(seconds) + "." + str(tenths_of_seconds)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global stops
    global precise_stops
    if timer.is_running() == False:
        return
    stops += 1
    timer.stop()
    if time % 10 == 0:
        precise_stops += 1
        
def reset():
    global time
    global stops
    global precise_stops
    timer.stop()
    time = 0
    stops = 0
    precise_stops = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw(canvas):
    global time
    canvas.draw_text(format(time), [115,200], 100, 'Yellow', 'sans-serif')
    canvas.draw_text(str(precise_stops) + "/" + str(stops), [400,50], 60, 'Blue', 'sans-serif')
    
# create frame
frame = simplegui.create_frame("StopWatch", 500, 400)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()
timer.stop()

