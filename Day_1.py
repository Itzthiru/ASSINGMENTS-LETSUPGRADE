'''ASSINGMENT SUBMISSON FOR DAY-1------THIRUMURUGAN B'''
'''python program for Get input from user and sort a list in descending order'''


# creating an empty list
list = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range\
print("Enter Data")
for i in range(0, n):
    ele = str(input())
    # adding the element
    list.append(ele)

#sort a list in descending order using sort

des_list = list.sort(reverse = True)

print('INPUT FROM YOU =',list)
print("LIST IN DESCENDING ORDER=",des_list)



