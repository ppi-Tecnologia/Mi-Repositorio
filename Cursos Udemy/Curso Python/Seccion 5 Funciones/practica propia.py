def costototal(precio):
    iva = precio * 0.19
    subtotal = precio + iva
    return iva, subtotal

print("digite el valor de la cuenta:")
costo_inicial = int(input())
iva_total, total = costototal(costo_inicial)

print("El valor a pagar es:",total,", se le ha puesto el iva del 19% que corresponde a:",iva_total)
