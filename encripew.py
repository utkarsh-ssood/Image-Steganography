import cv2
import os
import string

img=cv2.imread("img1.jpg")
msg=input("Enter the secret message: ")
password=input("Enter password: ")

d={}
c={}

for i in range(255):
    d[chr(i)]=i
# chr character
    c[i]=chr(i)  

def encrypt_image():
    m=0 # row
    n=0 # column
    z=0 

    for i in range(len(msg)):
        img[n,m,z]=d[msg[i]]
        n+=1
        m+=1
        z=(z+1)%3
        # because there are only three dimensions and only three layers are there
    return img

def decrypt_image():
    message=""
    m=0
    n=0
    z=0

    pas=input("Enter password for Decryption: ")
    if password==pas:
        for i in range(len(msg)):
            message=message+c[img[m,n,z]]
            n+=1
            m+=1
            z=(z+1)%3

        print("Decrypted message: ",message)
    else:
        print("You are not authenticated!!")



img=encrypt_image()
cv2.imwrite("encryptedimg.jpg",img)
os.startfile("encryptedimg.jpg")
decrypt_image()
