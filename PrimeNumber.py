#finding prime number
for num in range(3,20):
    for i in range(2,num):
        if num%i==0:
            j=num/i
            print "%d = %d * %d" % (num,i,j)
            break
    else:
        print "%d Number is prime number" % (num)
