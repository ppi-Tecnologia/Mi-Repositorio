class Figura(object):
    nombre = None
    def __init__(self, nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        pass
    
class Rectangulo(Figura):
    base = None
    altura = None
    
    def __init__(self, nombre, base, altura):
        #self.nombre = __class__.__name__ Esto me deja en el atributo nombre el nombre de la clase
        Figura.__init__(self, nombre)
        self.base = base
        self.altura = altura
        
    def set_base(self, base):
        self.base = base
        
    def get_base(self):
        return self.base
    
    def set_altura(self, altura):
        self.altura = altura
        
    def get_altura(self):
        return self.altura
        
    def calcular_area(self):
        area = self.base * self.altura
        return area

    def calcular_perimetro(self):
        perimetro = (self.base*2) + (self.altura*2)
        return perimetro
        
class Circulo(Figura):
    radio = None
    
    def __init__(self, nombre, radio):
        Figura.__init__(self, nombre)
        self.radio = radio
        
    def set_radio(self, radio):
        self.radio = radio
        
    def get_radio(self):
        return self.radio
        
    def calcular_area(self):
        pi = 3.1415
        area = pi*self.radio**2
        return area
    
    def calcular_perimetro(self):
        perimetro = self.radio*2
        return perimetro
    
def probar_figura(objeto):
    print(f'Area: {objeto.calcular_area()}')
    print(f'Perimetro: {objeto.calcular_perimetro()}')
    #Rectangulo.calcular_area()
    #Rectangulo.calcular_perimetro()
    #print(f'{objeto.get_nombre()}, Base: {objeto.get_base()}, Altura: {objeto.get_altura()}')