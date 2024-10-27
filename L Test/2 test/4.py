'''
7) Fibonacci Sequence Generator (4 ქულა)
Create a program that receives an integer n and returns the first n numbers in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
Examples:
5 --> [0, 1, 1, 2, 3]
7 --> [0, 1, 1, 2, 3, 5, 8]
'''
def jj(n):
    if n == 0:
        print([])
    elif n == 1:
        print([0])
    else:
        print([0 , 1])
    sb = [0 , 1]
    
    for i in range(2 , n):
        has = sb[-1] + sb[-2]
        sb.append(has)
    print(sb[:n]) 
jj(9) # boloriscxvi daikidet 