Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import array as arr
>>> numbers=arr.array('i',[1,2,3])
>>> numbers.append(4)
>>> print(numbers)
array('i', [1, 2, 3, 4])
>>> numbers.extend([5,6,7])
>>> print(numbers)
array('i', [1, 2, 3, 4, 5, 6, 7])
>>> odd=arr.array('i',[1,3,5])
>>> even=arr.array('i',[2,4,6])
>>> numbers=arr.array('i')
>>> numbers= odd + even
>>> print(numbers)
array('i', [1, 3, 5, 2, 4, 6])
>>> 
