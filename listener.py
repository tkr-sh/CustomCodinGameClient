from mitmproxy import http
from json import dumps, dump
from pynput.keyboard import Key, Listener
from codingame import CustomCodinGameClient
from dotenv import load_dotenv
import os
import pprint
import time

# Load environment variables from .env file
load_dotenv()

# Access environment variables
ID = os.environ.get('ID')
COOKIE = os.environ.get('COOKIE')


# Initialize the Client
client = CustomCodinGameClient(ID, COOKIE)



# Functions
## Handle the request
def response(flow: http.HTTPFlow) -> None:
    if flow.response:
        open("listener.log", "at").write(f'services/TestSession/startTestSession in {flow.request.url}\n')
        if "services/TestSession/startTestSession" in str(flow.request.url):
            client.store_clash_info(flow.response.json())
            open("listener.log", "at").write("Storing the data...\n")