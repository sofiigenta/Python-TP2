#! /usr/bin/python3
from notaSG import Nota
class Anotador:
    '''Representa una colección de Notas que se pueden etiquetar, modificar, y
    buscar'''

    def __init__(self):
       
        '''Inicializa el anotador con una lista vacía de Notas'''
        n1 = Nota('pagar boleta gas ', 'gas')
        n2 = Nota ('llamar por telefono', 'llamada')
        self.notas = [n1,n2]
        
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
