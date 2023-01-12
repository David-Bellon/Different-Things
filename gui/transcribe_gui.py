import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog, QLineEdit, QHBoxLayout, QFrame, QComboBox, QDialog
from PySide6.QtCore import Qt, QTimer
import torch
import torch.nn as nn
from transcribe import main_transcribe
from record_audio import record
import datetime
import time

class TranscribeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transcribe Audio")
        self.setFixedSize(1000, 800)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.ready_to_trans = False

        title_label = QLabel("Transcribe Any Audio")
        font = title_label.font()
        font.setPointSize(20)
        title_label.setFont(font)
        title_label.setStyleSheet("color: blue;")
        title_label.setAlignment(Qt.AlignCenter)

        self.explain_text = QLabel("To run this you should have a GPU with enought VRAM otherwise won't work. With CPU you may destroy your PC")
        if self.device == "cuda":
            self.device_text = QLabel(f"You currently are connected with the device GPU: {torch.cuda.get_device_name(0)}   It may work")
        else:
            self.device_text = QLabel(f"You currently are connected with the device: CPU    Probably not gonna work")

        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFixedHeight(170)
        frame_layout = QVBoxLayout()

        model_label = QLabel("Select Model: Take care that the higher the model the more VRAM you need")

        self.model_selection = QComboBox()
        self.model_selection.addItems(["base", "medium"])

        button1 = QPushButton("Select file")
        button1.setMinimumSize(130, 40)
        button1.setMaximumSize(130, 40)
        button1.setStyleSheet("margin-top: 10px;")
        button1.clicked.connect(self.select_file)

        self.file_label = QLabel()
        self.warning_label = QLabel()

        frame_layout.addWidget(model_label)
        frame_layout.addWidget(self.model_selection)
        frame_layout.addWidget(button1)
        frame_layout.addWidget(self.file_label)
        frame_layout.addWidget(self.warning_label)
        frame_layout.setContentsMargins(20, 20, 20, 20)

        frame.setLayout(frame_layout)

        self.text_trans = QLabel("This is working I promise it takes time")
        self.text_trans.setVisible(False)
        self.text_trans.setAlignment(Qt.AlignCenter)

        button_transcribe = QPushButton("Transcribe File")
        button_transcribe.setMinimumSize(120, 50)
        button_transcribe.setMaximumSize(120, 50)
        button_transcribe.setStyleSheet("margin-top: 10px;")
        button_transcribe.clicked.connect(self.transcirbe_file)

        text_record = QLabel("If you want to record 10 seconds of audio and trascribe this is your way")
        text_record.setStyleSheet("margin-top: 20px")
        text_record.setAlignment(Qt.AlignCenter)
        self.text_warning = QLabel("Recording...")
        self.text_warning.setVisible(False)
        self.text_warning.setAlignment(Qt.AlignCenter)

        button_record = QPushButton("Record 10 seconds")
        button_record.setMinimumSize(130, 40)
        button_record.setMaximumSize(130, 40)
        button_record.setStyleSheet("margin-top: 10px;")
        button_record.clicked.connect(self.record_and_transcribe)

        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(self.explain_text)
        layout.addWidget(self.device_text)
        layout.addWidget(frame)
        layout.addWidget(self.text_trans)
        layout.addWidget(button_transcribe)
        layout.addWidget(text_record)
        layout.addWidget(button_record)
        layout.addWidget(self.text_warning)
        layout.setAlignment(button_transcribe, Qt.AlignCenter)
        layout.setAlignment(button_record, Qt.AlignCenter)
        layout.setAlignment(Qt.AlignTop)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def select_file(self):
        options = QFileDialog.Option()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            self.file_label.setText(file_name)
            file = file_name.split("/")[-1].split(".")[-1]
            if file != "mp4" and file != "mp3" and file != "wav":
                self.warning_label.setText("Only mp4, mp3, or wav supported. Please select another file")
                self.warning_label.setStyleSheet("color: red;")
                self.ready_to_trans = False
            else:
                self.warning_label.setText("File has a correct extension. Ready to goooooo!!")
                self.warning_label.setStyleSheet("color: green;")
                self.ready_to_trans = True

    def transcirbe_file(self):
        if self.ready_to_trans:
            self.text_trans.setVisible(True)
            QApplication.processEvents()
            out = main_transcribe(self.file_label.text(), self.model_selection.currentText(), self.device)
            final_res = ""
            for elements in out["segments"]:
                start = str(datetime.timedelta(seconds=elements["start"])).split(":", 1)[1]
                end = str(datetime.timedelta(seconds=elements["end"])).split(":", 1)[1]
                text = str(elements["text"])
                final_res = final_res + f"[{start} --> {end}]  {text}\n"
            pop_up = PopUp(final_res)
            self.text_trans.setVisible(False)
            pop_up.exec()
    
    def record_and_transcribe(self):
        self.text_warning.setVisible(True)
        QApplication.processEvents()
        record()
        self.text_warning.setText("Stop talking know if you want, of course.")
        QApplication.processEvents()
        out = main_transcribe("media\output.wav", self.model_selection.currentText(), self.device)
        final_res = ""
        for elements in out["segments"]:
                start = str(datetime.timedelta(seconds=elements["start"])).split(":", 1)[1]
                end = str(datetime.timedelta(seconds=elements["end"])).split(":", 1)[1]
                text = str(elements["text"])
                final_res = final_res + f"[{start} --> {end}]  {text}\n"
        self.text_warning.setVisible(False)
        pop_up = PopUp(final_res)
        pop_up.exec()


class PopUp(QDialog):
    def __init__(self, text):
        super().__init__()
        self.transcribe = QLabel(text)
        layout = QVBoxLayout()
        layout.addWidget(self.transcribe)
        self.setLayout(layout)