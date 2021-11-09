n1 = int(input("length of list 1: "))
n2 = int(input("length of list 2: "))
X = []
Y = []
for i in range (n1):
    elements1 = int(input("enter elements of X: "))
    X.append(elements1)
for j in range (n2):
    elements2 = int(input("enter elements of Y: "))
    Y.append(elements2)
print(X)
print(Y)

for i in X:
    for j in Y:
        if j % i == 0:
            print(True)
        else:
            print(False)
