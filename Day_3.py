'''ASSINGMENT SUBMISSON FOR DAY-3------THIRUMURUGAN B'''

'''Take input for the gift_presented_to[] list and print its respective gift_received_from[] list.'''

# creating an empty list
gift_presented_to = []

# iterating till the range
print("Enter persons one by one")
for i in range(0, 5):
    ele = str(input())
    # adding the element
    gift_presented_to.append(ele)

#updating names in gift_received_from
gift_received_from = []

gift_received_from.append(gift_presented_to[0])
gift_received_from.append(gift_presented_to[1])
gift_received_from.append(gift_presented_to[4])
gift_received_from.append(gift_presented_to[2])
gift_received_from.append(gift_presented_to[3])

#printing both gift_presented_to and gift_received_from

print('Gift presented to =',gift_presented_to)
print("Gift received from",gift_received_from)