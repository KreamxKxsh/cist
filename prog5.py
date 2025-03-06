def main():
    n1, n2 = getNum()
    addSum = addNum(n1, n2)
    subSum = subNum(n1, n2)
    divSum = divNum(n1, n2)
    multSum = multNum(n1, n2)
    print(f"The two numbers Added equal {addSum}.")
    print(f"The two numbers Subtracted equal {subSum}.")
    print(f"The two numbers Divided equal {divSum}.")
    print(f"The two numbers Multiplied equal {multSum}.")


def getNum():
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Please enter your first number: "))
    return(num1, num2)

def addNum(x, y):    
    return(x + y)

def subNum(x, y):
    return(x - y)    

def divNum(x, y):
    return(x / y)

def multNum(x, y):
    return(x * y)

main()