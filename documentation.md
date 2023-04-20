# Classes
For every method or property of a class, when the return type is "int", "str" or "list", it's not going to be an **`int`** a `str` or a `list` but an `ExentdedInt`, `ExtendedString` and `ExtendedList`
## String
### Properties
#### .int
> str: int

Return the string converted to an extended int


#### .float
> str: float

Return the string converted to a flaot


#### .list
> str: list[str]

Return an extended list of each char in the string


#### .low
> str: str

Equivalent to str.lower()


#### .up
> str: str

Equivalent to str.upper()


#### .cap
> str: str

Equivalent to str.capitalize()


#### .title
> str: str

Equivalent to str.title()


#### .camel_to_snake
> str: str

Convert the string from a camelCase to a snake_case


#### .snake_to_pascal
> str: str

Convert the string from a snake_case to a PascalCase


#### .snake_to_camel
> str: str

Convert the string from a snake_case to a camelCase


#### .sum
> str: int

Return the sum of all the ords in the string
```py
sum(map(ord,str))
```


#### .chr_change 
> str: int

Return how many times, the char changed.
```
aaabccccddddaaa
000122223333444
```
So chr_change will return 4


#### .len
> str: int

Equivalent to `len(str)`


#### .max
> str: int

Max of ord of the string


#### .min
> str: int

Min of ord of the string


#### .falpha
> str: str

Filter alpha char


#### .falnum
> str: str

Filter alnum char


#### .fdigit
> str: str

Filter digit char


#### .fup
> str: str

Filter upper char


#### .flow
> str: str

Filter lower char


#### .fvow
> str: str

Filter vowels char


#### .fcon
> str: str

Filter consomns char


### Methods
#### .m()
> str: function ->  str | list[any]

Equivalent of `list(map(function, str))`.
If all elements returned by the map are string, it will join them, else it will return the list

_Example_:
```py
"abcde".m(lambda c: chr(c.ord+1)) # "bcdef"
"abcde".m(lambda c: c.ord + 1) # [98, 99, 100, 101, 102]
```


#### .f()
> str: function -> str

Equivalent of `"".join(filter(function, str))`.

_Example_:
```py
"abcdefabcdef".f(lambda c: c <= 'c') # abcabc
"abcdefabcdef".f(lambda c: c > 'c') # defdef
```


#### .rm()
> str: str | list -> str

The first argument, is the char to remove or the list of char to remove.

_Example_:
```py
"abcdef".rm("abc") # def
"abcdef".rm(['a', 'c', 'e']) # bdf
```


#### .cnt()
> str: str | function -> int

If the argument is a str, it's just the equivalent of `str1.count(str2)`
Else, it's a lambda function that counts how many times does it match.
Which is the same as
```py
sum(map(function, str))
```
or
```py
len(filter(function, str))
```

_Example_:
```py
"abcdefghijkl".cnt(lambda c: c <= 'e') # 5 (a,b,c,d,e)
"abcdefghijkl".cnt(lambda c: c > 'e') # 7 (f,g,h,i,j,k,l)
```


#### .rotate_ord() | .rotate_chr()
> str: int -> str

Rotate the ord of alphabetical char.

_Example_:
```py
"abcDEF".rotate_ord(1) # "bcdEFG"
```


#### .rotate()
> str: int -> str

Rotate the string

_Example_:
```py
"abcdef".rotate(1) # "fabcde"
"abcdef".rotate(-1) # "bcdefa"
```


#### .n_split()
> str: int -> list[str]

Split a string every n char.

_Example_:
```py
"abc".n_split(2) # ["ab", "c"]
"abcdef".n_split(3) # ["abc", "def"]
```


#### .get()
> str: regex -> list[str]

Equivalent to 
```py
re.findall(regex, str)
```


#### .sub()
> str: regex, str -> str

Equivalent to
```py
re.sub(regex, str, self)
```


#### .search()
> str: regex -> int

The index of the match in the string


### Operators
#### - (operator)
> str: int -> str

Will return `str[:-int]`


#### / (operator)
> str: str -> str

Will remove every occurences of every char in the string in argument.

_Example_:
```py
"abcdef"/"abc" # def
"CaseMatter"/"ca" # CseMtter
```


#### // (operator)
> str: str -> str

Equivalent to `str.split(_arg_str)`




## List
### Properties
#### .len
> list: int

Equivalent to `len(list)`


#### .min
> list: int

Equivalent to `min(list)`


#### .max
> list: int

Equivalent to `max(list)`


#### .sum
> list: int

Equivalent to `sum(list)`


### Methods
#### .m()
> list: function -> list

Same as [str.m()](#m-1)


#### .f()
> list: function -> list

Same as [str.f()](#f-1)


#### .rm()
> list: any -> list

Same as [str.rm()](#rm-1)


#### .cnt()
> list: any -> int

Same as [str.cnt()](#cnt-1)


### Operators
#### * (operator)
> list: str -> str

Equivalent to
```py
str.join(list)
```


#### - (operator)
> list: int -> list

Same as `list[:-int]`


> list: list -> list

Remove every element from `self` that are also in the list in argument (as in ruby)

_Example_:
```py
[3, 4, 5, 6, 5] - [3, 5, 3] # [4, 6]
```

## Int
### Properties
#### .str
> int: str

Equivalent of `str(int)`


#### .chr
> int: str

Equivalent of `chr(int)`


#### .isprime
> int: bool

Return true if the int is a prime. Else false


#### .count1
> int: int

Count the number of 1 in the binary expression


#### .count0
> int: int

Count the number of 0 in the binary expression


#### .len
> int: int

The length of the binary expression when you remove trailing 0

```py
(0b11101).len # 5
(0b011101).len # 5
(31).len # 5
(32).len # 6
```

### Methods
#### .isfib()
> int: int,int -> bool

Say if the number is a fibonacci number, with the 2 first term being thoses in parameter

### Operators
#### @ (operator)
> int: int -> list[int]

Equivalent of `range(a,b)`

#### [] (operator)
> int: int -> int

The n-th bit.