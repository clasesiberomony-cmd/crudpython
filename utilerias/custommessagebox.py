from PyQt5 import QtWidgets, QtCore, QtGui
# Si usas PyQt6, cambia los imports a:
# from PyQt6 import QtWidgets, QtCore, QtGui


class TranslucentMessageBox(QtWidgets.QDialog):
    def __init__(self, parent=None, title="Mensaje", message=""):
        super().__init__(parent)

        # --- Configuración de ventana sin bordes y fondo transparente ---
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.Dialog |
            QtCore.Qt.WindowSystemMenuHint
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        # --- Contenedor principal (el "cuadro" visual) ---
        frame = QtWidgets.QFrame()
        frame.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 230);
                border-radius: 20px;
                border: 1px solid rgba(0,0,0,0.1);
            }
            QLabel {
                color: #222;
                font-size: 14px;
            }
            QPushButton {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                                  stop:0 #228BE6, stop:1 #1C70C6);
                color: white;
                border: none;
                border-radius: 8px;
                padding: 6px 14px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #1C70C6;
            }
        """)

        # --- Sombra para el cuadro ---
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(24)
        shadow.setOffset(0, 8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 60))
        frame.setGraphicsEffect(shadow)

        # --- Layout interno ---
        vbox = QtWidgets.QVBoxLayout(frame)
        vbox.setContentsMargins(24, 24, 24, 24)
        vbox.setSpacing(18)

        # Título
        lbl_title = QtWidgets.QLabel(title)
        lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        lbl_title.setStyleSheet("font-size: 18px; font-weight: 700; color: #1C70C6;")
        vbox.addWidget(lbl_title)

        # Mensaje
        lbl_message = QtWidgets.QLabel(message)
        lbl_message.setAlignment(QtCore.Qt.AlignCenter)
        lbl_message.setWordWrap(True)
        vbox.addWidget(lbl_message)

        # Botón OK
        btn_ok = QtWidgets.QPushButton("Aceptar")
        btn_ok.setFixedWidth(100)
        btn_ok.clicked.connect(self.accept)
        vbox.addWidget(btn_ok, alignment=QtCore.Qt.AlignCenter)

        # --- Layout principal del diálogo ---
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(frame)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Tamaño base
        self.setFixedSize(340, 200)

        # Permitir arrastre del cuadro (ya que no hay título)
        frame.mousePressEvent = self._mouse_press
        frame.mouseMoveEvent = self._mouse_move
        frame.mouseReleaseEvent = self._mouse_release
        self._drag_pos = None

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
