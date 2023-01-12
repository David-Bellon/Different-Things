import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt
from face_track import cam_test

class FaceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Face Tracking Model")
        self.setFixedSize(1000, 800)

        title_label = QLabel("Face Tracking Model")
        font = title_label.font()
        font.setPointSize(20)
        title_label.setFont(font)
        title_label.setStyleSheet("color: green;")
        title_label.setAlignment(Qt.AlignCenter)

        button = QPushButton("Initiate")
        button.setMinimumSize(130, 60)
        button.setMaximumSize(130, 60)
        button.clicked.connect(self.track_face)

        self.label = QLabel()
        self.label.setGeometry(10, 10, 700, 700)
        self.label.setAlignment(Qt.AlignCenter)

        self.out_button = QPushButton("Exit")
        self.out_button.setMinimumSize(130, 60)
        self.out_button.setMaximumSize(130, 60)
        self.out_button.setVisible(False)

        self.close = False

        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(button)
        layout.addWidget(self.label)
        layout.addWidget(self.out_button)
        layout.setAlignment(button, Qt.AlignCenter)
        layout.setAlignment(self.out_button, Qt.AlignCenter)
        layout.setAlignment(Qt.AlignTop)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def track_face(self):
        cam_test(self)