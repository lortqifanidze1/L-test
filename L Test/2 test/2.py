'''
4) Factorial Calculation (3 ქულა)
Create a program that receives a non-negative integer and returns its factorial. The factorial of a number 
n is the product of all positive integers from 1 to n. By definition, the factorial of 0 is 1.
'''







def paqroti_tu_ramcxa(a):
    if a == 0:
        print(1)
    elif a == 1:
        print(1)
    j = 1
    for i in range(1 , a + 1):
        j  = j * i 
        print(j)
paqroti_tu_ramcxa(5)



