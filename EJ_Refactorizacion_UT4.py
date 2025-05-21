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

def crear_receta(nombre1, ingrediente1, paso1): # 4. Añadimos la función que nos servirá para la creación de las recetas
    nombre1 = input("Introduce el nombre de la receta: ")
    ingrediente1 = []
    print("Introduce los ingredientes (escribe 'fin' para terminar): ")
    while True:
        ingrediente = input("- ")
        if ingrediente.lower() == "fin":
            break
        ingrediente1.append(ingrediente)
    paso1 = []
    print("Introduce los pasos (escirbe 'fin' para terminar): ")
    while True:
        paso = input("- ")
        if ingrediente.lower() == "fin":
            break
        paso1.append(ingrediente)
    return nombre1, ingrediente1, paso1
        
# Función principal
def principal():


# Ejecutar el programa
if __name__ == "__main__":
    principal()
