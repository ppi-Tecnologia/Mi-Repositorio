from collections import deque  # Libreria para trabajar con colas

# PRIMERO EN ENTRAR, PRIMERO EN SALIR

cola = deque(['Juan', 'David', 'Castrillon', 'Villa'])

cola.append('Usuga')  # agregue el elemento 'Usuga' Al final de la Cola

cola.popleft() # elimine el elemento 'Juan' de la Cola

print(cola)

