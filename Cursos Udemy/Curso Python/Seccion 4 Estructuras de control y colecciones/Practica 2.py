'''Enunciado: debido a los excelentes resultados, el restaurante decide ampliar sus ofertas de acuerdo a la siguiente escala de consumo, ver la tabla. Determinar el monto del descuento, el importe del impuesto y el importe a pagar.
    Hasta 100 = 10%
    Mayor a 100 = 20%
    Mayor a 200 = 30%
'''


print('----Restaurante Delicious----')
print('='*30)
print('Ingrese el valor de consumo')
consumo = float(input())

if consumo<0:
    print('Error del sistema "No se permiten numeros negativos"')
else:
    if consumo<=100:
        descuento = '10%'
        costo = consumo*0.90
    else:
        if consumo>100 and consumo<200:
            descuento = '20%'
            costo = consumo*0.80
        else:
            if consumo>=200:
                descuento = '30%'
                costo = consumo*0.70 

    iva = costo*0.19


    print('----FACTURA DE VENTA----')
    print('='*30)
    print('Consumo inicial:',consumo)
    print('Descuento:',descuento)
    print('Valor a descontar:',consumo-costo)
    print('Valor con Descuento',costo)
    print('Importe del: 0.19%')
    print('Valor total a pagar:',costo+iva)
