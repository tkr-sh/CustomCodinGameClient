from requests import get, post
from json import dumps, dump, load
from re import search
from os import system as exe, makedirs, getcwd
from webbrowser import open as wopen
from random import randint

# Custom client for CodinGame
class CustomCodinGameClient:
    # Variable that auth you
    ID=""
    COOKIE=""
    # Global variables of the clash
    public_handle = ""
    game_id = ""
    handle_code = ""
    statement = ""
    stub_generator = "read x:int s:string"
    test_cases_raw = [] # The raw tests cases
    test_cases = [] # The good tests cases
    mode = "" # The type of clash
    # Relative variables of the problem
    lang = "python" # The language to solve the clash in
    code = "" # The code of the user
    # Set up variable
    ide = ""

    # Init
    def __init__(self, ID, COOKIE, IDE="vscode") -> None:
        if ID == None:
            raise Exception("You must have an ID.")
        else:
            self.ID=ID

        if COOKIE == None:
            raise Exception("You must have a COOKIE.")
        else:
            self.COOKIE=COOKIE


        IDE=IDE.lower()
        # Add different extensions to the editor, to automatically open it
        if IDE == "neovim" or IDE == "nvim":
            self.ide = "nvim"
        elif IDE == "vim":
            self.ide = "vim"
        elif IDE == "vi":
            self.ide = "vi"
        elif IDE == "emacs":
            self.ide = 'emacs'
        elif IDE == "vscode":
            self.ide = "code"
        else:
            self.ide = "code"


    # Store the data in a JSON    
    def store_data(self):
        dump(
            {
                "ID": self.ID,
                "COOKIE": self.COOKIE,
                "game_id": self.game_id,
                "handle_code": self.handle_code,
                "statement": self.statement,
                "stub_generator": self.stub_generator,
                "test_cases": self.test_cases,
                "title": self.title,
                "test_cases_raw": self.test_cases_raw,
                "mode": self.mode,
                "lang": self.lang,
                "code": self.code,
                "public_handle": self.public_handle,
            },
            open("vars.json", "wt"),
            indent=4,
        )
        
    # Restore the data from the JSON
    def restore_data(self):
        data = load(open("vars.json", "r"))
        try:
            self.ID = data['ID']
            self.COOKIE = data['COOKIE']
            self.game_id = data['game_id']
            self.handle_code = data['handle_code']
            self.statement = data['statement']
            self.stub_generator = data['stub_generator']
            self.title = data['title']
            self.test_cases_raw = data['test_cases_raw']
            self.test_cases = data['test_cases']
            self.mode = data['mode']
            self.lang = data['lang']
            self.code = data['code']
            self.public_handle = data['public_handle']
        except KeyError as err:
            print(err)



    # Store the info of the clash that started
    def store_clash_info(self, data):
        self.handle_code = data["testSessionId"]
        # It's not really the problem ID, because the real one is testSessionId, but this string allow to submit solutions
        self.handle_code = data["testSessionHandle"]
        # Statement
        self.statement = data["currentQuestion"]["question"]["statement"]
        # STUB generator
        self.stub_generator = data["currentQuestion"]["question"]["stubGenerator"]
        # Test cases
        self.test_cases_raw = data["currentQuestion"]["question"]["testCases"]
        # Get the title
        self.title = data["currentQuestion"]["question"]["title"]
        # The mode
        self.mode = data['clash']["mode"]
        # Public game id
        self.public_handle = data['clash']["publicHandle"]
        print(data)

        # Initialize the test_cases with the good size
        self.test_cases = []
        for _ in self.test_cases_raw:
            self.test_cases.append({})


        # Update the code with the stub generator
        # But only if it's not shortest, because in shortest we can just take our time
        if self.mode.lower() != "shortest" and self.mode != "short":
            self.code = "\n".join(self.convert_generator())
            open("prog.py", "wt").write(self.code)
            self.lang = "Python"
            exe(f"{self.ide} prog.py")
        # Else, if it' shortest,
        # We don't need the stub generator tbh
        # So just set the lang to ruby
        else:
            self.lang = "Ruby"
            exe(f"{self.ide} prog.rb")
            

        # For every test case:
        for i in range(len(self.test_cases_raw)):
            self.get_test_case(i)

        self.test_cases = self.test_cases[:len(self.test_cases_raw)]


        # Store the data
        self.store_data()
        self.replace_html()


    # Get the players    
    def get_players(self):
        rep = self.fetch(
            f"https://www.codingame.com/services/TestSession/startTestSession",
            [self.handle_code]
        ).json()

        if 'clash' in rep and 'players' in rep['clash']:
            return rep
        else:
            return None



    # Get the headers
    def get_headers(self) -> str:
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=1",
            "Connection": "keep-alive",
            "Content-Length": "11",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": self.COOKIE,
            "Host": "www.codingame.com",
            "Origin": "https://www.codingame.com",
            "Referer": "https://www.codingame.com/home",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }

        return headers

    # Fetch
    def fetch(self, url, body=[ID]):
        self.restore_data()
        rep = post(url, json=body, headers=self.get_headers())
        return rep
    

    # Get the correct tests cases
    def get_test_case(self, n: int):

        new_headers = self.get_headers()

        new_headers["Accept"] = "application/json, text/plain, */*"
        new_headers["Host"] = "static.codingame.com"
        del new_headers["Cookie"] 
        del new_headers["Content-Length"] 
        del new_headers["Content-Type"] 

        input = get(
            "https://static.codingame.com/servlet/fileservlet?id="+str(self.test_cases_raw[n]['inputBinaryId']),
            headers=new_headers
        ).text

        output = get(
            "https://static.codingame.com/servlet/fileservlet?id="+str(self.test_cases_raw[n]['outputBinaryId']),
            headers=new_headers
        ).text

        # Store that in the class
        self.test_cases[n] = {
            "input": input,
            "output": output,
        }

        # Bump the json
        self.store_data()


    # Convert the generator into python code
    def convert_generator(self):
        l = []

        for e in self.stub_generator.splitlines():
            if r := search(r'^read (([\w\d_]+:\w+\s?)+)', e):

                print(r.group(1))

                # If there is multiple terms
                if r.group(1).count(" ") > 0:
                    l.append("line = input().split()")
                    for i,read in enumerate(r.group(1).split()):
                        l.append(
                            f'{read.split(":")[0]} = {read.split(":")[1].replace("string","").replace("word","").replace("long","int")}(line[{i}])'
                        )
                # Else, if there is only one term
                else:
                    l.append(
                        f'{r.group(1).split(":")[0]} = {r.group(1).split(":")[1].replace("string","").replace("word","").replace("long","int")}(input())'
                    )


            elif r := search(r'^write (.*)', e):
                l.append(
                    f'# say("{r.group(1)}")'
                )
            elif r := search(r'^loop ([\d\w]+) ([\w]+) (.*)', e):
                l.append(
                    f'\n\nfor i in range({r.group(1)}):'
                )
                for sub_e in r.group(3).split():
                    # Write
                    if r.group(2) == "write":
                        l.append(
                            f"    # say(\"{r.group(3)}\")"
                        )
                        break

                    # Read
                    else:
                        # If there is multiple terms
                        if r.group(3).count(" ") > 0:
                            l.append("line = input().split()")
                            for i,read in enumerate(r.group(3).split()):
                                l.append(
                                    f'    {read.split(":")[0]} = {read.split(":")[1].replace("string","").replace("word","").replace("long","int")}(line[{i}])'
                                )
                        # Else, if there is only one term
                        else:
                            l.append(
                                f'    {r.group(3).split(":")[0]} = {r.group(3).split(":")[1].replace("string","").replace("word","").replace("long","int")}(input())'
                            )

            elif r := search(r'^loopline ([^\s]+) ([\w\d_]+):\w+', e):
                l.append(
                    f'for e in input().split():\n    '
                )

        l += ["\n"]*3

        return l


    # Replace the HTML
    def replace_html(self, fail=[], got=[]):
        html = open("pages/template.html").read()
        html = html.replace("{{title}}", self.title)
        html = html.replace("{{description}}", self.statement)

        # Format the tests cases for HTML
        test_case_format = []
        
        # For each test in test_cases
        for it, test_case in enumerate(self.test_cases):
            try:
                print(test_case["input"])
                test_case_format.append(
                    f"""
                    <li class="{str(it not in fail) * (len(got) > it) }">
                        <div class="input">{test_case['input']}</div>
                        <div class="output">{test_case['output']}</div>
                        {
                            
                            f'''<div class="got">{got[it]}</div>'''
                            if len(got) > it else
                            ''
                        }
                    </li>
                    """
                )
            except KeyError as err:
                print(err)

        test_case_format = "\n".join(test_case_format)

        html = html.replace("{{test_cases}}", test_case_format)

        open("pages/index.html", "wt").write(html)

        wopen(f"file://{getcwd()}/pages/index.html")



    # Execute some code
    def exec(self, force=False):
        # Restore the data
        self.restore_data()

        # Get the code
        if self.lang.lower() == "python":
            exe("python3 translate_ast.py")
            self.code = open(f"tmp/prog.py",'rt').read()
            print(open(f"tmp/prog.py",'rt').read())
        else:
            self.code = open(f"prog.rb",'rt').read()
            
        self.store_data()

        # Generate a random number 
        test_id = "".join(chr(randint(65,90)) for _ in range(10))
        # Create directory if it doesn't exist
        makedirs(f"tmp/{test_id}", exist_ok=True)

        # Add the program
        open(f"tmp/{test_id}/prog.{'py'if self.lang.lower() == 'python'else'rb'}", "wt").write(self.code)

        # Create alls the input and output files
        for it,test_case in enumerate(self.test_cases):
            try:
                test_case["input"]
                open(f"tmp/{test_id}/in{it}.txt", "w").write(test_case["input"])
                open(f"tmp/{test_id}/out{it}.txt", "w").write(test_case["output"])
            except KeyError as error:
                print(error)

        # Execute each file
        exe(f"Docker/launchvm.sh {self.lang} {len(self.test_cases)} {test_id}")

        # Correct boolean
        correct = True
        fail = []
        tot_got = []

        # Veryify if the answer is correct
        for i in range(len(self.test_cases)):
            try: 
                excepted = self.test_cases[i]["output"]
                got = open(f"tmp/{test_id}/got{i}.txt").read()

                if got == "":
                    got = open(f"tmp/{test_id}/err{i}.txt").read()

                tot_got.append(got.replace("<", "&lt;").replace(">", "&gt;"))

                if excepted.strip("\n") != got.strip("\n"):
                    correct = False
                    fail += [i]
            except KeyError as error:
                print(error)
            except Exception as error:
                print(error)
        

        self.replace_html(fail, tot_got)

        # If it's a correct answer and not shortest, just submit
        if force or (correct and self.lang.lower() == "python"):
            # Get the player
            players = self.get_players()

            if players != None and any(player['score'] == 100 for player in players if 'score' in player):
                wopen(f"https://www.codingame.com/multiplayer/clashofcode")
            else:
                print(self.code)
                rep = self.submit_solution()
                print("========")
                print(rep)
                print(rep.text)
                print("========")

                self.test_cases_raw = []
                self.test_cases = []

                self.store_data()

                wopen(f"https://www.codingame.com/clashofcode/clash/report/{self.public_handle}")




    # Function that submits a solution
    def submit_solution(self):
        rep = self.fetch(
            "https://www.codingame.com/services/TestSession/submit",
            [
                self.handle_code, # The code that indentifies you and the problem at the same time
                {
                    "code": self.code, # The code
                    # The lang
                    "programmingLanguageId": self.lang if self.lang.lower() != "python" else f"{self.lang}3" ,
                },
                None # I have no idea why there is this, but every time that you submit a solution they put a null here
            ]
        )

        return rep
    


# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# # Access environment variables
# ID = os.environ.get('ID')
# COOKIE = os.environ.get('COOKIE')


# # Initialize the Client
# client = CustomCodinGameClient(ID, COOKIE, "vscode")

# # client.store_clash_info(ID)
# client.exec()