#! /usr/bin/python3
from notaSG import Nota
import datetime



class Tarea(Nota):
    def __init__(self, texto, etiquetas, responsable, fecha_vencimiento):
        self.responsable = responsable
        self.fecha_vencimiento = fecha_vencimiento
        self.finalizado = False
        super().__init__(texto, etiquetas)

    def proximo_a_vencer(self):
        '''Determina si una tarea esta proxima a vencer
        Retorna true si esta proxima a vencer y false si no'''
        dia = datetime.timedelta(days=1)
        maniana = datetime.date.today() + dia
        pasadomaniana = datetime.date.today() + dia + dia
        if self.finalizado:
            return False
        elif self.fecha_vencimiento == datetime.date.today() or self.fecha_vencimiento == maniana or self.fecha_vencimiento == pasadomaniana:
            return True
        else:
            return False
  
    
    def vencido (self):
        if (self.finalizado == False and self.fecha_vencimiento<datetime.date.today()):
            return True
        else:
            return False








    



