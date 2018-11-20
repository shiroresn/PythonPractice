import Sum

def calc(a,b,o):
    if o=='+':
        return Sum.sum(a,b)
    elif o=='-':
        return a-b
    elif o=='*':
        return a*b
    elif o=='/':
        return a/b
    else:
        return "invalid input"

calc (5,10,'+')
print(calc (5,10,'-'))
print(calc (5,10,'*'))
print(calc (5,10,'/'))
