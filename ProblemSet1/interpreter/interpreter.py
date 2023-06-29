userInput = input("Expression: ")

x, y, z = userInput.split(" ")

if y == "+":
    result = (float(x) + float(z))
    rounded = round(result, 1)
    print(rounded)

elif y == "-":
    result = (float(x) - float(z))
    rounded = round(result, 1)
    print(rounded)

elif y == "*":
    result = (float(x) * float(z))
    rounded = round(result, 1)
    print(rounded)

elif y == "/":
    result = (float(x) / float(z))
    rounded = round(result, 1)
    print(rounded)