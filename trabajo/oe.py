from datetime import date

class Nota:
    _contador_id = 0  # Variable de clase para llevar el seguimiento de los IDs de las notas
    
    def __init__(self, memo, tag=''):
        self.id = Nota._contador_id
        self.memo = memo
        self.tag = tag
        self.fecha_creacion = date.today()
        Nota._contador_id += 1
    
    def match(self, filtro):
        """Verifica si el filtro coincide con el memo o el tag."""
        return filtro in self.memo or filtro in self.tag

class Cuaderno:
    def __init__(self):
        self.notas = []
    
    def nueva_nota(self, memo, tag=''):
        """Crea una nueva nota y la añade al cuaderno."""
        self.notas.append(Nota(memo, tag))
    
    def modificar_memo(self, id_nota, memo):
        """Modifica el memo de una nota con el ID dado."""
        for nota in self.notas:
            if nota.id == id_nota:
                nota.memo = memo
                break
    
    def modificar_tag(self, id_nota, tag):
        """Modifica el tag de una nota con el ID dado."""
        for nota in self.notas:
            if nota.id == id_nota:
                nota.tag = tag
                break
    
    def buscar(self, filtro):
        """Busca notas que coincidan con el filtro."""
        return [nota for nota in self.notas if nota.match(filtro)]
    
    def buscar_nota_por_id(self, id_nota):
        """Encuentra una nota por su ID."""
        for nota in self.notas:
            if nota.id == id_nota:
                return nota
        print(f"Nota con id {id_nota} no encontrada.")
        return None
    
    def imprimir_notas(self):
        """Imprime todas las notas."""
        for nota in self.notas:
            print("ID de la Nota:", nota.id)
            print("Memo:", nota.memo)
            print("Tag:", nota.tag)
            print("Fecha de Creación:", nota.fecha_creacion)
            print()
    
    def imprimir_direcciones_memoria_notas(self):
        """Imprime las direcciones de memoria de todas las notas."""
        for nota in self.notas:
            print(nota)

# Prueba del programa
if __name__ == '__main__':
    cuaderno = Cuaderno()
    cuaderno.nueva_nota('Hola Mundo')
    cuaderno.nueva_nota('Hola Mundo otra vez')

    print('Imprimiendo todas las direcciones de memoria de las notas en el cuaderno:')
    cuaderno.imprimir_direcciones_memoria_notas()
    print('')

    print('cuaderno.notas[0].id: {}'.format(cuaderno.notas[0].id))
    print('cuaderno.notas[1].id: {}'.format(cuaderno.notas[1].id))
    print('cuaderno.notas[0].memo: {}'.format(cuaderno.notas[0].memo))
    print()

    print('Ejecutando cuaderno.buscar(\'Hola\'):')
    print('Imprimiendo todas las direcciones de memoria de las notas en el cuaderno con la cadena \'Hola\' en el memo o tag:')
    for nota in cuaderno.buscar('Hola'):
        print(nota)
    print('')

    print("Ejecutando cuaderno.modificar_memo(1, 'Hola Mundo Modificado')")
    cuaderno.modificar_memo(1, 'Hola Mundo Modificado')
    print('cuaderno.notas[1].memo: {}'.format(cuaderno.notas[1].memo))

    print("Ejecutando cuaderno.nueva_nota('Con tag', 'Pedro')")
    cuaderno.nueva_nota('Con tag', 'Pedro')
    print('Imprimiendo todas las direcciones de memoria de las notas en el cuaderno:')
    cuaderno.imprimir_direcciones_memoria_notas()
    print('')

    print("Ejecutando vars(cuaderno.notas[0])")
    print(vars(cuaderno.notas[0]))
    print()

    print("Ejecutando print(cuaderno.notas[2].tag)")
    print(cuaderno.notas[2].tag)

    print("Ejecutando cuaderno.buscar_nota_por_id(3)")
    nota1 = cuaderno.buscar_nota_por_id(3)
    print(nota1)
    print()

    print("Ejecutando cuaderno.buscar_nota_por_id(2)")
    nota2 = cuaderno.buscar_nota_por_id(2)
    print(vars(nota2))
    print()

    print("Ejecutando cuaderno.modificar_tag(2, 'Juan')")
    cuaderno.modificar_tag(2, 'Juan')
    print("Ejecutando print(cuaderno.notas[2].tag)")
    print(cuaderno.notas[2].tag)
    print()

    print('Imprimiendo todas las direcciones de memoria de las notas en el cuaderno:')
    cuaderno.imprimir_direcciones_memoria_notas()
    print('')

    print("Imprimiendo todas las notas iterando sobre el cuaderno y usando vars() para cada nota:")
    for nota in cuaderno.notas:
        print(vars(nota))
    print('')

    print('Imprimiendo todas las notas usando el método imprimir_notas():')
    cuaderno.imprimir_notas()
