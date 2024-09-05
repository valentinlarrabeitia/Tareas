from PySide6 import QtWidgets
from UI.ui_tareas import Ui_VentanaPrincipal
from controlador_tareas import AdministradorTareas


class VentanaTareas(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ventana = Ui_VentanaPrincipal()
        self.ventana.setupUi(self)
