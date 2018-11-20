name = input("Enter Name : ")
mobile = input("Enter Mobile Number : ")
age = input("Enter Age : ")
address = input("Enter Your Address : ")

info = str(name+","+mobile+","+age+","+address)

fo = open(name+".txt","")

fo.write(info)
fo.close()
