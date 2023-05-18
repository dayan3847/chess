import chess.svg

from dayan3847.checkmate_in.src.CheckmateIn import CheckmateIn

if __name__ == "__main__":
    print("Chessmate in 3 moves?")
    fen = "5B2/6P1/1p6/8/1N6/kP6/2K5/8 w - - 0 1"
    board = chess.Board(fen)
    svg = chess.svg.board(board=board)
    with open("exercise_1.svg", "w") as f:
        f.write(svg)

    # Muestra el gráfico SVG en la salida
    # display(SVG(svg))

    s = CheckmateIn.win_checkmate_in(board, 3)
    print("Yes" if s >= 0 else "No")
