from ventana_agregar_tarea import VentanaAgregarTarea
from PySide6 import QtWidgets


class AdministradorTareas:
    def desplegar_ventana_para_agregar_tarea(self):
        ventana = VentanaAgregarTarea()
        ventana.desplegar_ventana_para_agregar_tarea()

