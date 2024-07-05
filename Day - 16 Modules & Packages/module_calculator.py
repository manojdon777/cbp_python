def add(var1, var2):
    print('I am mosudle with add functionality')
    return var1 + var2

def sub(var1, var2):
    return var1 - var2

def mul(var1, var2):
    return var1 * var2

def div(var1, var2):
    return var1 / var2



if __name__ == '__main__':
    print('Below are function testing calls')
    print('Addition is =', add(22,55))
    print('Substraction is =', sub(22,55))
    print('Multiplication is =', mul(22,55))
    print('Division is =', div(22,55))

