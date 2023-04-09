from persona import Cliente, Empleado

#cliente1 = Cliente('Javier', 34)
#cliente2 = Cliente('Gilberto', 77)
#cliente1.detalle_persona()
#print(cliente2)

empleado1 = Empleado('Alex', 25, 1160000)
empleado2 = Empleado('Roel', 25, 1300000)

empleado1.detalle_persona()
empleado1.detalle_empleador()

print(empleado2)