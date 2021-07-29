'''ASSINGMENT SUBMISSON FOR DAY-2------THIRUMURUGAN B'''
'''Delete all occurrences of an element in a list'''

'''METHOD_1'''

# removing all duplicate elements from list
# initializing list


list = [1, 2, 3, 4, 5, 6, 7, 6, 3, 5, 6, 1, 8, 9, 10, 11, 12, 13, 7]
print ("The original list is : " + str(list))


# to remove duplicated
# from list
result = []
for i in list:
    if i not in result:
        result.append(i)

# printing list after removal of duplicate elements
print ("The list after removing duplicates from list: " + str(result))





