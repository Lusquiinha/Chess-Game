import pygame

WHITE = (200, 200, 200)
BLACK = (100, 100, 100)
YELLOW = (255,255,0)

DEFAULT_BOARD = [
            'rnbqkbnr',
            'pppppppp',
            '        ',
            '        ',
            '        ',
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
            image_path = f'assets/{piece}.png'
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

    def draw(self, screen):
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                if(row, col) == self.selected_square:
                    color = YELLOW
                pygame.draw.rect(screen, color, (col * 100, row * 100, 100, 100))

                piece = self.board[row][col]
                if piece:
                    self.draw_piece(screen, piece, row, col)

    def draw_piece(self, screen, piece, row, col):
        if piece and piece != ' ':
            piece_img = self.piece_image[piece]  # Convert to lowercase for consistency
            screen.blit(piece_img, (col * 100 + 10, row * 100 + 10))

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
            if not self.check_same_colors(self.selected_square, new_pos):
                self.swap_pos(self.selected_square, new_pos)
                self.board[self.selected_square[0]][self.selected_square[1]] = ' '
            self.selected_square = None
        else: #não há peças selecionadas
            self.selected_square = self.get_square_at_pixel(mouse_x, mouse_y)

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