import matplotlib.pyplot as plt
import numpy as np
import math
from helpers import grid, promptParam
from sys import exit

print("==========================================================\n Welcome to Archil's graph plotter!")
print("==========================================================")
print("1. y = ax²+bx+c | Quadratic function")
print("2. y = kx + b   | Linear function")
print("3. y = k/x      | Inverse variation")
print("4. y = ax³      | Cubic function")
try:
    case = int(input("Select function type via its ID: "))
except ValueError:
    print("Try again! Make sure to enter an integer!")
    print("==========================================================")
    exit(1)
print("==========================================================")

# ============================== Case 1: Quadratic function ======================================
if case == 1:
    # Assign quadratic function its values
    a,b,c = 'a','b','c'
    a = promptParam(a)
    b = promptParam(b)
    c = promptParam(c)
    
    a, b, c = int(a), int(b), int(c)
    if a == 0:
        exit("a parameter can not equal 0, since function may not be valid")
    if a > 0:
        pointedUp = True
    else:
        pointedUp = False
    hasXInter = True
    hasYInter = True
    xInter = [1, 5]
    xZero = (-b)/(2*a)
    yZero = (4*a*c-b**2)/(4*a)

    # Get values for possible X-intercept via f(x)=0:
    try:
        xInter = [(-b + math.sqrt(b**2 - 4*a*c))/(2*a),
                  (-b - math.sqrt(b**2 - 4*a*c))/(2*a)]
    except ValueError:
        hasXInter = False
        print("No X intercept")
    # Get value of possible Y-intercept
    if b == 0:
        hasYInter = False
    else:
        yInter = c

    if abs(xInter[0]) < abs(xInter[1]):
        xBorder = abs(xInter[1]) + 2
    else:
        xBorder = abs(xInter[0]) + 2
    if hasYInter:
        yBorder = abs(yInter) + 2
    else:
        yBorder = xBorder
        
    if yZero < 0:
        if pointedUp:
            yBorder = round(abs(yZero) + 2)
            yBorderInter = abs(c) + 2
            grid(-xBorder, xBorder, -yBorder, yBorderInter)
        if not pointedUp:
            yBorder = 2
            yBorderInter = abs(c) + 2
            grid(-xBorder, xBorder, -yBorderInter, yBorder)
    elif yZero > 0:
        if pointedUp:
            yBorder = 2
            yBorderInter = abs(c) + 2
            grid(-xBorder, xBorder, -yBorder, yBorderInter)
        elif not pointedUp:
            yBorder = abs(yZero) + 2
            yBorderInter = abs(c) + 2
            grid(-xBorder, xBorder, -yBorderInter, yBorder)

    # Define the function
    x = np.arange(-xBorder, xBorder, 0.1)
    y = a*(x**2)+b*x+c

    # Plot the function
    plt.plot(x, y)

    # If statements to represent the function in a readable way:
    wrtA = a
    wrtB = b
    wrtC = c
    if True:
        if b > 0:
            wrtB = f"+{b}"
        if b == 1:
            wrtB = ""
        if b == -1:
            wrtB = "-"
        if c > 0:
            wrtC = f"+{c}"
        if a == 1:
            wrtA = ""
        if a == -1:
            wrtA = "-"
    plt.title(f"Function: {wrtA}x²{wrtB}x{wrtC}\n\n")

    # Print starting coordinate of the parrabola:
    print(
        f"Function: {wrtA}x²{wrtB}x{wrtC}\n----------------------------------------------------------\nZEROES: \n")
    print(f"X zero: {xZero}")
    print(f"Y zero: {yZero}")
    print("----------------------------------------------------------\nINTERCEPTS: \n")

    # Print X intercepts if function has them:
    if hasXInter:
        print(f"X intercepts: {xInter[0]}, {xInter[1]}")

    # If function is a full square (i.e. [x+2]^2):
    if xInter[0] == xInter[1]:
        hasXInter = False
        print("No X intercept")

    # Print Y intercept in case function has any:
    if hasYInter:
        print(f"Y intercept: {yInter}")
    # If function does not have b parameter (i.e. [x^2 + c])
    if b == 0:
        hasYInter = False
        print("No Y intercept")
    print("==========================================================")

    plt.show()

# ==================================  Case 2: y = kx + b  ===============================================
if case == 2:
    # Define k and b
    k,b = 'k','b'
    k = promptParam(k)
    b = promptParam(b)

    wrtK = k
    wrtB = b
    if True:
        if k == 1:
            wrtK = ""
        if k == -1:
            wrtK = "-"
        if b > 0:
            wrtB = f"+{b}"
        if b == 0:
            wrtB = ""

    xInter = -b/k
    yInter = float(b)
    print(
        f"Function: {wrtK}x{wrtB}\n----------------------------------------------------------\nINTERCEPTS: \n")
    print(f"X intercept: {xInter}")
    print(f"Y intercept: {yInter}")
    print("==========================================================")

    x = np.arange(-10, 10, 0.1)
    y = k*x+b

    xBorder = abs(xInter) + 1
    yBorder = abs(yInter) + 1
    grid(-xBorder, xBorder, -yBorder, yBorder)
    plt.title(f"Function: {wrtK}x{wrtB}\n\n")
    plt.plot(x, y)

    plt.show()

# ==================================  Case 3: y = k/x ===============================================

if case == 3:
    # Define k
    k = 'k'
    k = promptParam(k)

    x = np.arange(-10, 10, 0.1)
    y = k/x

    grid(-10, 10, -10, 10)
    print(
        f"Function: y = {k}/x\n==========================================================")
    plt.title(f"Function: y = {k}/x\n\n")
    plt.plot(x, y)
    plt.show()

# ==================================  Case 4: y = ax³ ===============================================

if case == 4:
    a = 'a'
    a = promptParam(a)
    x = np.arange(-10, 10, 0.1)
    y = a*x**3

    grid(-10, 10, -10, 10)
    print(
        f"Function: y = {a}/x\n==========================================================")
    plt.title(f"Function: y = {a}/x\n\n")
    plt.plot(x, y)
    plt.show()

# ===================================================================================================

