def inputNumber(variableName):
    check = False
    while check != True:
        inp = input(f"Введите значение {variableName}= ")
        try:
            res = float(inp)
            check = True
        except ValueError:
            print(f"Введённое значение \"{inp}\" не является числом!")
    return res

a = inputNumber("a")
b = inputNumber("b")
c = inputNumber("c")

value = round((a + b**3) / (1 + c**2))
print(f"Ответ: {value}")

value = (a + b**3) / (1 + c**2)
print(f"Ответ: {value}")

print(f"Ответ: (a + b^3) / (1 + c^2) = {value}")

print(f"Ответ: ({a} + {b}^3) / (1 + {c}^2) = {value}")



