"""
Nombres:
    - Samuel Alejandro Jimenez Ramirez - 202116652
    - Carlos Manuel Muñoz Almeida - 202
    - Sebastian Murcia Gómez - 202
"""

from sys import stdin

def casosPosibles(p : int, r : int, m : int, array)-> int:
    print('piedras: ', p)
    print('ranas: ', r)
    print('movimientos: ', m)
    print('array: ', array)
    return 0

def main(): 
    numberOfCases = int(stdin.readline())
    for case in range(numberOfCases):
        line = stdin.readline().split(" ")
        p = int(line[0])
        r = int(line[1])
        m = int(line[2])
        array = [char for char in line[3][:-1]]
        print(casosPosibles(p,r,m,array))



if __name__ == '__main__':
    main()