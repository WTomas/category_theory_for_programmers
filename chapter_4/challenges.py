from typing import Generic, TypeVar, Callable

### Question 1

_T = TypeVar('_T')

class Optional(Generic[_T]):
    __is_valid: bool
    __value: _T | None

    def __init__(self, v: _T = None):
        self.__value = v
        self.__is_valid = v != None

    @property
    def is_valid(self) -> bool:
        return self.__is_valid
    
    @property
    def value(self) -> _T | None:
        return self.__value
    

a = Optional()
b = Optional(10)

print(a.is_valid, a.value)
print(b.is_valid, b.value)


### Question 2

def safe_reciprocal(v: float) -> Optional[float]:
    if v != 0:
        return Optional(1/v)
    return Optional()
        
x = safe_reciprocal(10)
y = safe_reciprocal(-0.5)
z = safe_reciprocal(0)

print(x.is_valid, x.value)
print(y.is_valid, y.value)
print(z.is_valid, z.value)


### Question 3

def safe_root(v: float) -> Optional[float]:
    if v >= 0:
        return Optional(v ** 0.5)
    return Optional()

_A = TypeVar('_A')
_B = TypeVar('_B')
_C = TypeVar('_C')


def compose(f1: Callable[[_A], Optional[_B]], f2: Callable[[_B], Optional[_C]]) -> Callable[[_A], Optional[_C]]:
    def composed(a: _A) -> Optional[_C]:
        o1 = f1(a)
        if not o1.is_valid:
            return Optional()
        return f2(o1.value)
    return composed


safe_root_reciprocal = compose(safe_reciprocal, safe_root)

r1 = safe_root_reciprocal(1/4)
r2 = safe_root_reciprocal(0)
r3 = safe_root_reciprocal(-0.5)

print(r1.is_valid, r1.value)
print(r2.is_valid, r2.value)
print(r3.is_valid, r3.value)
