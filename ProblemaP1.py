"""
Nombres:
    - Samuel Alejandro Jimenez Ramirez - 202116652
    - Carlos Manuel Muñoz Almeida - 202
    - Sebastian Murcia Gómez - 202015229
"""

from sys import stdin

def casosPosibles(p : int, r : int, m : int, array:list)-> int:
    print('piedras: ', p)
    print('ranas: ', r)
    print('movimientos: ', m)
    print('array: ', array)

    indice= 0

    # Verificar si se puede mover a la izquierda
    if array[indice]==0:
        pIzquierda= 0
    else: 
        if indice==0:
            pIzquierda= array[indice]
        else: 
            pIzquierda= array[indice]-array[indice-1]-1

    # Verificar si se puede mover a la derecha
    if array[indice]==p-1 or (indice<r-1 and array[indice+1]-array[indice]==1):
        pDerecha= 0
    elif indice==r-1:
        pDerecha= p-array[indice]-1
    else:
        pDerecha= array[indice+1]-array[indice]-1




    return 0

casosPosibles(4,2,2,[0,2])
#1010

def main(): 
    numberOfCases = int(stdin.readline())
    for case in range(numberOfCases):
        line = stdin.readline().split(" ")
        p = int(line[0])
        r = int(line[1])
        m = int(line[2])
        # array = [char for char in line[3][:-1]]
        print(casosPosibles(p,r,m, toList(line[3])))


def toList(d:str="rprp"):
    l= []
    i= d.find("r")
    while i!=-1: 
        l.append(i)
        i= d.find("r", i+1)
    return l




if __name__ == '__main__':
    # main()
    pass