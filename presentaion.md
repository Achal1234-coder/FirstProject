# Presentation on List, Set, Dictionary Comprehension

## Comprehension in Python

The comprehension consists of a single expression followed by at least one for clause.

## There are three comprehensions in Python.
   1. List Comprehension
   2. Set Comprehension
   3. Dictionary Comprehension
## List Comprehension
List comprehension is a way to define and create lists in Python in a concise way.

**Syntax:-**

```python
[expression for item in iterable if conditional]
```
This is equivalent to:-

```python
for item in iterable:
    if conditional:
        expression
```

## How to initialize 1D list with (0) with the help List Comprehension

### using for loop

```python
mylist = []
for i in range(5):
    mylist.append(0)
print(mylist)
```
**Output**
```python
[0, 0, 0, 0, 0]
```

using List Comprehension
```python
mylist = [i for i in range(5)]
print(mylist)
```
**output**
```python
[0, 0, 0, 0, 0]
```

## List Comprehension vs for loop

By using List Comprehension, it is more concise and readable comparing to for loop.

using for loop
```python
# Using for loop
l1 = []
for i in range(1, 11):
    a = i*i
    l1.append(a)
print(l1)     #Output:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

using list comprehension
```python
#Using List Comprehension
l2 = [i*i for i in range(1, 11)]
print(l2) #Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
## List comprehension vs filter
using filter

```python
#Using filter function
evennumber = filter(lambda x: x%2==0,range(1, 11))
#filter() returns an iterator.
print(evennumber) #Output:<filter object at 0x0144EC10>
print(list(evennumber))#Output:[2, 4, 6, 8, 10]
```
using List Comprehension
```python
#Using List Comprehension
evenno = [n for n in range(1, 11) if n%2==0]
print(evenno) #Output:[2, 4, 6, 8, 10]
```
## List Comprehension vs map
using map
```python
#Using map() function
l1 = map(lambda x:x*x,range(1, 11))
#Returns an iterator(map object)
print(l1)#Output:<map object at 0x00C0EC10>
print(list(l1))#Output:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
using List Comprehension
```python
#Using List Comprehension
l2 = [x*x for x in range(1, 11)]
print(l2)#Output:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
##  Nested loops in List Comprehension
```python
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = [num2 for num1 in l1 for num2 in num1]
print(l2) #Output:[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Multiple if condition in List Comprehension
```python
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
l2 = [n for n in l1 if n % 2 == 0 if n % 3 == 0]
print(l2)#Output:[6, 12]
```
## The expression can be tuple in List Comprehension
```python
a1 = ['red', 'green', 'blue']
b1 = [0, 1, 2]
a2 = [(a, b) for a in a1 for b in b1]
print(a2)#Output:[('red', 0), ('red', 1), ('red', 2), ('green', 0), ('green', 1), ('green', 2), ('blue', 0), ('blue', 1), ('blue', 2)]
```
### using ZIP function
```python
l1 = ['red', 'green', 'blue']
l2 = [0, 1, 2]
l3 = [(n1, n2) for n1, n2 in zip(l1, l2)]
print(l3)#Output:[('red', 0), ('green', 1), ('blue', 2)]
```
##  List comprehension can be used to call a method on each element.

```python
l1 = ["   a", "b  ", "  c  "]
l2 = [i.strip() for i in l1]
print(l2)#Output:['a', 'b', 'c']
```
## How to initialize 2d List with zeros with the help of list Comprehension

using for loop
```python
mylist = []
for i in range(3):
    mylist.append([])
    for j in range(3):
        mylist[-1].append(0)
print(mylist)
```
 **output**
 ```python
 [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
 ```

 using list Comprehension

 ```python
 mylist = [[0 for i in range(3)] for j in range(3)]
 ```
 **output**
 ```python
 [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
 ```
 ## If else in List Comprehension
 using for loop

```python
names = ['Brian', 'Linda', 'sharon', ‘James’, ‘Amanda’, ‘Billy’, ‘Thomas’, ‘Mampush’, ‘Linus’, ‘Harry’, ‘Bob’, ‘Brenda’, ‘Philbert’]

mylist = []
for n in names:
    if n[0] == 'B':
        mylist.append(n)
    else:
        mylist.append(0)
print(mylist)
```
**output**
```python
['Brian', 0, 0, 0, 0, 'Billy', 0, 0, 0, 0, 'Bob', 'Brenda', 0]
```

using List Comprehension
```python
mylist = [n if n[0] == 'B' else 0  for n in names]
print(mylist)
```
**output**
```python
['Brian', 0, 0, 0, 0, 'Billy', 0, 0, 0, 0, 'Bob', 'Brenda', 0]
```

## Can we use elif in List Comprehension

**Answer is NO**

List comprehension won’t take an elif statement, it will take multiple nested else statements.

**Example**

-The number if the number is not divisible by 3 or 5 <br>
-”fizz” if the number is divisible by 5 <br>
-”buzz” if the number is divisible by 3 <br>
-”fizzbuzz” if the number is divisible by 3 and 5

using for loop

```python
mylist = []
for x in range(1, 20):
    if x % 15 == 0:
        mylist.append('fizzbuzz')
    elif x % 5 == 0:
        mylist.append('fizz')
    elif x % 3 == 0:
        mylist.append('buzz')
    else:
        mylist.append(x)

# Output
[1, 2, 'buzz', 4, 'fizz', 'buzz', 7, 8, 'buzz', 'fizz', 11, 'buzz', 13, 14, 'fizzbuzz', 16, 17, 'buzz', 19]
```

using list Comprehension

```python
mylist = ['fizzbuzz' if x % 15 == 0 else 'fizz' if x % 5 == 0 else 'buzz' if x % 3 == 0 else x for x in range(1,20)]
# Output
[1, 2, 'buzz', 4, 'fizz', 'buzz', 7, 8, 'buzz', 'fizz', 11, 'buzz', 13, 14, 'fizzbuzz', 16, 17, 'buzz', 19]
```
## Set Comprehension
Like List comprehension, Python supports Set Comprehension also.
Set comprehension is written within curly braces {}

**Return Type: Set**

**Syntax:**
```python
{expression for item in iterable if conditional}
```
## How to find even numbers using set Comprehension:

```python
s1 = {n for n in range(1, 11) if n % 2 == 0}
print(s1) #Output:{2, 4, 6, 8, 10}
```
## How to find the square of numbers using Set Comprehension.
```python
s1 = {n*n for n in range(1, 11)}
#Sets are unordered.
print(s1) #Output: {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
```

## Let see a fizz buzz question in set

```python
myset = {'fizzbuzz' if x % 15 == 0 else 'fizz' if x % 5 == 0 else 'buzz' if x % 3 == 0    else x for x in range(1, 20)}

print(myset)
```
### What happening let's see

```python
{1, 2, 4, 'fizz', 7, 8, 11, 13, 14, 'fizzbuzz', 16, 17, 'buzz', 19}
```
## Dictionary Comprehension
Like List and Set comprehension, Python supports Dictionary Comprehension.

A dict comprehension, in contrast, to list and set comprehensions, needs two expressions separated with a colon followed by the usual “for” and “if” clauses

**Return Type: dict**

**Syntax:-**

```python
{key: value for (key,value) in iterable if conditional}
```
## How to find the square of numbers using Dictionary Comprehension.

```python
d1 = {n: n*n for n in range(1, 11)}
print(d1) #Output:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```
## If Condition in Dictionary Comprehension:

```python
d = {n: n*n for n in range(1, 11) if n % 2 == 0}
print(d)#Output:{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
print(type(d))#Output:<class 'dict'>
```
## Finding the number of occurrences using dictionary comprehension:
```python
#finding the number of occurrences of each character in the string
s="dictionary"
d={n:s.count(n) for n in s}
print (d)#Output:{'d': 1, 'i': 2, 'c': 1, 't': 1, 'o': 1, 'n': 1, 'a': 1, 'r': 1, 'y': 1}
```

## How to make 2d dictionary

using for loop

```python
mylist = {}
for i in range(3):
    mylist[i] = {}
    for j in range(3):
        mylist[i][j] = j*j
print(mylist)
```
**output**
```python
{0: {0: 0, 1: 1, 2: 4}, 1: {0: 0, 1: 1, 2: 4}, 2: {0: 0, 1: 1, 2: 4}}
```

using dict comprehension

```python
mylist = {j: {i: i*i for i in range(3)} for j in range(3)}
print(mylist)
```
**output**
```python
{0: {0: 0, 1: 1, 2: 4}, 1: {0: 0, 1: 1, 2: 4}, 2: {0: 0, 1: 1, 2: 4}}
```
