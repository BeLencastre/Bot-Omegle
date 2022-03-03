from time import sleep
from datetime import datetime, timedelta
from pyautogui import click, press, hotkey
from PIL import ImageGrab
from pyperclip import copy

# Put which and as many texts as you want
text1 = "Heeyy, how're u doing??"
text2 = "I'm Bernardo and I'm a developer looking for a job or freela"
text3 = "If you need a programmer, just text me"
text4 = "linkedin.com/in/bernardo-lencastre-8a4a7020a"
text5 = "IG  @be.python // @be.lencastre"
text6 = "Btw, that's my bot and it'll skip u, so, byebye"

# Minimizes the app, open Omegle (already on the chat screen) and determines the time the script will quit
def start_script():
    click(515, 750, interval=0.3)
    press('esc', interval=0.3)
    global stop_time
    stop_time = datetime.now() + timedelta(minutes=50)

# Copy the message from here and paste in the chat
def send_msg():
    click(250,673, interval=0.1)
    copy(text1)
    hotkey('ctrl', 'v')
    press('enter')
    copy(text2)
    hotkey('ctrl', 'v')
    press('enter', interval=0.1)
    copy(text3)
    hotkey('ctrl', 'v')
    press('enter', interval=0.1)
    copy(text4)
    hotkey('ctrl', 'v')
    press('enter', interval=0.1)
    copy(text5)
    hotkey('ctrl', 'v')
    press('enter', interval=0.5)
    copy(text6)
    hotkey('ctrl', 'v')
    press('enter', interval=0.1)

# Take a screenshot
def capture_screen():
    image = ImageGrab.grab()
    return image

# Detects if the person has already joined the chat
def detect_person(arg):
    sleep(1)
    for x in range(648, 657):
        for y in range(230, 236):
            send_button = arg.getpixel((x, y))

            if send_button == (255, 255, 255):
                return True

# Detects if the person has skiped you or it skips the person after the given time
def skip_person(arg):
    for x in range(140, 146):
        for y in range(680, 687):
            skip_button = arg.getpixel((x, y))

            if skip_button != (255, 255, 255):
                press('esc')
                return True
            sleep(0.04)

    for c in range(3):
        press('esc')
        sleep(0.3)
    return True

# Calculates the time to interrupt the script
def calculate_time(arg):
    if arg >= stop_time:
        return True
    return False

# Everything working together
start_script()
while True:
    while True:
        screen = capture_screen()
        if detect_person(screen):
            break
    send_msg()
    while True:
        screen = capture_screen()
        if skip_person(screen):
            break
    if calculate_time(datetime.now()):
        quit()
