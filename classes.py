from functions import *
from re import *

class ExtendedString(str):
    # Initialize the string
    def __new__(cls, v="", *args):
        # If there is a set (in a f-string for example)
        if isinstance(v, set):
            v = next(iter(v))

        # If it's an array, join it
        if "<class 'list'>" == f'{type(v)}' or isinstance(v, ExtendedList):
            v = "".join(v)
        return super().__new__(cls, v or "")
    
    # Return
    def __getitem__(self, index):
        return ExtendedString(super().__getitem__(index))
    


    def __iter__(self):
        for c in super().__iter__():
            yield ExtendedString(c)

    # Types
    # Int
    @property
    def int(self):
        return ExtendedInt(self)
    
    # Float
    @property
    def float(self):
        return float(self)
    
    # Float
    @property
    def list(self):
        return ExtendedList(self)
    

    # String specific
    # Lower case
    @property
    def low(self):
        return ExtendedString(self.lower())
    
    # Upper case
    @property
    def up(self):
        return ExtendedString(self.upper())
    
    # Capitalize string
    @property
    def cap(self):
        return ExtendedString(self.capitalize())
    
    # Upper case
    @property
    def title(self):
        return ExtendedString(self.title())
    
    # Camel To Snake
    @property
    def camel_to_snake(self):
        return ExtendedString(camel_to_snake(self))
    
    # Camel To Snake
    @property
    def snake_to_pascal(self):
        return ExtendedString(snake_to_pascal(self))
    
    # Camel To Snake
    @property
    def snake_to_camel(self):
        return ExtendedString(snake_to_camel(self))
    
    # Sum of ords
    @property
    def sum(self):
        return ExtendedInt(sum(map(ord, self)))
    
    # Count how many times the char change in a string
    @property
    def chr_change(self):
        return ExtendedInt(chr_change(self))
    
    # Length of the binary expr
    @property
    def len(self):
        return ExtendedInt(len(self))
    
    # Max of the string
    @property
    def max(self):
        return ExtendedInt(max(self.m(ord)))
    
    # Min of the string
    @property
    def min(self):
        return ExtendedInt(min(self.m(ord)))
    

    # Filters
    ## Alpha
    @property
    def falpha(self):
        return ExtendedString(falpha(self))
    # Alnum
    @property
    def falnum(self):
        return ExtendedString(falnum(self))
    # Digit
    @property
    def fdigit(self):
        return ExtendedString(fdigit(self))
    # Upper
    @property
    def fup(self):
        return ExtendedString(fup(self))
    # Lower
    @property
    def flow(self):
        return ExtendedString(flow(self))
    # Vowels
    @property
    def fvow(self):
        return ExtendedString(fvow(self))
    # !Vowels
    @property
    def fcon(self):
        return ExtendedString(fcon(self))
    


    # Short map
    def m(self, function):
        res = ExtendedList(map(lambda c: function(ExtendedString(c)), self))

        # If it's all string
        if all(isinstance(e, ExtendedString) for e in res):
            return ExtendedString("".join(res))
        else:
            return ExtendedList(res)
    
    # Short filter
    def f(self, function):
        return ExtendedString("".join(map(lambda c: ExtendedString(c), filter(lambda c: function(ExtendedString(c)), self))))
    
    # Remove substring things
    def rm(self, other):
        if isinstance(other, ExtendedList):
            temp_string = self
            for s in other:
                temp_string=temp_string.replace(s, "")
            return temp_string
        elif isinstance(other, ExtendedString):
            return self.replace(other, "")
        else:
            return NotImplemented
        
    # Count the number of char in a string
    def cnt(self, other):
        if isinstance(other, ExtendedString):
            return ExtendedInt(self.count(other))
        elif str(type(other)) == "<class 'function'>":
            return ExtendedInt(sum(map(other, self)))
        else:
            return NotImplemented

    # Rotate the ord of the char of the strings
    def rotate_ord(self, n: int):
        return ExtendedString(rotate(self, n))
    def rotate_chr(self, n: int):
        return ExtendedString(rotate(self, n))
    
    # Rotate
    def rotate(self, n: int):
        if n == 0:
            return self
        return ExtendedString(self[-n:] + self[:-n])
    
    # Split a string every n char
    def n_split(self, step):
        return ExtendedList(n_split(self, step))
        
    # Modify the default function
    # So that it returns an Extended List
    #
    # Sadly we can't just do return self.split(*args)
    # Because of recursion problems.
    def split(self, delimiter=" "):
        result = ExtendedList([])
        current = ExtendedString('')

        for char in self:
            if char == delimiter:
                result.append(current)
                current = ExtendedString('')
            else:
                current += char

        result.append(current)

        return result
    

    # Regex
    ## Get (equivalent of findall or scan)
    def get(self, regex):
        match_regex = findall(regex, self)
        return ExtendedList(match_regex)
    
    ## Sub
    def sub(self, regex, _str):
        return ExtendedString(sub(regex, _str, self))
    
    ## Search
    def search(self, regex):
        match_regex = search(regex, self)
        return -1 if not match_regex else match_regex.start()


        
    

    # + Operator
    def __add__(self, other):
        if isinstance(other, ExtendedString):
            return ExtendedString(f"{self}{other}")
        elif isinstance(other, int):
            return ExtendedString(f"{self}{other}")
        elif isinstance(other, float):
            return ExtendedString(f"{self}{other}")
        else:
            return NotImplemented
    
    def __radd__(self, other):
        if isinstance(other, int) or isinstance(other, ExtendedInt):
            return ExtendedString(f"{other}{self}")
        if isinstance(other, float):
            return ExtendedString(f"{other}{self}")
        else:
            return NotImplemented

    # - Operator
    def __sub__(self, other):
        if isinstance(other, int):
            return ExtendedString(self[:-other])
        if isinstance(other, float):
            return ExtendedString(self[:-round(other)])
        else:
            return NotImplemented
    
    # / Operator (in this context, replace)
    def __truediv__(self, other):
        if isinstance(other, ExtendedString):
            temp_s = self
            for c in other:
                temp_s=temp_s.replace(c, "")
            return ExtendedString(temp_s)
        else:
            return NotImplemented
        
    # // Operator (in this context, split)
    def __div__(self, other):
        if isinstance(other, ExtendedString):
            return self.split(other)
        else:
            return NotImplemented
        


# Extended List
class ExtendedList(list):
    # Length of the list
    @property
    def len(self):
        return ExtendedInt(len(self))
    
    # Min of the list
    @property
    def min(self):
        return ExtendedInt(min(self))
    
    # Max of the list
    @property
    def max(self):
        return ExtendedInt(max(self))
    
    # Sum of the list
    @property
    def sum(self):
        return ExtendedInt(sum(self))

    # Short map
    def m(self, function):
        return ExtendedList(map(function, self))
    
    # Short Filter
    def f(self, function):
        return ExtendedList(filter(function, self))

    # Remove substring things
    def rm(self, other):
        if isinstance(other, ExtendedList):
            temp_list = self
            for e in other:
                if e in self:
                    temp_list.remove(e)
            return temp_list
        else:
            if other in self:
                self.remove(other)
            return self
    
    # Count the number of something in array
    def cnt(self, other):
        if str(type(other)) == "<class 'function'>":
            return sum(map(other, self))
        else:
            return self.count(other)
        
    # * Operator
    def __mul__(self, other):
            if isinstance(other, ExtendedString):
                return ExtendedString(ExtendedString(other).join(ExtendedString(e) for e in self))
            else:
                return NotImplemented

    # - Operator
    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, ExtendedInt):
            return ExtendedList(self[:-other])
        if isinstance(other, float):
            return ExtendedList(self[:-round(other)])
        if isinstance(other, ExtendedList):
            return self.f(lambda e: e not in other)
        else:
            return NotImplemented


# Extended int
class ExtendedInt(int):
    # Types
    @property
    def str(self):
        return ExtendedString(self)
    
    # Transform it to char
    @property
    def chr(self):
        return ExtendedString(chr(self))



    # Functions
    # Is a number prime
    @property
    def isprime(self):
        return is_prime(self)
    
    # Counts 1 in binary expr
    @property
    def count1(self):
        return ExtendedInt(bin(self).count("1"))
    
    # Counts 0 in binary expr
    @property
    def count0(self):
        return ExtendedInt(bin(self).count('0')-1)

    # Length of the binary expr
    @property
    def len(self):
        return len(self)



    # Is a number a fibonacci number
    def isfib(self, a=0, b=1):
        return is_fib(self, a, b)




    # @ Operator <=> Range
    def __matmul__(self, other):
          if isinstance(other, int):
            return ExtendedList(range(self, other))
    
    # [] Operator 
    def __getitem__(self, n):
        bin_exp = bin(self)[2:]

        if n >= len(bin_exp):
            return 0
        
        return ExtendedInt(bin_exp[~n])
    
    # Length function
    def __len__(self, n):
        bin_exp = bin(n)
        return ExtendedInt(len(bin_exp) - 2) # We remove 2 because of the 0b
    
