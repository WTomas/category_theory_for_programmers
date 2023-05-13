from typing import TypeVar, Callable, Generic
from dataclasses import dataclass

### 4.

L = TypeVar('L')
R = TypeVar('R')
T = TypeVar('T')

@dataclass
class Either(Generic[L, R]):
    __Left: L
    __Right: R

    def __init__(self):
        self.__Left = None
        self.__Right = None

    @property
    def Left(self) -> L:
        return self.__Left
    
    @Left.setter
    def Left(self, left: L) -> None:
        if self.__Right:
            raise Exception('Right has already been set.')
        self.__Left = left
        
    @property
    def Right(self) -> R:
        return self.__Right
    
    @Right.setter
    def Right(self, right: R) -> None:
        if self.__Left:
            raise Exception('Left has already been set.')
        self.__Right = right
        

    
    def case(self, f: Callable[[L], T], g: Callable[[R], T]) -> T:
        if self.Left:
            return f(self.Left)
        else: 
            return g(self.Right)
    
l = Either()
l.Left = 123
r = Either()
r.Right = 'abc'

def f(left: int) -> bool:
    return left == 123

def g(right: str) -> bool:
    return False

print(l.Left, l.Right)
print(r.Left, r.Right)
print(l.case(f, g))
print(r.case(f, g))

### 5.

def i(n: int) -> int:
    return n

def j(b: bool) -> int:
    return int(not b)

def m(e: Either[int, bool]) -> int:
    if e.Left: 
        return e.Left
    else: 
        return int(not e.Right)
    
# i = m . Either
# j = m . Either
# Thus, we have defined a morphism m, which factorizes injections i and j

e1 = Either()
e1.Left = 10
print(i(10) == m(e1))

e2 = Either()
e2.Right = False
print(j(False) == m(e2))

### 6.
# Int with injections i and j cannot be better than Either, as we cannot find a morphism going from Int with i and j to Either which factorizes Left and Right.
# def m_int(i: int)-> Either[int, bool]:
#     e = Either()
#     if i == 0:
#         e.Left = 0
#         e.Right = True
#         # ^impossible
#     elif i == 1:
#         e.Left = 1
#         e.Right = False
#         # ^impossible
#     else: 
#         e.Left = i
#    return e
# So int equipped with injections i and j results in ambiguous behaviour.

def i_prime(n: int) -> int:
    if n < 0:
        return n
    return n + 2

def j_prime(b: bool) -> int:
    return int(not b)

# In this case, there is no ambiguity when defining a morphism m' from Int to Either

def m_prime(n: int) -> Either[int, bool]:
    e = Either()
    if n == 0:
        e.Right = True
    elif n == 1:
        e.Right = False
    else:
        e.Left = n
    return e

# However, this implementation prevents Left from ever taking the values 0 or 1, whereas this is not an issue with Either. So Either is better.

### 7.
_L = TypeVar('_L')
_R = TypeVar('_R')


class TripleEither(Generic[_L, _R]):
    __Left: _L
    __Middle: _L
    __Right: _R

    @property
    def Left(self) -> _L:
        return self.__Left
    
    @Left.setter
    def Left(self, left: _L) -> None:
        if self.__Right:
            raise Exception('Right has already been set.')
        self.__Middle = left
        self.__Left = left
        
    @property
    def Right(self) -> _R:
        return self.__Right
    
    @Right.setter
    def Right(self, right: _R) -> None:
        if self.__Left or self.__Middle:
            raise Exception('Left and Middle has already been set.')
        self.__Right = right

    @property
    def Middle(self) -> _L:
        return self.__Middle
    
    # Middle cannot explicitly be set alone.
    

def m_dprime1(te: TripleEither[int, int, bool]) -> Either[int, bool]:
    e = Either()
    if te.Left:
        e.Left = te.Left
    else:
        e.Right = te.Right

def m_dprime2(te: TripleEither[int, int, bool]) -> Either[int, bool]:
    e = Either()
    if te.Middle:
        e.Left = te.Middle
    else:
        e.Right = te.Right

# Thus, we have multiple acceptable implementations from the morphism going from TripleEither to Either.

