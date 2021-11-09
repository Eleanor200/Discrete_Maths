n = int(input("length of the list: "))
list = []
for i in range (n):
    elements = input("enter the elements:")
    list.append(elements)
newSet = set(list)
if len(list) == len(set(list)):
    print("True, the set is", newSet)
else:
    print("False, the set should be", newSet)







