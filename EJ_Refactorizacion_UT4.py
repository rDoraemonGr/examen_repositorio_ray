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
    
    receta1 = recetaVegetariana("Ensalada César", ["lechuga", "queso", "pan tostado", "salsa"], ["Lavar", "Mezclar", "Servir"]) # 2. Cambio el nombre para que corresponda con el nuevo nombre y r1 a receta1
    receta2 = recetaNoVegetariana("Pollo al horno", ["pollo", "patatas", "ajo", "aceite"], ["Preparar", "Hornear", "Servir"]) # 2. Cambio el nombre para que corresponda con el nuevo nombre y r2 a receta2
    
    # Duplicación de código al imprimir
    print("== Mostrar recetas ==")
    utilidades.imprimir_receta(receta1) # 2. De r1 a receta1
    utilidades.imprimir_receta(receta2) # 2. De r2 a receta2

    # Código duplicado para mostrar ingredientes
    print("Ingredientes de Ensalada César:")
    for ingrediente in receta1.ingrediente: # 2.1. Cambie receta1.i por receta.ingrediente
        print(f"* {ingrediente}")
    
    print("Ingredientes de Pollo al horno:")
    for ingrediente in receta2.ingrediente: # 2.1. Cambie receta1.i por receta.ingrediente
        print(f"* {ingrediente}")


# Ejecutar el programa
if __name__ == "__main__":
    principal()
