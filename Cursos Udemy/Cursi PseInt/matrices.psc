Algoritmo matrices
	Dimension matriz[3,3]
	contador = 1
	Para i<-1 Hasta 3 Con Paso 1 Hacer
		Para j<-1 Hasta 3 Con Paso 1 Hacer
			matriz[i,j] = contador
			contador = contador + 1
		Fin Para
	Fin Para
	
	Para i<-1 Hasta 3 Con Paso 1 Hacer
		Para j<-1 Hasta 3 Con Paso 1 Hacer
			Escribir matriz[i,j] Sin Saltar
		Fin Para
		Escribir ""
	Fin Para
FinAlgoritmo
