'''ASSINGMENT SUBMISSON FOR DAY-2------THIRUMURUGAN B'''
'''Delete all occurrences of an element in a list'''

'''METHOD_2'''


# creating an empty list
list = []

# number of elements as input
n = int(input("Enter number of elements in your list that you want to remove duplicates : "))

# iterating till the range
print("Enter Elements one by one")
for i in range(0, n):
    ele = str(input())
    # adding the element
    list.append(ele)


# to remove duplicated
# from list
result = []
for i in list:
    if i not in result:
        result.append(i)

result.sort(reverse=False)

print ("The original list is : " + str(list))

# printing list after removal of duplicate elements
print ("The list after removing duplicates from list: ",result)

