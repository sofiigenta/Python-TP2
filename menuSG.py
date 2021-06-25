#! /usr/bin/python3
from anotadorSG import Anotador
import datetime
import sys
class Menu:
    '''Mostrar un menú y responder a las opciones'''

    def __init__(self):
        self.anotador = Anotador()
        self.opciones= {
            "1": self.mostrar_notas,
            "2": self.buscar_notas,
            "3": self.agregar_nota,
            "4": self.modificar_nota,
            "5": self.finalizar_tarea,
            "6": self.mostrar_vencidas,
            "7": self.mostrar_por_vencer,
            "8": self.salir
        }

    def mostrar_menu(self):
        '''Muestra el menú de opciones'''
        print("""
Menú del anotador:
1. Mostrar todas las notas
2. Buscar Notas
3. Agregar Nota
4. Modificar Nota
5: Finalizar tarea
6: Mostrar tareas vencidas
7: Mostrar tareas por vencer
8: Salir
""")
   

    def ejecutar(self):
        '''Mostrar el menu y responder a las opciones.'''
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")

            # Guardamos en la variable accion el método que corresponde a la
            # opción elegida por el usuario. Por ejemplo, si opcion tiene el 
            # valor 1, accion va a guardar el valor correspondiente a 
            # self.opciones[1], es decir: self.mostrar_notas
            accion = self.opciones.get(opcion)

            # Si hay algún valor guardado en accion, ejecutamos el método que
            #tiene ese nombre, y si no mostramos un error:
            if accion:
                accion()
            else:
                print("{0} no es una opción válida".format(opcion))

    def mostrar_notas(self, notas=None):
        '''Si recibe como parámetro una lista de notas, muestra id, texto y
        etiquetas de esas notas. Si no recibe el parámetro, muestra id, texto
        y etiquetas de todas las notas'''
        
        if notas:
            for nota in notas:
                print (f' El id de la nota es: {nota.id}, el texto de la nota es: {nota.texto} y las etiquetas de la nota son: {nota.etiquetas}')   
        else:
            for nota in self.anotador.notas:
                print (f' El id de la nota es: {nota.id}, el texto de la nota es: {nota.texto} y las etiquetas de la nota son: {nota.etiquetas}')


    def buscar_notas(self):
        '''Solicita al usuario una cadena de búsqueda y muestra las notas que 
        coinciden con la misma, si es que hay alguna'''
        filtro = input("Buscar: ")
        notas = self.anotador.buscar(filtro)
        if notas:
            print ('Las notas que coinciden son: ')
            self.mostrar_notas(notas)
        else:
            print("Ninguna nota coincide con la búsqueda")
  
    

    def agregar_nota(self):
        '''Solicita un texto al usuario y agrega una nueva nota con ese texto'''
        opcion = int(input('Ingrese 1 si es Nota o 2 para tareas'))
        if opcion == 1:
            texto = input('Ingrese el texto de la nota: ')
            etiquetas = input('Ingrese las etiquetas de la nota: ')
            nota = self.anotador.nueva_nota(texto,etiquetas)
        elif opcion == 2:
            texto = input('Ingrese el texto de la nota: ')
            etiquetas = input('Ingrese las etiquetas de la nota: ')
            responsable = input('Ingrese el nombre del responsable')
            fecha = input('Ingrese fecha de vencimiento en formato AAAA/MM/DD')
            a,m,d = map(int,fecha.split('/'))
            fecha_vencimiento = datetime.date(a,m,d)
            nota = self.anotador.nueva_tarea(texto,etiquetas,responsable,fecha_vencimiento)
        else: 
            print ('Error de opcion')
        

        
    def modificar_nota(self):
        '''Solicita el id de una nota y el nuevo texto y/o etiquetas que tendrá
        la misma.  Busca la nota con el id ingresado, y actualiza su texto y/o
        etiquetas.'''
        id2 = int(input("Ingrese el id de la nota a modificar: "))
        texto = input("Ingrese el texto de la nota: ")
        etiquetas = input("Ingrese las etiquetas: ")

        # Si el usuario ingresó algún texto, lo actualiza.
        if texto:
            self.anotador.modificar_nota(id2, texto)
        # Si el usuario ingresó etiquetas, las actualiza.
        if etiquetas:
            self.anotador.modificar_etiquetas(id2, etiquetas)
          
         
    def finalizar_tarea(self):
        id_tarea = int(input('Ingrese el id de la tarea a finalizar'))
        self.anotador.finalizar_tarea(id_tarea)
        

    def mostrar_vencidas (self):
        responsable = input('Warning: Distingue mayusculas de minusculas. Si lo desea ingrese el nombre del responsable: ')
        notas = self.anotador.tareas_vencidas(responsable)
        if notas: 
            print('Las tareas vencidas son: ')
            self.mostrar_notas(notas)
        else: 
            print ('Ninguna tarea coincide')
    
    def mostrar_por_vencer (self):
        responsable = input ('Warning: Distingue mayusculas de minusculas. Si lo desea ingrese el nombre del responsable: ')
        notas = self.anotador.tareas_por_vencer(responsable)
        if notas: 
            print ('Las tareas vencidas son: ')
            self.mostrar_notas(notas)
        else: 
            print ('Ninguna tarea coincide')
          

    def salir(self):
        '''Muestra un mensaje y sale del sistema'''
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

#Esta parte del código está fuera de la clase Menu.
#Si este archivo es el programa principal (es decir, si no ha sido importado
#desde otro módulo, sino ejecutado directamente), entonces llamamos al método
# ejecutar(). 
if __name__ == "__main__":
    Menu().ejecutar()
