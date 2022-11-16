import os

class node():
    #se definen las partes del arbol ya sea el dato, lado izquiero y el lado derecho 
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato
#en esta clase se define el arbol y que en un principio la raiz se encuentra vacia
class arbol():
    def __init__(self):
        self.root = None
#en este bloque se insertan datos en caso de que el arbo esté vacio se inserta uno
    def insert(self, a, dato):
        if a == None:
            a = node(dato)
        else:
            d = a.dato
            if dato < d: #en esta parte si el dato insertado despues de la raiz
                a.left = self.insert(a.left, dato) #se inserta el elemento en el lado izquierdo del arbol
            else:
                a.right = self.insert(a.right, dato)#de otra forma se inserta el elemento en el lado derecho del arbol
        return a
#funcion de ordenar en orden
    def inorder(self, a):
        if a == None:
            return None
        else:
            self.inorder(a.left)
            print(a.dato)
            self.inorder(a.right)
            
#funcion de ordenar en preorden
    def preorder(self, a):
        if a == None:
            return None
        else:
            print(a.dato)
            self.preorder(a.left)
            self.preorder(a.right)
#funcion de ordenar en postorden
    def postorder(self, a):
        if a == None:
            return None
        else:
            self.postorder(a.left)
            self.postorder(a.right)
            print(a.dato)

    def buscar(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a.dato
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.left)
                else:
                    return self.buscar(dato, a.right)

tree = arbol()
#en este bloque agregamos un menú con las funcionalidades del programa que son inorden, preorden, postorden
while True:
    os.system("cls")
    print("Arbol ABB")
    opc = input("\n1.-Insertar nodo \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-Salir \n\nElige una opcion -> ")
#si la opcion es 1 va a ingresar datos en nuestro arbol
    if opc == '1':
        nodo = input("\nIngresa el nodo -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            tree.root = tree.insert(tree.root, nodo)
        else:
            print("\nIngresa solo digitos...")#en esta linea validamos que solo se ingresen números
    elif opc == '2':#en esta linea se realiza la opcion de ordenar inorder y ejecuta nuestra clase propia
        if tree.root == None:
            print("Vacio")
        else:
            tree.inorder(tree.root)
    elif opc == '3':#en esta linea se realiza la opcion de ordenar inorder y ejecuta nuestra clase propia 
        if tree.root == None:
            print("Vacio")
        else:
            tree.preorder(tree.root)
    elif opc == '4':#en esta linea se realiza la opcion de ordenar postorder y ejecuta la clase propia
        if tree.root == None:
            print("Vacio")
        else:
            tree.postorder(tree.root)
    elif opc == '5':
        nodo = input("\nIngresa el nodo a buscar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if tree.buscar(nodo, tree.root) == None:
                print("\nNodo no encontrado...")
            else:
                print("\nNodo encontrado -> ",tree.buscar(nodo, tree.root), " si existe...")
        else:
            print("\nIngresa solo digitos...")        
    elif opc == '6':
        print("\nElegiste salir...\n")
        os.system("pause")
        break
    else:
        print("\nElige una opcion correcta...")
    print()
    os.system("pause")

print()
