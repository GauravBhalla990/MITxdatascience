def f(x):
    return (x+15)**0.5 + x**0.5 == 15

def solveit(test):
    # base case
    if test(0):
        return 0
    solved = False
    xneg = -1
    xpos = 1
    while(not(solved)):
        if test(xpos):
            solved = True
            return xpos
        elif test(xneg):
            solved = True
            return xneg
        xneg -= 1
        xpos += 1


print(solveit(f))