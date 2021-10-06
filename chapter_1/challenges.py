from typing import Any, Callable

"""
Implement, as best as you can, the identity function in your favorite language (or the second favorite, if your favorite language happens to be Haskell).
2. Implementthecompositionfunctioninyourfavoritelanguage. It takes two functions as arguments and returns a function that is their composition.
3. Write a program that tries to test that your composition function respects identity.
4. Is the world-wide web a category in any sense? Are links morphisms?
5. Is Facebook a category, with people as objects and friendships as morphisms?
6. When is a directed graph a category?
"""


def identity(x: Any) -> Any:
    return x

def compose(
        f: Callable[[Any], Any], 
        g: Callable[[Any], Any]
    ) -> Callable[[Any], Any]:
    return lambda x: f(g(x))

def test_function(x: int) -> int:
    return x + 5

print(compose(identity, test_function)(10))
print(compose(test_function, identity)(10))

