from pynput.keyboard import Key, Listener
from codingame import CustomCodinGameClient
from dotenv import load_dotenv
import os
import time


# Load environment variables from .env file
load_dotenv()

# Access environment variables
ID = os.environ.get('ID')
COOKIE = os.environ.get('COOKIE')


# Initialize the Client
client = CustomCodinGameClient(ID, COOKIE)

# Handle the key press
## When the key is pressed
def on_press(key):
    print('{0} pressed'.format(key))

## When the key is released
def on_release(key):
    print('{0} release'.format(key))
    if str(key) == "Key.shift_r": # Execute the code when clicked on RShift
        print("Executing the code.")
        client.exec()
    if str(key) == "Key.ctrl_r": # Execute the code when clicked on RShift
        print("Executing the code. [FORCED]")
        client.exec(force=True)
    if str(key) == "Key.f4":
        return False


## Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()