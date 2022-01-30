'''
Input : an integer value
Output : all its prime fators
'''

def primeFactors(number):
    list = []
    i = 2
    while(number >= i):
        if(number % i == 0):
            list.append(i)
            number = number // i
        else:
            i = i + 1
    return list
