#! /usr/bin/python3
import datetime
from notaSG import Nota
from tareaSG import Tarea

class Anotador:
    '''Representa una colección de Notas que se pueden etiquetar, modificar, y
    buscar'''

    def __init__(self):
       
        '''Inicializa el anotador con una lista vacía de Notas'''
        n1 = Nota('pagar boleta gas ', 'gas')
        n2 = Nota ('llamar por telefono', 'llamada')
        n3 = Tarea('Ir a la verduleria', 'compras', 'Sofia', datetime.date(2020,4,13)) 
        n4 = Tarea('Ir al dentista','dentista', 'Sofia', datetime.date(2021,6,29)) 
        self.notas = [n1,n2,n3,n4]
        
        #p Para facilitar las pruebas, podrías inicializarlo con dos o tres
        # notas precargadas, para evitar cargarlas a mano cada vez que se
        # ejecuta el programa.

    def nueva_nota(self, texto, etiquetas = ''):
        '''Crea una nueva nota y la agrega a la lista de notas'''
        
        
        n = Nota(texto,etiquetas) 
        self.notas.append(n)

    def _buscar_por_id(self,id_nota):
        '''Buscar la nota con el id dado'''
        for nota in self.notas:
            if id_nota == nota.id:
                return nota
        return None




    def modificar_nota(self, id_nota, texto):
        '''Busca la nota con el id dado y modifica el texto'''
        # (Este método ya está hecho)
        # Busca la nota por id, usando el método anterior.
        nota = self._buscar_por_id(id_nota)

        # Si lo encontró, actualiza el texto de la nota y retorna True:
        if nota:
            nota.texto = texto
            return True
        # pero si no lo encontró, retorna False:
        return False

    def modificar_etiquetas(self, id_nota, etiquetas):
        '''Busca la nota con el id dado y modifica las etiquetas'''
        
        nota = self._buscar_por_id(id_nota)
        if nota:
            nota.etiquetas = etiquetas
            return True
        return False
   
    def buscar(self, filtro):
        '''Retorna una lista de todas las notas que coincidan con el filtro 
        dado, en el texto o en las etiquetas'''
     
        notas = []
        for nota in self.notas:
            if nota.coincide(filtro):
               notas.append(nota)
            else:
                None
        return notas
    
    def nueva_tarea (self, texto, etiquetas, responsable, fecha_vencimiento):
        n = Tarea(texto, etiquetas, responsable, fecha_vencimiento)
        self.notas.append(n)

    def finalizar_tarea (self, id_nota):
        nota = self._buscar_por_id(id_nota)
        if hasattr(nota, 'responsable') and nota.finalizado == False:
            nota.finalizado = True
            print ('Tarea finalizada')
        else:
            print ('No se encontro esta tarea o ya se encuentra finalizada')


    def tareas_vencidas (self, responsable= None):
        notas = []
        if responsable: 
            for nota in self.notas:
                if hasattr(nota, 'responsable') and nota.vencido() and nota.responsable == responsable:
                    notas.append(nota)
        else:
            for nota in self.notas:
                if hasattr (nota, 'responsable') and nota.vencido():
                    notas.append(nota)
        return notas
       
 

    def tareas_por_vencer (self, responsable=None):
        notas = []
        if responsable:
            for nota in self.notas:
                if hasattr(nota, 'responsable') and nota.proximo_a_vencer() and nota.responsable == responsable:
                    notas.append(nota)
        else:
            for nota in self.notas:
                if hasattr(nota, 'responsable') and nota.proximo_a_vencer():
                    notas.append(nota)
        return notas
        


 
