#The first line asking the user how many elements will be in his/her list. for example 3
n = int(input("length of the list: "))
#we then created an empty list which will store the elements the user inputs
list = []
for i in range (n):
    elements = input("enter the elements:")
    list.append(elements)
#we then created a set from the user's input and this will help to remove any duplicates
newSet = set(list)
#this condition is to check if there are equal number of elements in the list and set then print out the response
if len(list) == len(set(list)):
    print("True, the set is", newSet)
else:
    print("False, the set should be", newSet)







