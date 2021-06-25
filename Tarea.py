#! /usr/bin/python3
import datetime
from notaSG import Nota


class Tarea(Nota):
    def __init__(self, texto, etiquetas='', responsable, fecha_vencimiento):
        super().__init__(texto, etiquetas='')
        self.responsable = responsable
        self.fecha_vencimiento = fecha_vencimiento
        self.finalizado = False
        
    
    def proximo_a_vencer (self):
        hoy = datetime.date.today()
        un_dia_mas = datetime.timedelta(days=1)
        maniana = hoy + un_dia_mas
        pasado = hoy + un_dia_mas + un_dia_mas
        if self.finalizado: 
            return False
        elif (self.fecha_vencimiento == hoy or self.fecha_vencimiento == maniana or self.fecha_vencimiento == pasado) 
            return True
        else:
            return False
    
    def vencido (self):
        if (self.finalizado == False or self.fecha_vencimiento<hoy == True ):
            return True
        else:
            return False








    



