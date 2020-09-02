# To start project

import mro into your new file, and do the following on defined classes

```
from c3 import mro

class_order = mro(class_name)

print([a_class.__name__ for a_class in class_order])
```

# Expected output

program is expected to output the class iself and a its ancestors, ordered from the nearest ancestor to the furthest, `[class1, class2, class3, class4, class5]` .

# c3 Algorithm
In computing, C3 superclass linearization is an algorithm used primarily to obtain the order in which methods should be inherited in the presence of multiple inheritance. In other words, the output of C3 superclass linearization is a deterministic Method Resolution Order (MRO) 
[source](https://en.wikipedia.org/wiki/C3_linearization)

# mro definition

**mro** method resolution order of a class is defined as a set of rules that determine the linearization of a class an its ancestors.The c3 linearization of a class is the sum of the class plus a unique merge of the linearizations of its parents defined by:
 `mro(A) = [A] + merge([ [mro(1)] ,[mro(2),..mro(n)] ])`

simply put, **mro** is the order in which Python looks for a method in a hierarchy of classes.

for a simple case, 
```
class A: pass
class B (A): pass
class C (B): pass
```
C subclasses B and B subclasses A  and A subclasses Objects. Therefore linearization of a class C is definded as  `mro(C) = [C] + merge([mro(B)])` recursively calling `mro(B)` defines it as `mro(B) = [B] + merge([mro(A)])` recursively calling `mro(A)` , `mro(A) = [A] + merge([mro(0)])` , for the base case, 
```
if the_cls is object:
        # if class is object
        return [object]
```
therefere `mro(A) = [A] + merge([object])`

**merge** The merge of parents' linearizations is done by selecting the first head of the lists which does not appear in the tail (all elements of a list except the first) of any of the lists. **Note: a good head may appear as the first element in multiple lists at the same time, but should not appear anywhere else**

```
def merge(mros):
    if not any(mros):
        # if mro is an empty list
        return []
    for current, *_ in mros:
        # *_ takes other values after first as a variable
        if all(current not in tail for _, *tail in mros):
            return [current] + merge(
                [tail if head is current else [head, *tail] for head, *tail in mros]
            )

        # if i've gone through every item in list
    else:
        raise TypeError("class heiracy not legal")
```

**base case** states that if an empty list is passed, an empty list is returned , thus ` merge([objects)` is 
`[object] + merge([])` ---> `[object]+[]` ---> `[object]`


therfore  `mro(A) = [A] + merge([object]` --> [A,object]
then `mro(B) = [B] + merge([mro(A)])`  ---> `[B] + merge([A,object])`

`merge([A,object])` is `[A] + merge(object)`

so `mro(B) = [B] + merge([mro(A)])` --> [B,A,Object]

**finally** `mro(C) = [C] + merge([mro(B)])`  is `[C] + merge([B,A,Object])`
thus `[C,B] + merge([A,Object])`

running this recursvely produces: 

`[__main__.C, __main__.B, __main__.A, object]`