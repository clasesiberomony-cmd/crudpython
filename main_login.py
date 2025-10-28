# ejemplo_py_load_ui.py
import sys
from PyQt5 import QtWidgets, uic, QtCore  # si usas PyQt6: from PyQt6 import ...
# from PyQt6 import QtWidgets, uic, QtCore
from modelo.usuariodao import UsuarioDAO

class LoginWindow(QtWidgets.QWidget):
    def __init__(self, ui_path="login_form.ui"):
        super().__init__()
        uic.loadUi(ui_path, self)

        # Quitar bordes / título y permitir transparencia (necesario en runtime)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowSystemMenuHint)
        # Permite fondo transparente (en algunos sistemas puede requerir composición)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        # Conectores
        self.btn_close.clicked.connect(self.close)
        self.btn_login.clicked.connect(self.on_login)
        

        # Estética: si quieres sombra nativa puedes crear QGraphicsDropShadowEffect en frame_main
        # Habilitar arrastre de la ventana (para ventana sin marco)
        self._drag_pos = None
        self.frame_main.mousePressEvent = self._mouse_press
        self.frame_main.mouseMoveEvent = self._mouse_move
        self.frame_main.mouseReleaseEvent = self._mouse_release

    def _mouse_press(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def _mouse_move(self, event):
        if self._drag_pos and event.buttons() & QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self._drag_pos)
            event.accept()

    def _mouse_release(self, event):
        self._drag_pos = None
        event.accept()

    def on_login(self):
        usuario = self.le_username.text().strip()
        password = self.le_password.text().strip()

        
        # Aquí validas credenciales -> reemplaza con tu lógica
        
        # Ejemplo simple:
        if usuario and password:
            usuariodao = UsuarioDAO()
            usuariodao.usuario.nickname = usuario
            usuariodao.usuario.password = password
            lista = usuariodao.buscarUsuario()
            if len(lista) > 0:

                QtWidgets.QMessageBox.information(self, "OK", "Intento de login enviado.")
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Usuario o contraseña inválido.")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Completa usuario y contraseña.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = LoginWindow("ui/login.ui")
    win.show()
    sys.exit(app.exec_())
