from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class receta(ABC):
    def __init__(self, nombre, ingrediente, paso): # 2. Modifico las variables "n", "i" y "p" para que sean mas claros
        self.nombre = nombre  # 2. nombre
        self.ingrediente = ingrediente  # 2. ingredientes
        self.paso = paso  # 2. pasos

    @abstractmethod
    def mostrar(self): # 3. Movemos todo el método mostrar a la clase principal 
        print(f"Receta: {self.nombre}")
        print("Ingredientes:")
        for ingrediente in self.ingrediente:
            print(f"- {ingrediente}")
        print("Pasos:")
        for paso in self.paso:
            print(f"{paso}")

# Clase para recetas vegetarianas
class recetaVegetariana(receta): 
    def mostrar(self): # 3. Extracción del método mostrar
        return super().mostrar()


# Clase para recetas no vegetarianas
class recetaNoVegetariana(receta):
    def mostrar(self): # 3. Extracción del método mostrar
        return super().mostrar()


# Clase con utilidades del restaurante
class utilidades:
    @staticmethod
    def imprimir_receta(receta): # 2. De r a receta
        print("====================================")
        receta.mostrar()
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(lista):
        for l in lista:
            print(f"* {l}")

    
# Función principal
def principal():
    
   # 4. Eliminamos todas las funciones repetidas.


# Ejecutar el programa
if __name__ == "__main__":
    principal()
