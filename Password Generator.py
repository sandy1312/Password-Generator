import string
import random
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation
pwd_len = int(input("Enter password length:"))
s=[]
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
random.shuffle(s)
print("Your password is:")
print("".join(s)[0:pwd_len])










