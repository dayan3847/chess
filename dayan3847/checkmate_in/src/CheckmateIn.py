import chess


class CheckmateIn:

    @staticmethod
    def lost_receive_checkmate_in(board: chess.Board, n: int) -> int:
        if n < 0:
            raise ValueError("n cannot be negative")
        if board.is_checkmate():
            # svg = chess.svg.board(board=my_board)
            # with open("is_checkmate.svg", "w") as f:
            #     f.write(svg)
            return 0
        if board.is_stalemate():
            return -1
        if n == 0:
            return -1
        i_receive_checkmate_in = -1
        for move in board.legal_moves:
            board.push(move)
            s = CheckmateIn.win_checkmate_in(board, n)
            board.pop()
            if s < 0:
                return s
            if s > i_receive_checkmate_in:
                i_receive_checkmate_in = s
        return i_receive_checkmate_in

    @staticmethod
    def win_checkmate_in(board: chess.Board, n: int) -> int:
        if n <= 0:
            raise ValueError("n cannot be negative")
        if board.is_checkmate():
            return -1
        for move in board.legal_moves:
            board.push(move)
            s = CheckmateIn.lost_receive_checkmate_in(board, n - 1)
            board.pop()
            if s >= 0:
                return s
        return -1
