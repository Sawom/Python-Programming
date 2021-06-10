nm = int(input("Enter a number : "))

def multiplicationTable(nm):
    m=1
    for i in range(10):
        print(nm, " X ",m , "=", m*nm)
        m=m+1

multiplicationTable(nm)