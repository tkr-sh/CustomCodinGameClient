mv prog.py prog.py~
cp test/$1.py prog.py
cp functions.py tmp/functions.py
rm tmp/prog.py
python3 translate_ast.py
echo "\n\n# Test it 
try:
    test()
    print(\"\033[042m    Success!     \033[0m\")
except AssertionError as e:
    print(f\"Erorr: {e}\")
    print(\"\033[041m     Fail.     \033[0m\")" >> tmp/prog.py
python3 tmp/prog.py
rm prog.py
mv prog.py~ prog.py