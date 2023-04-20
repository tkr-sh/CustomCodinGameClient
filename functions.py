import re
from math import *
from classes import *

# Filter alpha
falpha = lambda s: "".join(filter(lambda c:c.isalpha(),s))
# Filter alnum
falnum = lambda s: "".join(filter(lambda c:c.isalnum(),s))
# Filter digit
fdigit = lambda s: "".join(filter(lambda c:c.isdigit(),s))
# Filter lower
flow = lambda s: "".join(filter(lambda c:c.islower(),s))
# Filter uppers
fup = lambda s: "".join(filter(lambda c:c.isupper(),s))
# Filter vowels
fvow = lambda s, y=False: "".join(filter(lambda c:c in "AEIOUaeiou"+ExtendedString(["","Yy"][y>0]),s))
# Filter cons
fcon = lambda s, y=False: "".join(filter(lambda c:c.isalpha() and c not in "AEIOUaeiou"+[ExtendedString(""),ExtendedString("Yy")][y>0],s))
# Is fibonacci
is_fib = lambda n, a=0, b=1: n == a if n<=a else is_fib(n,b,a+b)
# Get the n-th Fibonacci number
fib = lambda n,a=0,b=1,it=0:a if n==it else fib(n,b,a+b,it+1) 
# Is prime
is_prime = lambda n: False if n<2 else all(n%i for i in range(2, int(sqrt(n))+1))
# Prime form 2 to n
prime_to = lambda n: [i for i in range(n) if is_prime(i)]
# Create a list of size n with n being the length of the list
prime_size = lambda n, lst=[], it=0: lst if len(lst) >= n else (prime_size(n, lst + [it] , it+1) if is_prime(it) else prime_size(n, lst, it+1))
# Count the number of time, that a char changes
chr_change = lambda s, p="", lst=[], it=0: lst + [p] if it >= len(s) else (chr_change(s, s[it], lst, it+1) if p == "" else (chr_change(s, p+s[it], lst, it+1) if s[it] in p else chr_change(s, s[it], lst+[p], it+1 )))
# Count 1 in binary expr
count1 = lambda n: bin(n).count("1")
# Count 0 in binary expr
count0 = lambda n: bin(n).count("0")-1
# SPlit every n char
n_split = lambda s, step=1: [s[i:i+step] for i in range(0, len(s), step)]
# Rotate str by n
rotate = lambda s, n: "".join([c,chr((ord(c)-97+n)%26+97 if c.islower() else (ord(c)-65+n)%26+65)][c.isalpha()] for c in s)
# Sum all the numbers in the string
sum_numbers = lambda s: 0 if all(c.isalpha()for c in s) else eval('+'.join(re.findall('\d+',s)))
# Convert Camel case to snake
camel_to_snake = lambda s: ''.join("_"+c.low if c.isupper() else c for c in ExtendedString(s)).strip('_')
# Convert Snake case to Pascal
snake_to_pascal = lambda s: ''.join(x.capitalize() or '_' for x in s.split('_'))
# Convert snale case to Camel
snake_to_camel = lambda s: (z:=''.join(x.capitalize() or '_' for x in s.split('_')))[0].lower()+z[1:]
# Return
anagram = lambda s,z: set(s) == set(z)
cnt = lambda f, iterable: sum(f(e) for e in iterable)

# Rock Paper scissors
def rps(p1_choice, p2_choice):
    if p1_choice == p2_choice:
        return 0
    elif (p1_choice == 'rock' and p2_choice == 'scissors') or (p1_choice == 'paper' and p2_choice == 'rock') or (p1_choice == 'scissors' and p2_choice == 'paper'):
        return 1
    elif (p2_choice == 'rock' and p1_choice == 'scissors') or (p2_choice == 'paper' and p1_choice == 'rock') or (p2_choice == 'scissors' and p1_choice == 'paper'):
        return 2
    else:
        return -1



# Convert attributes to functions
isdigit = lambda s: s.isdigit()
isalpha = lambda s: s.isalpha()
isalnum = lambda s: s.isalnum()
isupper = lambda s: s.isupper()
islower = lambda s: s.islower()
isint = lambda f: float(int(f)) == f

# Builtins functions modification
say=print
int=ExtendedInt
str=ExtendedString
list=ExtendedList


_builtin_range = range
range = lambda *args: ExtendedList(map(ExtendedInt, _builtin_range(*args)))
_builtin_sum = sum
sum = lambda iterable: _builtin_sum(map(ord,iterable)) if isinstance(iterable, ExtendedString) else _builtin_sum(iterable)
_builtin_input = input
input = lambda: ExtendedString(_builtin_input())


## Convert to extended string
_builtin_chr=chr
_builtin_hex=hex
_builtin_oct=oct
_builtin_bin=bin
_builtin_format=format
chr=lambda *args: ExtendedString(_builtin_chr(*args))
hex=lambda *args: ExtendedString(_builtin_hex(*args))
oct=lambda *args: ExtendedString(_builtin_oct(*args))
bin=lambda *args: ExtendedString(_builtin_bin(*args))
format=lambda *args: ExtendedString(_builtin_format(*args))

