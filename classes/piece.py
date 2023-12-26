import pygame

class Piece:
    def __init__(self, board, pos):
        self.board = board
        self.pos = pos

    def colision(self, row, col):
        if self.board[row][col] != ' ':
            return True
        return False    
    
    def check_same_colors(self, pos2):
        res1 = self.board[self.pos[0]][self.pos[1]].islower()
        res2 = self.board[pos2[0]][pos2[1]].islower()
        res3 = self.board[self.pos[0]][self.pos[1]].isspace()
        res4 = self.board[pos2[0]][pos2[1]].isspace()
        return (res1 == res2) and not(res3 or res4)
    
    def torre_moves(self):
        row, col = self.pos
        moves = []
        for i in range(row+1, 8):
            if self.colision(i, col):
                if not self.check_same_colors((i, col)):
                    moves.append((i, col))
                break
            moves.append((i,col))
        for i in range(row-1, -1, -1):
            if self.colision(i, col):
                if not self.check_same_colors((i, col)):
                    moves.append((i, col))
                break
            moves.append((i,col))
        for i in range(col+1, 8):
            if self.colision(row, i):
                if not self.check_same_colors((row, i)):
                    moves.append((row, i))
                break
            moves.append((row,i))
        for i in range(col-1, -1, -1):
            if self.colision(row, i):
                if not self.check_same_colors((row, i)):
                    moves.append((row, i))
                break
            moves.append((row,i))
        return moves

    def rainha_moves(self):
        moves = self.torre_moves()
        moves.extend(self.bispo_moves())
        return moves

    def rei_moves(self):
        row, col = self.pos
        moves = []
        destinies = [(row-1, col-1),
                     (row-1, col),
                     (row-1, col+1),
                     (row, col-1),
                     (row, col+1),
                     (row+1, col-1),
                     (row+1, col),
                     (row+1, col+1)]
        
        for r, c in destinies:
            if (-1 < r < 8) and (-1 < c < 8):
                if not self.check_same_colors((r,c)):
                    moves.append((r,c))
        return moves

    def cavalo_moves(self):
        row, col = self.pos
        moves = []
        destinies = [(row+2, col+1),
                     (row+2, col-1),
                     (row-2, col+1),
                     (row-2, col-1),
                     (row+1, col+2),
                     (row+1, col-2),
                     (row-1, col+2),
                     (row-1, col-2)]
        
        for r, c in destinies:
            if (-1 < r < 8) and (-1 < c < 8):
                if not self.check_same_colors((r,c)):
                    moves.append((r,c))
        return moves

    def bispo_moves(self):
        row, col = self.pos
        moves = []
        for i in range(1, min(8-row, 8-col)):
            if self.colision(row+i, col+i):
                if not self.check_same_colors((row+i, col+i)):
                    moves.append((row+i, col+i))
                break
            moves.append((row+i, col+i))
        for i in range(1, min(row+1, 8-col)):
            if self.colision(row-i, col+i):
                if not self.check_same_colors((row-i, col+i)):
                    moves.append((row-i, col+i))
                break
            moves.append((row-i, col+i))
        for i in range(1, min(row+1, col+1)):
            if self.colision(row-i, col-i):
                if not self.check_same_colors((row-i, col-i)):
                    moves.append((row-i, col-i))
                break
            moves.append((row-i, col-i))
        for i in range(1, min(8-row, col+1)):
            if self.colision(row+i, col-i):
                if not self.check_same_colors((row+i, col-i)):
                    moves.append((row+i, col-i))
                break
            moves.append((row+i, col-i))
        return moves

    def peao_moves(self):
        row, col = self.pos
        moves = []
        if self.board[row][col].isupper():
            if self.board[row-1][col] == ' ':
                moves.append((row-1,col))
            if row == 6:
                moves.append((row-2, col))
            if col+1 < 8 and self.board[row-1][col+1].islower():
                moves.append((row-1,col+1))
            if col-1 > 0 and self.board[row-1][col-1].islower():
                moves.append((row-1,col-1))
            return moves
        else:
            if self.board[row+1][col] == ' ':
                moves.append((row+1,col))
            if row == 1:
                moves.append((row+2, col))
            if col+1 < 8 and self.board[row+1][col+1].isupper():
                moves.append((row+1,col+1))
            if col-1 > 0 and self.board[row+1][col-1].isupper():
                moves.append((row+1,col-1))
            return moves
        



    def get_possible_moves(self):
        match self.board[self.pos[0]][self.pos[1]]:
            case 'R' | 'r':
                return self.torre_moves()
            case 'P' | 'p':
                return self.peao_moves()
            case 'N' | 'n':
                return self.cavalo_moves()
            case 'Q' | 'q':
                return self.rainha_moves()
            case 'K' | 'k':
                return self.rei_moves()
            case 'B' | 'b':
                return self.bispo_moves()
            case _:
                return []
                