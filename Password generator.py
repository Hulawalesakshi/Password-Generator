import sys
import random
import string
import time

def password(late,low,up,let,digg,symm):

    aw=up+low+digg+let+symm
    xb=random.sample(aw,lenh) # pass2 argument 1=str , 2=length
    random.shuffle(xb)
    
    yp="".join(xb)
    return yp

while True:
    san=input("Are you ready for play (Y/N)? \n")
    if(san=="Y" or san=="y"):

        lenh=int(input("enter the length: "))

        low=string.ascii_lowercase # abcd..z
        up=string.ascii_uppercase
        let=string.ascii_letters
        digg=string.digits
        symm=string.punctuation

        hole=password(lenh,low,up,let,digg,symm)
        time.sleep(1)
        print("....\n..generating..")
        time.sleep(1)
        print("password: "+hole)

    elif(san=="N" or san=="n"):
        print("thanks :)")
        sys.exit()