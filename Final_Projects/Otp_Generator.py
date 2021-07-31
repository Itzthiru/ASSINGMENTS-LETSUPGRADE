'''PROJECT------THIRUMURUGAN B'''

'''OTP GENERATOR'''


import  random
import string as str

#maximum length of otp
max_length = 6

OTP = ''
char = str.ascii_letters + str.digits
for i in range(max_length):
    OTP = OTP+random.choice(char)

print('One Time Password Is:',OTP)