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
        while actual.next:
            if actual.valor == valor:
                return True
            actual = actual.next
            
        return False


    def __len__(self):
        actual = self.primero
        contador = 0
        while actual.next:
            contador += 1
            actual = actual.next
        
        return contador

    def append(self, valor):
        if self.primero is None: # Si la lista está vacía que lo agregue derecho al elemento.
            self.primero = Nodo(valor)
        else:
            actual = self.primero
            while actual.next: # Mientras que existe un nodo siguiente.
                actual = actual.next

            actual.next = Nodo(valor) # No hay nodo siguiente, así que lo hago igual al nodo que quiero añadir

        
    def prepend(self, valor):
        if self.primero is None: # Si la lista está vacía quiero añadirlo derecho.
            self.primero = Nodo(valor)
        else: # Cuando la lista no está vacía tengo que conectar el Nodo con el primer nodo de la lista
            nodo = Nodo(valor)
            nodo.next = self.primero
            self.primero = nodo


    
    def insert(self, valor, indice): # Se pide también el índice para saber dónde conectarlo
        actual = self.primero
        contador = 0
        if contador == indice: # Si quiero insertar un número en el indice 0
            nodo = Nodo(valor)
            nodo.next = self.primero.next
            self.primero = nodo
            return
        while actual.next: # En caso contrario, busco primero contador = indice.
            contador += 1
            if contador == indice:
                nodo = Nodo(valor)
                nodo.next = actual.next.next
                actual.next = nodo
                return
            actual = actual.next
        return "No se encontró tal índice."


    def delete(self, valor):
        actual = self.primero
        if actual.valor == valor:
            self.primero = actual.next
            return
        while actual.next:
            if actual.next.valor == valor:
                actual.next = actual.next.next
                break
            actual = actual.next
        return "No se encontró tal valor"
            
    def pop(self, indice):
        actual = self.primero
        contador = 0
        if contador == indice:
            self.primero = actual.next
            return
        while actual.next:
            contador += 1
            if contador == indice:
                actual.next = actual.next.next
                return
            actual = actual.next
        return "No se encontró tal índice"

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

lista.prepend(4)

print(lista)
print(lista.__len__())
print(lista.__contains__('a'))

lista.pop(3)
print(lista)

lista.insert(7, 0)
print(lista)
