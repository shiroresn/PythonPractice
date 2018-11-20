#finding prime number
number = input("Enter Number : ")
for num in range(3,int(number)):
    for i in range(2,num):
        if num%i==0:
            j=num/i
            print(num,"=",i,"+",j)
            break
    else:
        print ("%d Number is prime number" , num)
