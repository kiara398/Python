Last login: Wed Dec  8 15:57:15 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
Freds-MacBook-Air:~ fredkwesiga$ python
Python 3.10.0 (v3.10.0:b494f5935c, Oct  4 2021, 14:59:20) [Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num, num1 = 20, 30
>>> ans = num + num1
>>> ans
50
>>> if num > num1 :
...    print(hello)
... 
>>> if num < num 1 :
  File "<stdin>", line 1
    if num < num 1 :
       ^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> if num < num1 :
... 
  File "<stdin>", line 2
    
    ^
IndentationError: expected an indented block after 'if' statement on line 1
>>> num, num1 - Null, 30
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Null' is not defined
>>> num, num1 = None, 30
>>> if num > num1 :
...    print (num)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'NoneType' and 'int'
>>>  if num < num1 :
  File "<stdin>", line 1
    if num < num1 :
IndentationError: unexpected indent
>>> for i in range(10):
...     print (i)
... 
0
1
2
3
4
5
6
7
8
9
>>> mylist=[1,2,3,4,5,6,7,,8]
  File "<stdin>", line 1
    mylist=[1,2,3,4,5,6,7,,8]
                          ^
SyntaxError: invalid syntax
>>> mylist=[1,2,3,4,5,6,7,8,]
>>> for i in mylist :
...     print (i)
... 
1
2
3
4
5
6
7
8
>>> for i in mylist :
...     if i%2==0 :
...     print i
  File "<stdin>", line 3
    print i
    ^
IndentationError: expected an indented block after 'if' statement on line 2
>>> for i in mylist :
...     if i%2==0 :
...        print i
  File "<stdin>", line 3
    print i
    ^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> for i in mylist :
...     if i%2==0 :
...        print (i)
... 
2
4
6
8
>>> for i in mylist :
...     if i%2 is not 0 :
...        print (i)
... 
<stdin>:2: SyntaxWarning: "is not" with a literal. Did you mean "!="?
1
3
5
7
>>> for i in mylist :
...     if i%2 != 0 :
...        print (i)
... 
1
3
5
7
>>> 
