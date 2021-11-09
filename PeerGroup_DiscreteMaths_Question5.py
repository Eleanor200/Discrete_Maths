#n1 and n2 is to ask the user the number of elements he would like to have in his lists X and Y
n1 = int(input("length of list 1: "))
n2 = int(input("length of list 2: "))
#we then created empty list to hold values the user is going to input
X = []
Y = []
#line 8 to 13, ask the user to enter the different elemenst he would like to see in his list and then automatically store them in X and Y respectively
for i in range (n1):
    elements1 = int(input("enter elements of X: "))
    X.append(elements1)
for j in range (n2):
    elements2 = int(input("enter elements of Y: "))
    Y.append(elements2)
#line 15 and 16 simply prints out the different list X and Y
print(X)
print(Y)
#the code below simply performs the operation y|x and then gives the output
for i in X:
    for j in Y:
        if j % i == 0:
            print(True)
        else:
            print(False)
