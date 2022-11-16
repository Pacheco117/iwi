


class Nodo:
    def __init__(self, nombre=None, cedula=None, izq=None, der=None):
        self.nombre=nombre
        self.cedula=cedula
        self.izq=izq
        self.der=der
    
    def __str__(self):
        return "%s %s" %(self.nombre, self.cedula)

class aBinarios:
    def __init__(self):
        self.raiz = None

def agregar(self,elemento):
    if self.raiz == None:
        self.raiz = elemento
    else:
        aux = self.raiz
        padre = None
        while aux != None:
            padre= aux
            if int(elemento.cedula) >= int(aux.cedula):
                aux = aux.der
            else:
                aux = aux.izq
        if int(elemento.cedula)>= int(padre.cedula):
            padre.der = elemento
        else:
            padre.izq=elemento

def preorder(self,elemento):
    if elemento != None:
        print(elemento)
        self.preorder(elemento.izq)
        self.preorder(elemento.der)

def postorder(self,elemento):
    if elemento != None:
        self.postorder(elemento.izq)
        self.postorder(elemento.der)
        print(elemento)

def inorder(self,elemento):
    if elemento != None:
        self.inorder(elemento.izq)
        print(elemento)
        self.inorder(elemento.der)

def getRaiz(self):
    return self.raiz

if __name__ == "__main__":
    ab=aBinarios()
    while(True):
        print("opción 1 agregar\n"+
        "opción 2 preorden\n"+
        "opcion 3 postorden\n"+
        "opcion 4 inorden\n")

        num = input("ingrese opción")
        if num == "1":
            nombre = input("ingrese nombre: ")
            cedula = input("ingrese la cedula: ")
            Nod = Nodo(nombre, cedula)
            ab.agregar(Nod)
        elif num == "2":
            print("imprimendo preorden")
            ab.preorder(ab.getRaiz())
        elif num =="3":
            print("imprimiendo postorden")
            ab.postorder(ab.getRaiz())
        elif num == "4":
            print("imprimiendo inorden")
            ab.inorder(ab.getRaiz())


            
