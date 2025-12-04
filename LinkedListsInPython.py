# Listas compuestas. Cada dato guarda un puntero al siguiente nodo
# Time complexity de O(n)

# También pueden ser dobles, y tener punteros al nodo anterior.
class Nodo: # Nodo de lista enlazada

    def __init__(self, valor):
        self.valor = valor
        self.next = None
    
    # Cada nodo tiene un valor y esta conectado a un next.

class linkedList: # Lista enlazada

    def __init__(self):
        self.primero = None # Primer nodo de la lista
        self.value = None # Valor del nodo

    def __repr__(self):
        if self.primero is None:
            return "[]"
        else:
            actual = self.primero
            lista = f'[{actual.valor}]'

            while actual.next:
                actual = actual.next
                lista += f' -> [{actual.valor}]'
            return lista
    
    def __contains__(self, valor):
        actual = self.primero
        if actual == None:
            return False

    def __len__(self):
        pass

    def append(self, valor):
        if self.primero is None:
            self.primero = Nodo(valor)
        else:
            actual = self.primero
            while actual.next:
                if actual.next == None: # Si el siguiente nodo está vacío.
                    actual = actual.next
                
                actual.next = Nodo(valor) # Entonces el siguiente nodo apuntará a mi nuevo nodo.

        
    def prepend(self, valor):
        if self.primero is None:
            self.primero = Nodo(valor)
        else:
            primerNodo = self.primero
            

    
    def insert(self, valor):
        pass

    def delete(self, valor):
        pass
    
    def pop(self, index):
        pass

    # O(n) - Complejidad lineal porque debo recorrer los nodos hasta encontrar el índice
    def get(self, index): # Obtener valor en el índice dado
        actual = self.primero # Empiezo a buscar desde el primer nodo.
        contador = 0

        while actual is not None: # Mientras que pueda recorrer nodos
            if contador == index: # Si encuentro el índice
                return actual.valor # Puedo llamar a .valor porque actual pertenece a la clase Nodo.
            actual = actual.next # Me voy al puntero al que señala mi nodo actual.
            contador += 1
        return "No se encontró el índice" # Si no encuentro el índice




primer_nodo = Nodo(5) # Crear un nodo con valor 5
segundo_nodo = Nodo(10) # Crear un nodo con valor 10

primer_nodo.next = segundo_nodo # Conectar el primer nodo al segundo

lista = linkedList() # Crear una lista enlazada

lista.primero = primer_nodo # Establecer el primer nodo de la lista enlazada como primer_nodo

lista.append(15)

print(lista)