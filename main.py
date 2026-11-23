def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

print(addition(4, 2))
print(soustraction(4, 2))
def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b