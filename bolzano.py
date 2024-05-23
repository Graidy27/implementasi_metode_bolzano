import matplotlib.pyplot as plt
import numpy as np
types = {
    "0": "polynomial",
    "1": "logarithm",
    "2": "exponent",
    "3": "trigometry",
    "4": "insert x1 and x2"
}
inBuffer = ""
part = ""
coefBuff = ""
powerBuff = ""
poly_dict = {}
log_dict = {}
exp_dict = {}
trig_dict = {"sin": 0, "cos": 0, "tan": 0, "sec": 0, "csc": 0, "cot": 0}
x1table = []
x2table = []
x3table = []
fx1table = []
fx2table = []
fx3table = []
# xroot = input("Please insert the root value = ")


def getPolynomial():
    print("Please input a pair of int. The first one is the coefficient and the second one is the power of x.")
    print('Example\n3x^2\t-> 3 2\n3\t-> 3 0\nExit\t-> ""')
    while True:
        inBuffer = input("Insert pair = ")  # read pair
        if inBuffer == "":  # if there's no pair, break
            break
        part = inBuffer.split()

        if len(part) != 2:  # missing power/coef/both
            print("Error: Invalid Input. Missing coefficient, power, or both.")
            continue
        try:    # input isn't a number
            coefBuff = float(part[0])
            powerBuff = float(part[1])
        except ValueError:
            print("Please insert a number")
            continue
        if powerBuff in poly_dict:  # adding coef
            poly_dict[powerBuff] = poly_dict[powerBuff] + coefBuff
        else:
            poly_dict[powerBuff] = coefBuff


def getLog():
    print("Format is as follow")
    print("coefficient: n\nbase: a\nn a")
    print("Example: 6 log(10) x -> 6 10")
    while True:
        inBuffer = input("Insert pair = ")  # read pair
        if inBuffer == "":  # if there's no pair, break
            break
        part = inBuffer.split()

        if len(part) != 2:  # missing power/coef/both
            print("Invalid input. Format is as follow")
            print("coefficient: n\nbase: a\nn a")
            print("Example: 6 * log(10) x -> 3 * 10\n6 ln x -> 3 e")
            continue
        try:    # input isn't a number
            coefBuff = float(part[0])
        except ValueError:
            print("Please insert a number for coefficient")
            continue
        powerBuff = part[1]     # base
        if powerBuff in log_dict:  # adding base
            log_dict[powerBuff] = log_dict[powerBuff] + coefBuff
        else:
            log_dict[powerBuff] = coefBuff


def getExp():
    print("Format is as follow")
    print("coefficient: n\nbase: a\nn a")
    print("Example: 3 * 10^x -> 3 10\n 2 * e^x -> 2 e")
    while True:
        inBuffer = input("Insert pair = ")  # read pair
        if inBuffer == "":  # if there's no pair, break
            break
        part = inBuffer.split()

        if len(part) != 2:  # missing power/coef/both
            print("Invalid input. Format is as follow")
            print("coefficient: n\nbase: a\nn a")
            print("Example: 3 * 10^x -> 3 10\n 2 * e^x -> 2 e")
            continue
        try:    # input isn't a number
            coefBuff = float(part[0])
        except ValueError:
            print("Please insert a number for coefficient")
            continue
        powerBuff = part[1]     # base
        if powerBuff in exp_dict:  # adding base
            exp_dict[powerBuff] = exp_dict[powerBuff] + coefBuff
        else:
            exp_dict[powerBuff] = coefBuff


def getTrig():
    print("Available option are as follow: sin, cos, tan, sec, csc, and cot\nFormat is as follow")
    print("coefficient: n\nfunction: f\nn f")
    print("Example\n5 * sin x\t-> 5 sin\n8 * cot x\t-> 8 cot")
    while True:
        inBuffer = input("Insert pair = ")  # read pair
        if inBuffer == "":  # if there's no pair, break
            break
        part = inBuffer.split()

        if len(part) != 2:  # missing power/coef/both
            print("Invalid input. Available option are as follow: sin, cos, tan, sec, csc, and cot\nFormat is as follow")
            print("coefficient: n\nfunction: f\nn f")
            print("Example: 5 * sin x -> 5 sin\n 8 * cot x -> 8 cot")
            continue
        try:    # input isn't a number
            coefBuff = float(part[0])
        except ValueError:
            print("Please insert a number for coefficient")
            continue
        powerBuff = part[1]     # function
        if powerBuff in trig_dict:  # adding function
            trig_dict[powerBuff] += coefBuff
        else:
            print("Please insert a sin, cos, tan, sec, csc, or cot as 2nd paramter")
            continue


functions = {
    "0": getPolynomial,
    "1": getLog,
    "2": getExp,
    "3": getTrig
}


def reviewFunc():
    print("Your function =  ", end="")
    printPlus = 0
    # -------------------------- Print All Poly Related ekspression --------------------------
    for power in sorted(poly_dict, reverse=True):  # print polynomial part
        if printPlus == 1:
            print(" ", end="+ ")
        else:
            printPlus = 1
        if (power != 0):
            print(f"{poly_dict[power]}x^{power}", end="")
        else:
            print(poly_dict[power], end="")
    # ----------------------------------------------------------------------------------------
    # -------------------------- Print All Log Related ekspression --------------------------
    for logExpression in log_dict:
        if printPlus == 1:
            print(" ", end="+ ")
        else:
            printPlus = 1
        print(f'{log_dict[logExpression]}', end="")
        print(f'* log({logExpression}) x', end="")
    # ----------------------------------------------------------------------------------------
    # -------------------------- Print All Exp Related ekspression --------------------------
    for expExpression in exp_dict:
        if printPlus == 1:
            print(" ", end="+ ")
        else:
            printPlus = 1
        print(f'{exp_dict[expExpression]} * {expExpression}^x', end="")
    # ----------------------------------------------------------------------------------------
    # -------------------------- Print All Trig Related ekspression --------------------------
    for trigExpression in trig_dict:
        if (trig_dict[trigExpression]):  # coef is not 0
            if printPlus == 1:
                print("", end=" + ")
            else:
                printPlus = 1
            print(f'{trig_dict[trigExpression]} * {trigExpression} x', end="")
    # ----------------------------------------------------------------------------------------


def calc(x):
    temp = 1
    fx = 0

    # ------------- Calculate Polynom -------------
    for type in poly_dict:
        temp = np.power(x, type)
        temp *= poly_dict[type]
        fx += temp
    # ---------------------------------------------
    # ------------ Calculate Logarithm ------------
    for logExpression in log_dict:
        temp = log_dict[logExpression]
        if (logExpression == "e"):
            temp *= np.log(np.e, x)            # log(base, x)
        else:
            temp *= np.log(int(logExpression), x)
        fx += temp
    # ---------------------------------------------
    # ------------- Calculate Exponent ------------
    for expExpression in exp_dict:
        temp = exp_dict[expExpression]
        if (expExpression == "e"):
            temp *= np.exp(x)            # exp(x) e^x
        else:
            temp *= np.power(int(expExpression), x)
        fx += temp
    # ---------------------------------------------
    # ----------- Calculate Trigonometry ----------
    fx += (trig_dict["sin"]*np.sin(x))
    fx += (trig_dict["cos"]*np.cos(x))
    fx += (trig_dict["tan"]*np.tan(x))
    try:
        if (trig_dict["sec"] != 0):
            fx += (trig_dict["sec"]/np.cos(x))
        if (trig_dict["csc"] != 0):
            fx += (trig_dict["csc"]/np.sin(x))
        if (trig_dict["cot"] != 0):
            fx += (trig_dict["cot"]/np.tan(x))
    except ZeroDivisionError:
        print("Error division by zero. Please input a new equation.")
        return
    # ---------------------------------------------
    return fx


def table(iter):
    print("\n\n---------------------- TABLE ----------------------")
    print("Iter\tx1\t\tx2\t\tx3\t\tf(x1)\t\tf(x2)\t\tf(x3)")
    for i in range(0, iter):
        print(i, end='\t')
        print(f'{x1table[i]:.7f}', end='\t')
        print(f'{x2table[i]:.7f}', end='\t')
        print(f'{x3table[i]:.7f}', end='\t')
        print(f'{fx1table[i]:.7f}', end='\t')
        print(f'{fx2table[i]:.7f}', end='\t')
        print(f'{fx3table[i]:.7f}', end='\t')
        print(" ")
    print(f'\nNilai pendekatan x3 = {x3table[iter-1]:.7f}')


def drawGraph(batas1, batas2):
    selisih = abs(batas1 - batas2)/15
    selisih = round(selisih, 2)

    # Generate x values
    if batas1 < batas2:
        # Generates 400 points from -10 to 10
        xtemp = np.linspace((batas1 - selisih), (batas2 + selisih), 400)

    # Compute y values
    ytemp = calc(xtemp)

    # Create the plot
    plt.plot(xtemp, ytemp, label='y = calc(x)')

    # x1
    plt.axvline(x=x1table[0], color='r', linestyle='--')
    plt.plot(x1table[0], fx1table[0], 'ro')
    plt.text(x1table[0], fx1table[0], f'x1',
             color='blue', verticalalignment='bottom')

    # x2
    plt.axvline(x=x2table[0], color='r', linestyle='--')
    plt.plot(x2table[0], fx2table[0], 'ro')
    plt.text(x2table[0], fx2table[0], f'x2', color='blue',
             verticalalignment='bottom')

    # Add a vertical line for each x in iteration
    for i, xVal in enumerate(x3table, start=3):
        yVal = calc(xVal)
        plt.axvline(x=xVal, color='r', linestyle='--')

        # Add a point where the line intersects the graph
        plt.plot(xVal, yVal, 'ro')
        if i < 5:
            plt.text(xVal, yVal, f'x{i}', color='blue',
                     verticalalignment='bottom')  # Add the label
    # Add a horizontal line at y=0
    plt.axhline(y=0, color='black', linestyle='-')

    # Add labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of the function')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()


def bolzano(x1, x2):
    funct = {"x1": round(calc(x1), 7),
             "x2": round(calc(x2), 7),
             "x3": 0.0000
             }
    iter = 0
    if funct["x1"] * funct["x2"] > 0:
        print(f"f(x1) = {funct['x1']}\nf(x2) = {funct['x2']}")
        print("Because the y value have the same sign, there's no way to approximate to 0")
    while True:
        iter += 1
        x3 = (x1+x2)/2
        x3 = round(x3, 7)
        funct["x3"] = round(calc(x3), 7)

        print(f"\n---- Iteration {iter} ----")
        print(f"x1 = {x1:.7f}")
        print(f"x2 = {x2:.7f}")
        print(f"x3 = {x3:.7f}")
        print(f"f(x1) = {funct['x1']:.7f}")
        print(f"f(x2) = {funct['x2']:.7f}")
        print(f"f(x3) = {funct['x3']:.7f}")

        x1table.append(x1)
        x2table.append(x2)
        x3table.append(x3)
        fx1table.append(funct["x1"])
        fx2table.append(funct["x2"])
        fx3table.append(funct["x3"])

        if (funct["x3"] == 0.0000000 or x1 == x3 or x2 == x3):
            break
        if (funct["x1"] * funct["x3"] > 0):
            funct["x1"] = funct["x3"]
            x1 = x3
        else:
            funct["x2"] = funct["x3"]
            x2 = x3
    table(iter)
    drawGraph(x1table[0], x2table[0])


def main():
    # read input
    print("Choose command..")
    while True:
        for type in types:
            print(type, ":", types[type])
        expression = input("Command = ")
        if (expression == "4"):
            break
        try:  # Handle the case where the key does not exist in the dictionary
            functions[expression]()
            print("Choose command..")
        except KeyError:
            print(f"Command '{expression}' is not valid..")
            print("Valid command..")
            continue
    reviewFunc()
    while True:
        try:
            x1 = float(input("\nInsert the value of x1 = "))
            break
        except ValueError:
            print("Input must be one number")
    while True:
        try:
            x2 = float(input("Insert the value of x2 = "))
            break
        except ValueError:
            print("Input must be one number")

    x1 = round(x1, 7)
    x2 = round(x2, 7)
    bolzano(x1, x2)


main()
