import hashlib
data= input("enter the data:")
encryption= hashlib.md5(data.encode()).hexdigest()
print(encryption)
