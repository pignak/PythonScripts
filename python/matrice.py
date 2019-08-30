import numpy as np

def sommaForEach(a):
    sum=0
    for row in a:
        for elem in row:
           sum+=elem
    print(sum)

def sommaElem(a):
    for i in range(2):
        for j in range(2):
            print(a[i][j])

def contaRighe(m):
    print("il numero di righe è ", len(m))
    return len(m)

def contaColonne(m):
    print("il numero di colonne è ",len(m[0]))
    return len(m[0])

def numeroCol(m):
    print("numero colonne e righe ", np.shape(m))
    return  np.shape(m)

m=([1,2],
   [3,4],
   [5,6]
   )

print("---1---")
sommaForEach(m)
print("---2---")
sommaElem(m)
print("---3---")
r=contaRighe(m)
print("---4---")
c=contaColonne(m)
print("---5---")
r1,c1=numeroCol(m)
print("------")
print(r1,c1)
print("------")