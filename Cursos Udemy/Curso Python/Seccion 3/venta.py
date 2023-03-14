"""Calcular Precio de venta"""
"""Enucnciadp: dado el valor de la venta de productos, hallar el IGV(18%) y el precio de venta."""
"""Analisis: ´para la solucion de este problema sse requiere que el usuario ingrese el valor de venta del producto y el sistema realice el calculo respectivo para hallar el IGV y el precio de venta, para esto use la siguiente expresion."""
"""igv = vv* 0.18"""
"""pv = vv + igv"""
print("----Calculo de venta----")
print("Ingrese el valor de la venta")
vv = float(input())
print('='*25)
igv = vv * 0.18
print("----Factura de venta----")
print('='*25)
print("el valor de la venta es:",vv)
print("El IGV es:",igv)
print("Valor sin IGV", vv-igv)
print('='*25)
