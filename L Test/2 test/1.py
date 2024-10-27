'''
3) Remove Duplicates from a List (3 ქულა)
Create a program that receives a list and removes duplicate elements while maintaining the original order.
Examples:
[1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']
'''

def remove_dupe(b):
    a = []
    for i in b:
        if i not in a:
            a.append(i)
    print(a)
    
remove_dupe([1,2,3,3,4,4])