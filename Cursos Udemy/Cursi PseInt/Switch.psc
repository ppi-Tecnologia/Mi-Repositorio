Algoritmo Switch
	Definir num1, num2, resultado Como Real
	Escribir "Escriba un numero"
	Leer num1
	Escribir "Escriba otro numero"
	Leer num2
	Escribir "Que desea hacer.   1=Sumar, 2=Restar, 3=Multiplicar, 4=Dividir"
	Leer numero
	Segun numero Hacer
		1:
			resultado = num1 + num2
			Escribir resultado
		2:
			resultado = num1 - num2
			Escribir resultado
		3:
			resultado = num1 * num2
			Escribir resultado
		4:
			resultado = num1 / num2
			Escribir resultado
		De Otro Modo:
			Escribir "Error"
	Fin Segun
FinAlgoritmo
