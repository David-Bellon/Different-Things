import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QGraphicsDropShadowEffect
from PySide6.QtGui import QPixmap, QColor, QDrag, QImage
from PySide6.QtCore import Qt, QMimeData
import chess
import torch
import numpy as np
from arqs import Chess

device = torch.device("cuda")
model = Chess().to(device)
state = torch.load(r"models\700k.pt")
model.load_state_dict(state["state_dict"])


class ChessBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.selected = None
        self.main_board = chess.Board()
        self.initUI()

    def setPiece(self, position, color):
        if color == "black":
            if position == 0 or position == 7:
                return "black_pieces/bR.png"
            elif position == 1 or position == 6:
                return "black_pieces/bN.png"
            elif position == 2 or position == 5:
                return "black_pieces/bB.png"
            elif position == 4:
                return "black_pieces/bK.png"
            else:
                return "black_pieces/bQ.png"
        else:
            if position == 0 or position == 7:
                return "white_pieces/wR.png"
            elif position == 1 or position == 6:
                return "white_pieces/wN.png"
            elif position == 2 or position == 5:
                return "white_pieces/wB.png"
            elif position == 4:
                return "white_pieces/wK.png"
            else:
                return "white_pieces/wQ.png"


    def initUI(self):
        self.setGeometry(500, 500, 600, 600)
        self.setWindowTitle("Chess")

        self.board = [[None for _ in range(8)] for _ in range(8)]

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    self.board[i][j] = QLabel(self)
                    self.board[i][j].setScaledContents(True)
                    self.board[i][j].setGeometry(j * 75, i * 75, 75, 75)
                    self.board[i][j].setStyleSheet("background-color: white")
                else:
                    self.board[i][j] = QLabel(self)
                    self.board[i][j].setScaledContents(True)
                    self.board[i][j].setGeometry(j * 75, i * 75, 75, 75)
                    self.board[i][j].setStyleSheet("background-color: gray")

        for i in range(8):
            for j in range(8):
                #Black here
                if i == 0:
                    image = QImage(self.setPiece(j, "black"))
                    pp = QPixmap.fromImage(image)
                    self.board[i][j].setPixmap(pp)
                elif i == 1:
                    image = QImage("black_pieces/bP.png")
                    pp = QPixmap.fromImage(image)
                    self.board[i][j].setPixmap(pp)
                elif i == 6:
                    image = QImage("white_pieces/wP.png")
                    pp = QPixmap.fromImage(image)
                    self.board[i][j].setPixmap(pp)
                elif i == 7:
                    image = QImage(self.setPiece(j, "white"))
                    pp = QPixmap.fromImage(image)
                    self.board[i][j].setPixmap(pp)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            for i in range(8):
                for j in range(8):
                    if self.board[i][j].geometry().contains(event.pos()):
                        piece_board = 8*(7-i) + j
                        if self.selected != None:
                            #New piece selected is another white.
                            if self.main_board.piece_at(piece_board) == None or self.main_board.piece_at(piece_board).color == False:
                                from_square = 8*(7 - self.selected["i"]) + self.selected["j"]
                                to_square = 8*(7-i) + j
                                move = chess.Move(from_square, to_square)
                                if self.main_board.is_legal(move):
                                    self.board[i][j].setPixmap(self.selected["piece"].pixmap())
                                    self.reset_background()
                                    self.selected["piece"].clear()
                                    self.main_board.push(move)
                                    QApplication.processEvents()
                                    #Move black pieces now
                                    self.selected = None
                                    self.black_moves()
                                else:
                                    print("invalid Move")
                            elif self.main_board.piece_at(piece_board).color == True:
                                self.reset_background()
                                piece = self.board[i][j]
                                piece.setStyleSheet("background-color: red")
                                self.selected = {
                                    "piece": piece,
                                    "i": i,
                                    "j": j
                                }
                                event.accept()
                        elif self.main_board.piece_at(piece_board) == None or self.main_board.piece_at(piece_board).color == False:
                            print("Invalid Move")
                        else:
                            piece = self.board[i][j]
                            piece.setStyleSheet("background-color: red")
                            self.selected = {
                                "piece": piece,
                                "i": i,
                                "j": j
                            }
                            event.accept()
                        


    def process_input(self, position):
        pieces = {
            "p": 0,
            "n": 1,
            "b": 2,
            "r": 3,
            "q": 4,
            "P": 5,
            "N": 6,
            "B": 7,
            "R": 8,
            "Q": 9
        }
        w_king_pos = torch.zeros(64)
        b_king_pos = torch.zeros(64)
        w_table = torch.zeros(64, 10)
        b_table = torch.zeros(64, 10)
        for i, square in enumerate(position):
            if square != "/":
                try:
                    number = int(square)
                    for _ in range(number):
                        w_table[63-i] = torch.zeros(10)
                        b_table[i] = torch.zeros(10)
                except:
                    if square == "k" or square == "K":
                        if square == "k":
                            w_king_pos[63-i] = 1
                        else:
                            b_king_pos[i] = 1
                        w_table[63-i] = torch.zeros(10)
                        b_table[i] = torch.zeros(10)
                    else:
                        vis_data = torch.zeros(10)
                        vis_data[pieces[square]] = 1
                        w_table[63-i] = vis_data
                        b_table[i] = vis_data
        white_data = torch.cat([w_king_pos.view(-1), w_table.view(-1)])
        black_data = torch.cat([b_king_pos.view(-1), b_table.view(-1)])
        data = torch.zeros((2, 704)).to(device)
        data[0] = white_data
        data[1] = black_data
        return data

    def black_moves(self):
        moves = list(self.main_board.legal_moves)
        scores = {}
        for move in moves:
            self.main_board.push(move)
            posibles = []
            black_moves = list(self.main_board.legal_moves)
            for black_move in black_moves:
                self.main_board.push(black_move)
                fen = self.main_board.fen().split(" ")[0]
                data = self.process_input(fen)
                out = model(data).item()
                posibles.append(out)
                self.main_board.pop()
                self.main_board.turn = False
            best = np.max(posibles)
            scores[move.uci()] = best
            self.main_board.pop()

        move_id = list(scores.values()).index(np.min(list(scores.values())))
        to_move = moves[move_id]
        self.main_board.push(to_move)
        from_i = 7 - (to_move.from_square // 8)
        from_j = 7 - (8*(to_move.from_square // 8) + 7 - to_move.from_square)
        to_i = 7 - (to_move.to_square // 8)
        to_j = 7 - (8*(to_move.to_square // 8) + 7 - to_move.to_square)

        self.board[to_i][to_j].setPixmap(self.board[from_i][from_j].pixmap())
        self.board[from_i][from_j].clear()

    def reset_background(self):
        if (self.selected["i"] + self.selected["j"]) % 2 == 0:
            self.selected["piece"].setStyleSheet("background-color: white")
        else:
            self.selected["piece"].setStyleSheet("background-color: gray")