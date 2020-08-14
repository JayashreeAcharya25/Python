import math, random

def genOTP():
    #declare a variable to store digits
    digits = "0123456789"
    OTP = ""

    #length of OTP
    for i in range(6):
        OTP += digits[math.floor(random.random()*10)]
    return OTP
#display
if __name__ == "__main__":
    print("Your 6 digit OTP is :", genOTP())

