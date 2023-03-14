Algoritmo si_no_Anidado
	Definir genero Como Entero
	Definir edad Como Entero
	Escribir "Cual es su gernero.  1=Masculino, 2=Femenino"
	Leer genero
	Si genero =1 Entonces
		Escribir "Digite su edad"
		Leer edad
		Si edad >= 18 Entonces
			Escribir "Presta servicio Militar"
		SiNo
			Escribir "No presta servicio militar"
		Fin Si
	SiNo
		Escribir "No presta servicio militar"
	Fin Si
FinAlgoritmo
