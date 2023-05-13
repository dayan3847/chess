import chess
import chess.svg

from checkmate_in.CheckmateIn import CheckmateIn

if __name__ == "__main__":
    print("Chessmate in 3 moves?")
    fen = "5B2/6P1/1p6/8/1N6/kP6/2K5/8 w - - 0 1"
    my_board = chess.Board(fen)
    svg = chess.svg.board(board=my_board)
    with open("exercise_1.svg", "w") as f:
        f.write(svg)

    # Muestra el gráfico SVG en la salida
    # display(SVG(svg))

    _s = CheckmateIn.win_checkmate_in(my_board, 3)
    print("Yes" if _s >= 0 else "No")
