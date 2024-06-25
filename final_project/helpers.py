import numpy as np                 # v 1.19.2
import matplotlib.pyplot as plt    # v 3.3.2
from sys import exit
import math


def grid(xmin, xmax, ymin, ymax):
    # Select length of axes and the space between tick labels
    xmin, xmax, ymin, ymax = xmin, xmax, ymin, ymax
    ticks_frequency = 1

    # Plot points
    fig, ax = plt.subplots(figsize=(10, 10))

    # Set identical scales for both axes
    ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

    # Set bottom and left spines as x and y axes of coordinate system
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Create 'x' and 'y' labels placed at the end of the axes
    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

    # Create custom major ticks to determine position of tick labels
    x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
    y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])

    # Create minor ticks placed at each integer to enable drawing of minor grid
    # lines: note that this has no effect in this example with ticks_frequency=1
    ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

    # Draw major and minor grid lines
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    # Draw arrows
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)


def promptParam(value):
    try:
        if abs(int(value)) > 25:
            exit("Sorry, but this calculator can handle parameters which have absolute value below 25 :(")
    except ValueError:
            exit("Please, enter an integer")
    return int(value)

def quadFunc(aP, bP, cP):
    print("==========================================================")
    # Assign quadratic function its values
    a = promptParam(aP)
    b = promptParam(bP)
    c = promptParam(cP)
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
    elif yZero >= 0:
        if pointedUp:
            yBorder = 2
            yBorderInter = abs(c) + 2
            grid(-xBorder, xBorder, -yBorder, yBorderInter)
        elif not pointedUp:
            yBorder = abs(yZero) + 2
            yBorderInter = abs(c) + 2
            grid(-xBorder, xBorder, -yBorderInter, yBorder)

    # Define the function
    if yZero == 0:
        x = np.arange(-(yInter+5), (yInter+5), 0.1)
    else:
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
    
    
def linearFunc(kP, bP):
    print("==========================================================")
    # Define k and b
    k = promptParam(kP)
    b = promptParam(bP)

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

def invFunc(kP):
    # Define k
    print("==========================================================")
    k = promptParam(kP)

    x = np.arange(-10, 10, 0.1)
    y = k/x

    grid(-10, 10, -10, 10)
    print(
        f"Function: y = {k}/x\n==========================================================")
    plt.title(f"Function: y = {k}/x\n\n")
    plt.plot(x, y)
    plt.show()
    
def cubicFunc(aP):
    print("==========================================================")
    a = promptParam(aP)
    x = np.arange(-10, 10, 0.1)
    y = a*(x**3)

    grid(-10, 10, -10, 10)
    print(
        f"Function: y = {a}x³\n==========================================================")
    plt.title(f"Function: y = {a}x³\n\n")
    plt.plot(x, y)
    plt.show()

