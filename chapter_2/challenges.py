# 1. Define a higher-order function (or a function object) memoize 
# in your favorite language. This function takes a pure function 
# f as an argument and returns a function that behaves almost 
# exactly like f, except that it only calls the original function 
# once for every argument, stores the result internally, and 
# subsequently returns this stored result every time it’s called 
# with the same argument. You can tell the memoized function from 
# the original by watch- ing its performance. For instance, try to 
# memoize a function that takes a long time to evaluate. You’ll 
# have to wait for the result the first time you call it, but on 
# subsequent calls, with the same argument, you should get the 
# result immediately.
print('Question 1)')

from functools import lru_cache
import time

memoize = lru_cache # hehe cheating

def timeit(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        end = time.time()
        print(f'This took {end - start:.4f} seconds!')
        return res
    return wrapper

def long_function(x: int) -> int:
    time.sleep(min(max(x, 1), 5)) # sleep between 1-5 seconds
    return x + 10

@lru_cache(None)
def memoized_function(x: int) -> int:
    return long_function(x)

print(timeit(long_function)(1)) # takes a long time
print(timeit(memoized_function)(1)) # takes a long time
print(timeit(memoized_function)(1)) # almost instantaneous

# Naive implementation of caching/memoization
# cache = {}
def manual_memoizer(f):
    cache = {}
    def wrapper(*args, **kwargs):
        arguments = tuple(list(args) + list(kwargs.items()))
        cache
        if arguments in cache:
            return cache[arguments]
        res = f(*args, **kwargs)
        cache[arguments] = res
        return res
    return wrapper

@manual_memoizer
def manually_memoized_function(x: int) -> int:
    return long_function(x)

print('Manual memoizer')
print(timeit(manually_memoized_function)(1))
print(timeit(manually_memoized_function)(1))
print()

# -----------------------------------
# 2. Try to memoize a function from your standard library 
# that you normally use to produce random numbers. Does it work?
print('Question 2)')

import random

@manual_memoizer
def memoized_random() -> float:
    return random.random()

print(memoized_random())
print(memoized_random())
print()

# Nope, it will not, as random takes no arguments,
# now the memoizer will return the same value 
# that the first call produced, because we are mapping
# () (set with a single member `unit`) to the set of Floats. 
# This function can only map to 1 element of Floats, as the 
# input is always the same (nothing).

# -----------------------------------

# 3. Most random number generators can be initialized with a seed. 
# Implement a function that takes a seed, calls the random number 
# generator with that seed, and returns the result. 
# Memoize that function. Does it work?
print('Question 3)')
def seeded_random_number_generator(seed: int) -> float:
    random.seed(seed)
    return random.random()

@manual_memoizer
def memoized_seeded_random_number_generator(seed: int) -> float:
    return seeded_random_number_generator(seed)

print(seeded_random_number_generator(1))
print(seeded_random_number_generator(1))
print(memoized_seeded_random_number_generator(1))
print(memoized_seeded_random_number_generator(1))

print(seeded_random_number_generator(2))
print(seeded_random_number_generator(2))
print(memoized_seeded_random_number_generator(2))
print(memoized_seeded_random_number_generator(2))
print()

# In this case, we are essentially mapping every 
# integer to a float. Since the seeding happens every time in the function,
# the memoization actually has no effect, as the return value will be the 
# deterministic based on that seed anyways. 

# -----------------------------------
# 4. Which of these C++ functions are pure? 
# Try to memoize them and observe what happens 
# when you call them multiple times: memoized and not.

"""
a)

int fact(int n) 
{ 
    int i;
    int result = 1;
    for (i = 2; i <= n; ++i)
        result *= i; 
    return result;
}

Yes, this is a pure function, 
as it does not have any side effects 
and always produces the same output based 
on the same input. 
"""

"""
b)
std::getchar()
Reads the next character from stdin.

Not a pure function as it depends on user input (side effect). 
"""

"""
c)
bool f() 
{
    std::cout << "Hello!" << std::endl; 
    return true;
}

Not a pure function as it produces a side effect.
"""

"""
d)
int f(int x) 
{
    static int y = 0;
    y += x;
    return y;
}

Pure function, no side effects and also deterministic.
"""

# -----------------------------------

# 5. How many different functions are there from Bool to Bool? 
# Can you implement them all?

"""
We can have: 
True -> True
True -> False
False -> True
False -> False

This is actually just two functions, identity and negation.
"""
print('Question 5)')
def identity(b: bool) -> bool:
    return b

def negation(b: bool) -> bool:
    return not b

print(identity(True))
print(identity(False))
print(negation(True))
print(negation(False))
print()




