from PySide6 import QtWidgets
from ventana_de_tareas import VentanaTareas

app = QtWidgets.QApplication()
ventana = VentanaTareas()
ventana.show()


app.exec()
