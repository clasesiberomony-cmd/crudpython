from PyQt5 import QtWidgets, uic, QtGui,QtCore
import sys
from load.load_ui_productos import Load_ui_productos

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/menu.ui", self)
        self.showMaximized()

        # Agregar logotipo centrado
        logo = QtWidgets.QLabel(self.centralwidget)
        logo.setPixmap(QtGui.QPixmap("resources/imagenes/logoIbero.png"))
        logo.setScaledContents(False)
        logo.setAlignment(QtCore.Qt.AlignCenter)

        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout.addWidget(logo)

        #conectar items con acciones
        self.actionProductos.triggered.connect(self.abrirProductos)

    def abrirProductos(self):
        window = Load_ui_productos()
        window.show()

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())'''