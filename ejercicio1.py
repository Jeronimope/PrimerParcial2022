# a #Necesito que proceses urgente este archivo con información del parque y esté
#disponible en mi monitor de informes. Y no olvide determinar cual de nuestro dinosaurios fuel el
#ultimo en ser descubierto y quien lo hizo.

# b Por favor debes hacer un scripts que procese el
#archivo en esta USB llamado “alerts.txt”, necesito los datos ordenados por fecha para Claire y otro
#ordenado por nombre de dinosaurio para cruzarlo con los datos del sistema de incidentes. Por favor
#date prisa lo necesito urgente poder listar esta información. Recuerda agregar el nombre del
#dinosaurio de acuerdo a su número.

# c#Les dije explícitamente que debemos mantener anónima toda la información respecto de las
#zonas WYG075, SXH966 y LYF010 por favor eliminen en este momento toda esa información de los
#datos procesados previamente. Ah casi me olvidaba de decirles modifiquen el registro de la zona
#HYD195 el nombre correcto del dinosaurio es Mosasaurus.

# d # Necesito urgente un listado filtrado de los
#datos que solo incluya datos de los dinosaurios: Tyrannosaurus Rex, , Spinosaurus, Giganotosaurus con
#nivel  ́critical’ o ‘high’.

# e #Necesito
#que tomes toda la información de alertas, y las insertes en dos colas, una con los datos de dinosaurios
#carnívoros y otra con los herbívoros, descarten las de nivel ‘low’ y ‘medium’.

# f #atiendan las alertas en la cola de carnívoros y muestren
#en la pantalla (para que se publiquen en el canal de alerta de banda segura) la información pero
#descarten las provenientes de la zona EPC944, ya se encuentra una unidad de respaldo ahí.

# g #notebook, podrían pasarme un listado de toda la información que tienen procesada del archivo, pero
#solo de los dinosaurios Raptors y Carnotaurus; y los códigos de las zonas donde puedo encontrar
#dinosaurios Compsognathus. Que sea lo antes posible hoy es un día muy agitado.

from jurassic_park import dinosaurs
from lista import Lista
from cola import Cola
lista_dinosaurios = Lista ()
lista_uno = Lista()
lista_dos = Lista()
pos=0
lista_dinosaurios.insertar(dinosaurs, 'nombre')
colacarnivoros = Cola()
colaherviboros = Cola()

#Punto a
pos = lista_dinosaurios.busqueda('cretácico superior')
if (pos > -1 ):
    print('El último dinosaurio en ser descubierto fue  ',lista_dinosaurios.obtener_elemento(pos)['nombre'])

    #puntob
archivo = open ("alerts.txt", "w")
archivo.close ()
    print "alerts.txt"
    
    for i in range(lista_dinosaurios.tamanio()):
    pos = lista_dinosaurios.obtener_elemento(i)
   lista_dinosaurios.ordenar
print ()
   #c
    
for i in range(lista_uno.tamanio()):
	num=lista_uno.obtener_elemento(i)
	pos = lista_dos.busqueda(num)
    pos = lista_dinosaurios.busqueda('WYG075',  y 'LYF010','SXH966')
if (pos > -1 ):
    aux=lista_uno.eliminar(pos)

    #d
pos = lista_dinosaurios.busqueda('Tyrannosaurus Rex','nombre')
if (pos > -1 ):
    print('Informacion de Tyrannosaurus Rex: ',lista_dinosaurios.obtener_elemento(pos))

pos = lista_dinosaurios.busqueda('Spinosaurus','nombre')
if (pos > -1 ):
    print('Informacion de Spinosaurus: ',lista_dinosaurios.obtener_elemento(pos))


pos = lista_dinosaurios.busqueda('Giganotosaurus','nombre')
if (pos > -1 ):
    print('Informacion de Giganotosaurus: ',lista_dinosaurios.obtener_elemento(pos))


    #e
    while (not colacarnivoros.cola_vacia()):
    dato=colacarnivoros.atencion()
    if (dato[0]=='carnivoros'):
        colacarnivoros.arribo(dato)
    else
    while (not colaherviboros.cola_vacia()):
    dato=colaherviboros.atencion()
    if (dato[0]=='herviboros'):
        colaherviboros.arribo(dato)    
    

        #f 
        if (not ctrl_colas):
    ctrl=False
    print('informacion de cola de carnivoros')
    while(not cola_aux.cola_vacia()):
        dato=cola_aux.atencion()
        if (dato='carnivoros'):
            print(dato)
            ctrl=True
    if (not ctrl):
        print('no se puede mostrar')


        #g
        for i in range (lista_dinosaurios.tamanio()):
    if (i< lista_dinosaurios.tamanio()):
        personaje= lista_dinosaurios.obtener_elemento(i)
    
    if (personaje [0] == 'Raptors'):
        print ('Informacion del personaje ', personaje['Raptors'])
     if (personaje [0] == 'Carnotaurus'):
        print ('Información del personaje ', personaje['Carnotaurus'])
    