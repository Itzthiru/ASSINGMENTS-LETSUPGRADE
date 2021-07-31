'''PROJECT(celsius to fahrenhiet convertion)------THIRUMURUGAN B'''

'''Develop a python based degree converter which takes °C value and give you output of °F '''

#getting input from user
celsius = float(input("Enter °C Value: "))

#converting °C value to °F
fahrenheit = (celsius * 9/5) + 32

#displaying the Equivalent °F value
print('Equivalent Value in °F is :',fahrenheit)