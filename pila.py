class Nodopila(): 
    info, sig= None, None               

class Pila():
    def __init__(self):                   
        self.__tamanio=0             # __ para hacer una variable privada
        self.__cima=None

    def tamanio(self):                  #para usar tamanio
        return self.__tamanio
    
    def apilar(self,dato):
        nodo=Nodopila()
        nodo.info=dato
        if(self.__cima is None):
            self.__cima=nodo
        else:
            nodo.sig=self.__cima
            self.__cima=nodo

        self.__tamanio+=1
    def cima(self):
        return self.__cima.info

    def pilaVacia(self):
        return self.__cima is None           #== o is
    def desapilar(self):
        dato=self.__cima.info 
        self.__cima=self.__cima.sig     #apunta la cima al dato que estaba abajo
        self.__tamanio-=1              #reasignar el tamañode la pila
        return dato

# from random import randint

# pila1=pila()
# print(pila1.pilaVacia())

# for i in range(10):
#     num= randint(0,100)
#     print('numero generado ', num)
#     pila1.apilar(num)

# print(pila1.tamanio())

# while(not pila1.pilaVacia()):
#     dato=pila1.desapilar()
#     print('elemento desapilado ', dato)


# print(pila1.pilaVacia())