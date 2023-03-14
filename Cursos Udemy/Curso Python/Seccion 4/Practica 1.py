'''Enunciado: un restaurante ofrece un descuento del 10% para consumo de hasta s/. 100.00 y un descuento del 20 % para consumos mayores, para ambos casos se aplica un impuesto del 19%. Determinar el monto del descuento, el impuesto y el importe a pagar.

Análisis: para la solución de este problema, se requiere que el usuario ingrese el consumo y el sistema verifica y calcula el monto del descuento, el impuesto y el importe a pagar.
'''

print('----FACTURA DE VENTA----')
print('Cuanto costo la comida?')
costo = float(input())
if (costo<=100):
    valortotal = costo*0.90
else:
    if(costo>100):
        valortotal = costo*0.80
    else:
        if(costo<100):
            print("No puede ser un valor inferior a 0")
iva = valortotal*0.19
descuento = costo-valortotal
valortotal += iva
print('='*25)
print("Valor Inicial: ",costo)
print("Importe del 19%:",iva)
print("Descuento:",descuento)
print('Subtotal:',valortotal-iva)
print('Valor total con iva:',valortotal)