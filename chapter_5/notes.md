# Section 5.5 - Products
Given any type `c` with two projections `p` and `q`, there is a unique `m` from `c` to the cartesian product `(a, b)` that factorizes them.

Meaning, we have:
```
p :: c -> a
q :: c -> b
m :: c -> (a, b)
m x = (p x, q x)
```

This makes the cartesian product the best match for our product.

The higher order function which takes the candidate projections (`p` and `q` ) and produces the factorizing function `m` is sometimes called the factorizer.
```
factorizer :: (c -> a) -> (c -> b) -> (c -> (a, b))
factorizer p q = \x -> (p x, q x)
```

The inverse of the product is called co-product, and it is defined as the two injections, such as:
```
i :: a -> c
j :: b -> c
```

Again, the most general and best `c` compared to `c'` exists if the there is a morphism `m` which factorizes the injections `i'` and `j'`. i.e.:
```
m :: c -> c'

i' :: a -> c'
i' = m . i

j' :: b -> c'
j = m . j
```

Unlike the cannonical product implementation built into Haskell as just a pair, the coproduct is represented by the `Either` datastructure. 

```
Either a b :: Left a | Right b
```

Once again, a higher order factorizer can be defined for the coproduct:
```
factorizer :: (a -> c) -> (b -> c) -> Either a b -> c
factorizer i _ Left x = i x
factorizer _ j Right y = j y


```












