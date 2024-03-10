import timeit

# Ejercicio 1: Reescribe el método myUnsolvedMystery de manera recursiva
def myUnsolvedMystery_iterative(z):
    x = 0
    for i in range(z, 0, -1):
        x += i
    return x

def myUnsolvedMystery_recursive(z):
    if z == 0:
        return 0
    else:
        return z + myUnsolvedMystery_recursive(z - 1)

print("Funcion iterativa:")
print(timeit.timeit("myUnsolvedMystery_iterative(6)", globals=globals(), number=10000000))
print(myUnsolvedMystery_iterative(6))
print("Funcion recursiva")
print(timeit.timeit("myUnsolvedMystery_recursive(6)", globals=globals(), number=10000000))
print(myUnsolvedMystery_recursive(6))

