def printline(str):
    print(str)

printline("Hello India!")



def fact(ans,x):

    if x==1:
        print(ans)
    else:
        ans = ans*x
        x=x-1
        fact(ans,x)


fact(1,5)
