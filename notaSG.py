#! /usr/bin/python3
import datetime

#Guardamos en una variable la próxima id disponible:
ultima_id = 0

class Nota:
    '''Representa una nota en el anotador. Tiene texto, etiquetas (separadas 
    por espacios) y se puede buscar por texto'''
    def __init__(self, texto, etiquetas=''):
        '''Inicializa la nota con un texto, y opcionalmente, con etiquetas 
        separadas por espacios. Automáticamente define fecha de creación e id'''
        self.texto = texto
        self.etiquetas = etiquetas
        self.fecha_creacion = datetime.date.today()
        global ultima_id
        ultima_id += 1
        self.id = ultima_id

    def coincide(self, filtro):
        '''Determina si la nota coincide con el filtro de búsqueda. Retorna 
        True si es así y False de lo contrario
        
        Busca tanto en el texto como en las etiquetas y distingue mayúsculas de
        minúsculas '''
        if filtro in self.texto or filtro in self.etiquetas:
            return True
        else:
            return False
            
        #TODO: Construir este método
        # Recordatorio para buscar en una cadena:
        # if {subcadena} in {cadena}:
        # Ej:
        # if 'ten' in 'entretenido':  ---> sale por True
        # if 'blabla' in 'entretenido': ---> sale por False

