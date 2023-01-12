import cv2
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from PIL import Image
from torchvision.transforms import ToTensor, ToPILImage
from PySide6.QtGui import QImage, QPixmap
from arqs import Model

def cam_test(window):

    def close_cam():
        cam.release()
        window.label.clear()
        window.out_button.setVisible(False)

    to_tensor = ToTensor()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = torch.load("models\Face_RecognitionV2.plt", map_location=device)

    cam = cv2.VideoCapture(0)
    width = cam.get(3)
    height = cam.get(4)
    model.eval()
    window.out_button.setVisible(True)
    window.out_button.clicked.connect(close_cam)
    while True:
        rate, frame = cam.read()
        source = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image_s = cv2.resize(source, (32, 32))
        input_s = to_tensor(Image.fromarray(image_s)).to(device)
        input_s = input_s[None, :, :, :]
        output_s = model(input_s)
        tlc = int(output_s[0][0].item() * (width - 1))
        brc = int(output_s[0][1].item() * (width - 1))
        tlr = int(output_s[0][2].item() * (height - 1))
        brr = int(output_s[0][3].item() * (height - 1))
        frame = cv2.rectangle(frame, (tlc, tlr), (brc, brr), (0, 0, 255), 2)
        image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_BGR888)
        window.label.setPixmap(QPixmap.fromImage(image))
        #cv2.imshow("video", frame)
        key = cv2.waitKey(1)
        if window.close:
            break