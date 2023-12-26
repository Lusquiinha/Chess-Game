import pygame
from classes.piece import Piece

WHITE = (200, 200, 200)
BLACK = (100, 100, 100)
YELLOW = (255,255,0)
DARK_BLACK = (0,255,50)

DEFAULT_BOARD = [
            'rnbqkbnr',
            'pppppppp',
            '        ',
            ' R      ',
            '     r  ',
            '        ',
            'PPPPPPPP',
            'RNBQKBNR',
        ]

class ChessBoard:
    def __init__(self):
        self.board = self.initialize_board()
        self.initialize_images()
        self.selected_square = None

    def initialize_images(self):
        self.piece_image = {}
        pieces = ['r','n','b','q','k','p','R','N','B','Q','K','P']

        for piece in pieces:
            image_path = f"assets/{'white' if piece.isupper() else 'black'}-{piece}.png"
            image = pygame.image.load(image_path)
            self.piece_image[piece] = pygame.transform.scale(image, (80, 80))
            

    
    def initialize_board(self):
        # Initialize an 8x8 chessboard
        board = [['' for _ in range(8)] for _ in range(8)]

        # Set up the initial chess position (you can customize this)
        # For simplicity, 'p' represents black pawn, 'P' represents white pawn
        # 'r', 'n', 'b', 'q', 'k' for black, 'R', 'N', 'B', 'Q', 'K' for white
        initial_position = DEFAULT_BOARD

        for row in range(8):
            for col in range(8):
                board[row][col] = initial_position[row][col]

        return board
    
    def update(self):
        for i, item in enumerate(self.board[0]):
            if item == 'P':
                self.board[0][i] = 'Q'
        for i, item in enumerate(self.board[7]):
            if item == 'p':
                self.board[7][i] = 'q'

    def draw(self, screen):
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                if(row, col) == self.selected_square:
                    color = YELLOW
                pygame.draw.rect(screen, color, (col * 100, row * 100, 100, 100))
        
        self.draw_possible_moves(screen)
        
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    self.draw_piece(screen, piece, row, col)

    def draw_piece(self, screen, piece, row, col):
        if piece and piece != ' ':
            piece_img = self.piece_image[piece]  
            screen.blit(piece_img, (col * 100 + 10, row * 100 + 10))

    def draw_possible_moves(self, screen):
        if not self.selected_square:
            return
        moves = self.piece_possible_moves(self.selected_square)
        if not moves:
            return
        for col, row in moves:
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, DARK_BLACK, pygame.Rect(row*100 +1   , col*100+1    , 98, 98))
            pygame.draw.rect(screen, color , pygame.Rect(row*100 + 5, col*100 + 5, 90 , 90))
        

    def get_square_at_pixel(self, x, y):
        col = x // 100
        row = y // 100
        if 0 <= row < 8 and 0 <= col < 8:
            if self.board[row][col] != ' ' or self.selected_square:
                return row, col
        return None
    
    def select_square(self, mouse_x, mouse_y):
        if self.selected_square: #já tem uma peçã selecionada
            new_pos = self.get_square_at_pixel(mouse_x, mouse_y)
            self.move_piece(new_pos)
        else: #não há peças selecionadas
            self.selected_square = self.get_square_at_pixel(mouse_x, mouse_y)

    def move_piece(self, new_pos):
        possible_moves = self.piece_possible_moves(self.selected_square)
        if new_pos in possible_moves:
            self.swap_pos(self.selected_square, new_pos)
            self.board[self.selected_square[0]][self.selected_square[1]] = ' '
            self.selected_square = None
            return
        if self.board[new_pos[0]][new_pos[1]] != ' ':
            self.selected_square = new_pos
            return
        self.selected_square = None    
            
        

    def swap_pos(self, pos1, pos2):
        self.board[pos1[0]][pos1[1]],self.board[pos2[0]][pos2[1]] = self.board[pos2[0]][pos2[1]],self.board[pos1[0]][pos1[1]]
    
    def check_same_colors(self, pos1, pos2):
        res1 = self.board[pos1[0]][pos1[1]].islower()
        res2 = self.board[pos2[0]][pos2[1]].islower()
        res3 = self.board[pos1[0]][pos1[1]].isspace()
        res4 = self.board[pos2[0]][pos2[1]].isspace()
        return (res1 == res2) and not(res3 or res4)
    
    def reset(self):
        self.board = self.initialize_board()
    
    def delete_selected(self):
        if self.selected_square:
            self.board[self.selected_square[0]][self.selected_square[1]] = ' '
            self.selected_square = None

    def player_possible_moves(self, player):
        pieces = self.find_pieces(player)
        moves = {}
        for piece in pieces:
            moves[piece] = self.piece_possible_moves(piece)
            
    def find_pieces(self, player):
        pass

    def piece_possible_moves(self, piece_pos):
        piece = Piece(self.board, piece_pos)
        return piece.get_possible_moves()

