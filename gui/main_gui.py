import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt
from youtube_gui import YoutubeWindow
from face_tracking_gui import FaceWindow
from transcribe_gui import TranscribeWindow
from chess_ui import ChessBoard
from arqs import Model

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the title of the main window
        self.setWindowTitle("Main Menu")
        self.setFixedSize(1100, 900)

        label = QLabel("App Paradise")
        font = label.font()
        font.setPointSize(20)
        label.setFont(font)
        label.setStyleSheet("padding-top: 70px;")

        # Create the buttons for the three sub-windows
        button1 = QPushButton("Youtube Download")
        button1.setMinimumSize(130, 100)
        button1.setMaximumSize(130, 100)

        button2 = QPushButton("Face Tracking")
        button2.setMinimumSize(130, 100)
        button2.setMaximumSize(130, 100)

        button3 = QPushButton("Audio to Text")
        button3.setMinimumSize(130, 100)
        button3.setMaximumSize(130, 100)

        button4 = QPushButton("Chess Game")
        button4.setMinimumSize(130, 100)
        button4.setMaximumSize(130, 100)

        # Connect the buttons to the appropriate functions
        button1.clicked.connect(self.open_window1)
        button2.clicked.connect(self.open_window2)
        button3.clicked.connect(self.open_window3)
        button4.clicked.connect(self.open_window4)

        # Create a vertical layout and add the buttons
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.setAlignment(label, Qt.AlignTop| Qt.AlignHCenter)
        layout.setAlignment(button1, Qt.AlignTop| Qt.AlignHCenter)
        layout.setAlignment(button2, Qt.AlignTop| Qt.AlignHCenter)
        layout.setAlignment(button3, Qt.AlignTop| Qt.AlignHCenter)
        layout.setAlignment(button4, Qt.AlignTop| Qt.AlignHCenter)
        layout.setContentsMargins(0, 10, 0, 0)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_window1(self):
        youtube_window.show()

    def open_window2(self):
        face_trackign.show()

    def open_window3(self):
        transcribe.show()

    def open_window4(self):
        chess.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    youtube_window = YoutubeWindow()
    face_trackign = FaceWindow()
    transcribe = TranscribeWindow()
    chess = ChessBoard()
    window.show()
    sys.exit(app.exec())