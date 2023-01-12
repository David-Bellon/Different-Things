import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog, QLineEdit, QHBoxLayout, QFrame
from PySide6.QtCore import Qt, QTimer
from dowload_youtube import dowload

class YoutubeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dowload Youtube Video")
        self.setFixedSize(1000, 800)

        title_label = QLabel("Youtube Dowload")
        font = title_label.font()
        font.setPointSize(20)
        title_label.setFont(font)
        title_label.setStyleSheet("padding-top: 40px;")
        title_label.setStyleSheet("padding-bop: 40px;")
        title_label.setStyleSheet("color: red;")
        title_label.setAlignment(Qt.AlignCenter)

        # Create the frame widget
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFixedHeight(170)
        frame_layout = QVBoxLayout()

        self.label_text_field = QLabel("Youtube Url:")
        
        # Create the text field widget
        self.text_field = QLineEdit()
        self.text_field.setPlaceholderText("Paste here Url from Youtube")
        self.text_field.setFixedHeight(30)

        button1 = QPushButton("Select folder")
        button1.setMinimumSize(100, 40)
        button1.setMaximumSize(100, 40)
        button1.setStyleSheet("margin-top: 10px;")
        button1.clicked.connect(self.open_file_dialog)

        self.folder_label = QLabel()

        frame_layout.addWidget(self.label_text_field)
        frame_layout.addWidget(self.text_field)
        frame_layout.addWidget(button1)
        frame_layout.addWidget(self.folder_label)
        frame_layout.setContentsMargins(20, 20, 20, 20)

        frame.setLayout(frame_layout)

        #Explanation Text
        explain_text = QLabel("When you press Download it will download the audio of the video that you paste in the folder that you have selected")
        exp_font = explain_text.font()
        exp_font.setPointSize(12)
        explain_text.setFont(exp_font)
        explain_text.setStyleSheet("padding-top: 50px;")
        explain_text.setAlignment(Qt.AlignCenter)

        #Button To Dowload
        d_button = QPushButton("DOWNLOAD")
        d_button.setMinimumSize(200, 100)
        d_button.setMaximumSize(200, 100)
        d_button.setStyleSheet("margin-top: 20px;")
        d_button.clicked.connect(self.dowload_video)

        #Text For results of dowload
        self.place_holder = QLabel()
        pl_font = self.place_holder.font()
        pl_font.setPointSize(13)
        self.place_holder.setFont(pl_font)
        self.place_holder.setAlignment(Qt.AlignCenter)

        # Create the layout and add the combo box and text field
        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(frame)
        layout.addWidget(explain_text)
        layout.addWidget(d_button)
        layout.addWidget(self.place_holder)
        layout.setAlignment(d_button, Qt.AlignCenter)
        layout.setAlignment(Qt.AlignTop)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def open_file_dialog(self):
        options = QFileDialog.Option()
        options |= QFileDialog.ReadOnly
        folder = QFileDialog.getExistingDirectory(self, "Select Folder", "", options=options)
        if folder:
            self.folder_label.setText(folder)
    
    def dowload_video(self):
        if self.text_field.text() == "" or self.folder_label.text() == "":
            self.place_holder.setText("Please select a url and a folder to dowload")
            QTimer.singleShot(2000, self.clear_text)
        else:
            outcome = dowload(self.text_field.text() ,self.folder_label.text())
            self.place_holder.setText(outcome)
            QTimer.singleShot(2000, self.clear_text)

    def clear_text(self):
        self.place_holder.clear()