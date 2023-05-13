import abc
import math

### 1.
# Show the isomorphism between Maybe a and Either () a
# In Haskell syntax:
# maybeToEither :: Maybe a -> Either () a
# maybeToEither Nothing = Left ()
# maybeToEither Just a = Right a
# Other way around:
# eitherToMaybe :: Either () a -> Maybe a
# eitherToMaybe Left () = Nothing
# eitherToMaybe Right a = Just a

### 2./3./4.
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self) -> float:
        pass

    @abc.abstractclassmethod
    def circ(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, r: float):
        self.r = r

    def area(self) -> float:
        return (self.r ** 2) * math.pi
    
    def circ(self) -> float:
        return 2 * math.pi * self.r
    
    


class Rectangle(Shape): 
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def area(self) -> float:
        return self.a * self.b
    
    def circ(self) -> float:
        return (self.a + self.b) * 2
    

class Square(Shape):
    def __init__(self, a: float):
        self.a = a
    
    def area(self) -> float:
        return self.a ** 2
    
    def circ(self) -> float:
        return self.a * 4 
    

# In haskell, we would need to extend the pattern matching of the area and circ functions to account for Square

# a + a can be represented as Either a a = Left a | Right a
# 2 * a can be respresented as (Either () (), a) = (Either () (), a)
# we can write morphisms to turn one into the other
# m1 :: Either a a -> (Either () (), a)
# m1 (Left a) = (Left (), a)
# m1 (Right a) = (Right (), a)
# 
# m1':: (Either () (), a) -> Either a a
# m1' (Left (), a) = Left a
# m1' (Right (), a) = Right a
# 
# Note: Either () () = Left () | Right () is equivalent to Bool = True | False up to isomorphism:
# eitherToBool :: Either () () -> Bool
# eitherToBool Left () = True
# eitherToBool Right () = False
# 
# boolToEither :: Bool -> Either () ()
# boolToEither True = Left ()
# boolToEither False = Right ()





