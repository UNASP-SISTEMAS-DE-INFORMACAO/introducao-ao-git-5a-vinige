from functools import reduce

array = [1,2,3,4,5,6]

def calculaSomaArray(num1,num2):
    """
    função
    """
    return num1+num2

soma = reduce(calculaSomaArray,array)

"""
for
"""
for(i in range(7)):
    print(array[i])

"""
 while
"""
cont=0
while(cont<len(array)):
    print(array[cont])
    cont=cont+1

print(soma)