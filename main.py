def divide(ourDividend , OurDivisor):
    sign = (-1 if(9(ourDividend < 0)^(OurDivisor<0))else 1)
    ourDividend = abs(ourDividend)
    ourDivisor = abs(ourDivisor)
    quotientNumber = 0
    tempNumber = 0
    for i in range(31, -1, -1):
        if (tempNumber + (ourDivisor << i) <= ourDividend):
            tempNumber += ourDivisor << i
            quotientNumber |= 1 << i
    if sign ==- 1:
        quotientNumber=-quotientNumber
    return quotientNumber
a = input("Enter a for a/b : ")
b = input("Enter b for a/b : ")
print("Result of",a,"/",b,"is",divide(a,b))
    