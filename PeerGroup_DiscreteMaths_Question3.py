#creating two different list that will store the values the user inputs
def lists():
    A = list(input("Enter elements for set A"))
    B = list(input("Enter elements for set B"))
    #condition to check if B is a subset of A and this checks for all elements in A and B
    if all(i in A for i in B):
        print("B is a subset of A")
    else:
        print("B is not a subset of A")
    C = []
    #this is to find the difference between A and B and then saving them into C which is an empty list
    for items in A:
        if items not in B:
            C.append(items)
    print(f"A-B= {C}")
    #this code is to find the cross product between A and B
    cross_product = [[x, y] for x in A for y in B]
    print(f"AXB= {cross_product}")


lists()