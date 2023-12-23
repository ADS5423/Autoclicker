
import time, random, threading, pynput
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
TOGGLE_KEY = KeyCode(char='r')
activated = False

def no_work():
    print("Why you see this?")

def on_press(key):
    global activated
    if key == TOGGLE_KEY:
        print("OFF")
        activated = not activated
        
def doClick():
    global activated
    while True:
        if activated:
            print("On!")
            variations = random.choice([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])
            Controller().click(Button.left, variations)
            delay = random.uniform(0.05, 0.0709)
            print(delay)
            time.sleep(delay)
        else:
            print("Off!?")
            pass

print("working!")
threading.Thread(target = doClick).start()
listner = Listener(on_press=on_press)
listner.start()
input()
