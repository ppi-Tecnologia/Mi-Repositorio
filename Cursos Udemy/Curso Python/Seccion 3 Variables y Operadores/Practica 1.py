"""Calcular cociente y residuo"""
"""Enunciado: Hallar el cociente y residuo (resto) de dos numeros enteros"""
"""Analisis: Para la solucion de este problema, se requiere que el usuario ingrese dos numeros enteros y el sistema realice el calculo respectivo para hallar el cociente  y residuo."""

print("Ingrese el primer numero")
num1 = int(input())
print("Ingrese el segundo numero")
num2 = int(input())
cociente = num1/num2
print("Cociente:",cociente)
residuo = num1%num2
print("Residuo:",residuo)
cocienteEntero = num1//num2
print("Cociente Entero",cocienteEntero)