from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout)
from config import *  # Importa las constantes globales (textos, dimensiones, estilos)
from test import *    # Importa las ventanas o módulos secundarios (ej. TestWindow)

class MainWindow(QWidget):
    """
    Clase que representa la ventana principal de la aplicación.
    Hereda de QWidget para funcionar como una ventana estándar de PyQt5.
    """
    def __init__(self, title=TXT_TITLE):
        """
        Constructor de la clase. Inicializa la ventana y gestiona
        el orden de configuración de la interfaz y sus eventos.
        """
        self.title = title       # Almacena el título de la ventana
        super().__init__()       # Llama al constructor de la clase base QWidget

        # Métodos de inicialización de la ventana
        self.set_ui()            # Instancia los elementos visuales y el diseño (layout)
        self.config_window()     # Aplica configuraciones físicas y visuales a la ventana
        self.connections()       # Asigna los eventos de interacción (clicks de botones)
        self.show()              # Hace visible la ventana en la pantalla

    def set_ui(self):
        """
        Crea, configura e inserta todos los widgets (componentes gráficos) 
        dentro del contenedor o esquema principal (layout).
        """
        # --- INSTANCIACIÓN DE WIDGETS ---
        # Crea una etiqueta de texto para el mensaje de bienvenida usando la constante TXT_HELLO
        self.welcome_label = QLabel(TXT_HELLO)
        
        # Crea una etiqueta para mostrar las instrucciones al usuario usando TXT_INSTRUCTION
        self.instructions_label = QLabel(TXT_INSTRUCTION)
        
        # Crea un botón interactivo con el texto definido en TXT_NEXT y asigna esta ventana como su padre
        self.btn_next = QPushButton(TXT_NEXT, self)

        # --- CONFIGURACIÓN DE DISEÑO (LAYOUT) ---
        # Define un layout vertical: los componentes se apilarán uno debajo del otro
        self.main_layout = QVBoxLayout()

        # Añade la etiqueta de bienvenida alineada a la izquierda
        self.main_layout.addWidget(self.welcome_label, alignment=Qt.AlignLeft)
        
        # Añade la etiqueta de instrucciones alineada a la izquierda
        self.main_layout.addWidget(self.instructions_label, alignment=Qt.AlignLeft)
        
        # Añade el botón "Siguiente" centrado horizontalmente
        self.main_layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        # Establece 'main_layout' como el diseño oficial que gestionará esta ventana
        self.setLayout(self.main_layout)

    def config_window(self):
        """
        Establece las propiedades físicas de la ventana como tamaño, 
        posición inicial en pantalla y hoja de estilos CSS.
        """
        # Asigna el ancho y alto de la ventana según las constantes WIN_WIDTH y WIN_HEIGHT
        self.resize(WIN_WIDTH, WIN_HEIGHT)
        
        # Posiciona la ventana en las coordenadas (X, Y) de la pantalla según WIN_X y WIN_Y
        self.move(WIN_X, WIN_Y)
        
        # Aplica la hoja de estilos (CSS) almacenada en la variable STYLES para personalizar los colores/fuentes
        self.setStyleSheet(STYLES)

    def connections(self):
        """
        Conecta las acciones del usuario (eventos/señales) con sus 
        respectivas funciones de respuesta (slots).
        """
        # Escucha el evento de clic en el botón 'btn_next' y ejecuta el método 'self.next_click'
        self.btn_next.clicked.connect(self.next_click)

    def next_click(self):
        """
        Maneja la transición de pantallas cuando el usuario presiona el botón 'Siguiente'.
        """
        self.hide()               # Oculta la ventana principal actual
        self.test = TestWindow() # Instancia e inicia la segunda ventana (TestWindow)


# --- PUNTO DE ENTRADA DE LA APLICACIÓN ---
app = QApplication([])      # Crea el bucle principal de la aplicación PyQt
main_window = MainWindow() # Instancia e inicia la ventana principal
app.exec_()                 # Inicia la ejecución del programa y mantiene la ventana abierta
