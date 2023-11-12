import chess
import chess.svg
import tkinter as tk
from PIL import Image, ImageTk
import cairosvg
from io import BytesIO

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.board = chess.Board()
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.draw_board()

    def draw_board(self):
        board_svg = chess.svg.board(self.board)
        board_png = self.svg_to_png(board_svg)
        self.tk_image = ImageTk.PhotoImage(board_png)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def svg_to_png(self, svg_data):
        png_data = cairosvg.svg2png(bytestring=svg_data.encode())
        png_image = Image.open(BytesIO(png_data))
        return png_image

if __name__ == "__main__":
    root = tk.Tk()
    chess_game = ChessGame(root)
    root.mainloop()

