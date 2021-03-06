from chess import *
from check_valid_moves import *

wP = Piece(Type.PAWN, Color.WHITE)
wN = Piece(Type.KNIGHT, Color.WHITE)
wB = Piece(Type.BISHOP, Color.WHITE)
wR = Piece(Type.ROOK, Color.WHITE)
wQ = Piece(Type.QUEEN, Color.WHITE)
wK = Piece(Type.KING, Color.WHITE)

bP = Piece(Type.PAWN, Color.BLACK)
bN = Piece(Type.KNIGHT, Color.BLACK)
bB = Piece(Type.BISHOP, Color.BLACK)
bR = Piece(Type.ROOK, Color.BLACK)
bQ = Piece(Type.QUEEN, Color.BLACK)
bK = Piece(Type.KING, Color.BLACK)

sample_board_1 = Board(
    [[wR, wN, wB, wQ, wK, wB, wN, wR],
     [wP, wP, wP, wP, wP, wP, wP, wP],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [bP, bP, bP, bP, bP, bP, bP, bP],
     [bR, bN, bB, bQ, bK, bB, bN, bR]]
)
sample_board_2 = Board(
    [[wR, None, wB, None, wK, wB, wN, wR],
     [wP, wP, wP, None, wP, wP, wP, wP],
     [None, None, None, None, None, None, None, None],
     [None, None, None, wP, None, None, None, None],
     [None, None, None, bP, None, None, None, None],
     [None, None, wN, None, None, None, None, None],
     [bP, bP, bP, None, bP, bP, bP, bP],
     [bR, bN, bB, bQ, bK, bB, bN, bR]]
)
sample_board_3 = Board(
    [[wR  , None, wB  , None, wK  , wB  , wN  , wR  ],
     [wP  , wP  , wP  , None, wP  , wP  , wP  , wP  ],
     [None, None, None, None, None, None, None, None],
     [None, bB  , None, wP  , None, None, None, None],
     [None, None, None, bP  , None, None, None, None],
     [None, None, wN  , None, None, None, None, None],
     [bP  , bP  , bP  , None, None, bP  , bP  , bP  ],
     [bR  , bN  , bB  , bQ  , bK  , None, bN  , bR  ]]
)

sample_board_4 = Board(
[[bR, bN, bB, bQ, bK, bB, bN, bR],
[bP,None, bP, bP, bP, bP, bP, bP],
[None,None,None,None,None,None,None,None],
[None, bP,None,None,None,None,None,None],
[None,None,None,None,None,None,None,None],
[None, wP,None,None,None,None,None,None],
[wP,None, wP, wP, wP, wP, wP, wP],
[wR, wN, wB, wQ, wK, wB, wN, wR]]
)


# check_material_value(board_input) returns a list of length 2 in form [int, int]
# the first int is the total material of white's pieces
# the second int is the total material of black's pieces
def check_material_value(board_input):
    white_mat = 0
    black_mat = 0
    for row in board_input.board:
        for piece in row:
            if piece is not None:
                if piece == wP:
                    white_mat += 1
                elif piece == wN or piece == wB:
                    white_mat += 3
                elif piece == wR:
                    white_mat += 5
                elif piece == wQ:
                    white_mat += 9
                elif piece == wK:
                    white_mat -= 100
                elif piece == bP:
                    black_mat += 1
                elif piece == bN or piece == bB:
                    black_mat += 3
                elif piece == bR:
                    black_mat += 5
                elif piece == bQ:
                    black_mat += 9
                elif piece == bK:
                    black_mat -= 100
    return [white_mat, black_mat]


# returns a num from low to high depending on if a piece has good activity
# return type is [whiteVal, blackVal]
def controls_centre(piece_input, x, y):
    white_val = 0
    black_val = 0
    if piece_input is not None:
        if piece_input == wP:
            if (x == 2 and y == 2) or (x == 5 and y == 2) or (x == 2 and y == 3) or (x == 5 and y == 3) or (
                    x == 3 and y == 2) or (x == 4 and y == 2):
                white_val += 0.2
            elif (x == 3 and y == 3) or (x == 4 and y == 3):
                white_val += 0.4
            elif (x == 3 and y == 4) or (x == 4 and y == 4):
                white_val += 0.3
            else:
                white_val += 0
        elif piece_input == wN:
            if (x, y) in [(1, 2), (1, 3), (2, 1), (3, 1), (4, 1), (5, 1), (6, 2), (6, 3),
                          (1, 5), (1, 4), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4)]:
                white_val += 0.2
            if (x, y) in [(2, 2), (5, 2), (2, 5), (5, 5)]:
                white_val += 0.4
            if (x, y) in [(3, 3), (4, 3), (3, 4), (4, 4), (2, 3), (2, 4), (3, 2), (4, 2), (5, 3), (5, 4), (3, 5),
                          (3, 6)]:
                white_val += 0.3
            if y in range(5, 7):
                white_val += 0.1
        elif piece_input == wB:
            if (x, y) in [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                          (0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)]:
                white_val += 0.2
            if x in range(2, 6) and y in range(2, 6):
                white_val += 0.1
        elif piece_input == wR:
            if x in [3, 4]:
                white_val += 0.1
            if y in [3, 4]:
                white_val += 0.1
        elif piece_input == wQ:
            if (x, y) in [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                          (0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)]:
                white_val += 0.1
            if x in [3, 4]:
                white_val += 0.1
            if y in [3, 4]:
                white_val += 0.1
        elif piece_input == bP:
            if (x == 2 and y == 5) or (x == 5 and y == 5) or (x == 2 and y == 4) or (x == 5 and y == 4) or (
                    x == 3 and y == 5) or (x == 4 and y == 5):
                black_val += 0.2
            elif (x == 3 and y == 4) or (x == 4 and y == 4):
                black_val += 0.4
            elif (x == 3 and y == 3) or (x == 4 and y == 3):
                black_val += 0.3
            else:
                black_val += 0
        elif piece_input == bN:
            if (x, y) in [(1, 2), (1, 3), (2, 1), (3, 1), (4, 1), (5, 1), (6, 2), (6, 3),
                          (1, 5), (1, 4), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4)]:
                black_val += 0.2
            if (x, y) in [(2, 2), (5, 2), (2, 5), (5, 5)]:
                black_val += 0.4
            if (x, y) in [(3, 3), (4, 3), (3, 4), (4, 4), (2, 3), (2, 4), (3, 2), (4, 2), (5, 3), (5, 4), (3, 5),
                          (3, 6)]:
                black_val += 0.3
            if y in range(1, 3):
                black_val += 0.1
        elif piece_input == bB:
            if (x, y) in [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                          (0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)]:
                black_val += 0.2
            if x in range(2, 6) and y in range(2, 6):
                black_val += 0.1
        elif piece_input == bR:
            if x in [3, 4]:
                black_val += 0.1
            if y in [3, 4]:
                black_val += 0.1
        elif piece_input == bQ:
            if (x, y) in [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                          (0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)]:
                black_val += 0.1
            if x in [3, 4]:
                black_val += 0.1
            if y in [3, 4]:
                black_val += 0.1
    return [white_val, black_val]
# check_centre_points(board_input) returns a list of length 2 in form [num, num]
# the first num is the total material of white's pieces
# the second num is the total material of black's pieces
def check_piece_activity(board_input):
    white_centre = 0
    black_centre = 0
    for x in range(0, 8):
        for y in range(0, 8):
            points_list = controls_centre(board_input.get(x, y), x, y)
            white_centre += points_list[0]
            black_centre += points_list[1]
    #return [0,0]
    return [white_centre, black_centre]


# returns a num from low to high depending on pawn activity - how close it is to promotion
# return type is [whiteVal, blackVal]
def check_close_to_promotion(board_input):
    white_val = 0
    black_val = 0
    for x in range(0, 8):
        for y in range(5, 8):
            if board_input.get(x, y) is not None and board_input.get(x, y) == wP:
                white_val += (0.1 * y) - 0.4
        for y in range(1, 4):
            if board_input.get(x, y) is not None and board_input.get(x, y) == bP:
                black_val += 0.4 - (0.1 * y)
    return [white_val, black_val]


def check_king_safety(board_input):
    return [0,0]
    # checks and evaluates king safety given a board, returns a list of two nums
    white_eval = 0
    black_eval = 0
    wK_pos = board_input.search(Piece(Type.KING, Color.WHITE))[0]
    bK_pos = board_input.search(Piece(Type.KING, Color.BLACK))[0]
    white_material = check_material_value(board_input)[0]
    black_material = check_material_value(board_input)[1]
    if white_material >= 18 and black_material >= 18:
        if wK_pos[0] in [3, 4]:
            white_eval -= 0.1
        if bK_pos[0] in [3, 4]:
            black_eval -= 0.1
        if wK_pos[1] == 2:
            white_eval -= 0.5
        if bK_pos[1] == 2:
            black_eval -= 0.5
        if wK_pos[1] > 2:
            white_eval -= 1.5
        if bK_pos[1] > 2:
            black_eval -= 1.5
    elif white_material < 18 and black_material < 18:
        if wK_pos[0] in [0, 7] or wK_pos[1] in [0, 7]:
            white_eval -= 0.2
        if bK_pos[0] in [0, 7] or bK_pos[1] in [0, 7]:
            black_eval -= 0.2
    else:
        if white_material > black_material:
            if wK_pos[1] >= 2:
                white_eval -= 0.1
        elif black_material > white_material:
            if bK_pos[1] <= 5:
                black_eval -= 0.1
    return [white_eval, black_eval]


# Gives the player a bonus for having two bishops of +0.2, or +0.3 if less pawns are present on the board
def check_double_bishop(board_input):
    white_eval = 0
    black_eval = 0
    less_than_10_pawns = len(board_input.search(wP)) + len(board_input.search(bP)) <= 10
    if len(board_input.search(wB)) == 2:
        white_eval += 0.2
        if less_than_10_pawns:
            white_eval += 0.1
    if len(board_input.search(bB)) == 2:
        black_eval += 0.2
        if less_than_10_pawns:
            black_eval += 0.1
    return [white_eval, black_eval]


# Gives players with knights a bonus of +0.1 for being in crowded situations
def check_knight_bonus(board_input):
    white_eval = 0
    black_eval = 0
    if len(board_input.search(wP)) + len(board_input.search(bP)) >= 14:
        for white_knight in board_input.search(wN):
            white_eval += 0.1
        for black_knight in board_input.search(bN):
            black_eval += 0.1
    return [white_eval, black_eval]


def check_king_threat(board_input):
    white_eval = 0
    black_eval = 0
    wK_pos = board_input.search(wK)[0]
    bK_pos = board_input.search(bK)[0]
    wK_surrounding = [wK_pos]
    bK_surrounding = [wK_pos]
    for x in range(wK_pos[0] - 1, wK_pos[0] + 2):
        for y in range(wK_pos[1] - 1, wK_pos[1] + 2):
            if x in range(0, 8) and y in range(0, 8):
                wK_surrounding.append((x, y))
    for x in range(bK_pos[0] - 1, bK_pos[0] + 2):
        for y in range(bK_pos[1] - 1, bK_pos[1] + 2):
            if x in range(0, 8) and y in range(0, 8):
                bK_surrounding.append((x, y))
    for x in range(0, 8):
        for y in range(0, 8):
            piece = board_input.get(x, y)
            if piece is not None:
                if piece.color == Color.WHITE:
                    for i in bK_surrounding:
                        if i in valid_moves(x, y, board_input):
                            white_eval += 0.1
                if piece.color == Color.BLACK:
                    for i in wK_surrounding:
                        if i in valid_moves(x, y, board_input):
                            black_eval += 0.1
    # return [0,0]
    return [white_eval, black_eval]


def check_checkmated(board_input):
    #return[0,0]
    """Checks if one side on the board is checkmated
    TODO: don't compute len of list of possible moves while in check. Instead, break when the first move is found"""

    if is_in_check(board_input, Color.WHITE):
        for x in range(0, 8):
            for y in range(0, 8):
                if board_input.get(x, y) is not None and board_input.get(x, y).color == Color.WHITE:
                    for move in valid_moves(x, y, board_input):
                        c = board_input.copy()
                        c.move_piece(x, y, move[0], move[1])
                        if not is_in_check(c, Color.WHITE):
                            return [0, 0]
        return [-1000000000, 0]
    if is_in_check(board_input, Color.BLACK):
        for x in range(0, 8):
            for y in range(0, 8):
                if board_input.get(x, y) is not None and board_input.get(x, y).color == Color.BLACK:
                    for move in valid_moves(x, y, board_input):
                        c = board_input.copy()
                        c.move_piece(x, y, move[0], move[1])
                        if not is_in_check(c, Color.BLACK):
                            return [0, 0]
        return [0, -1000000000]
    return [0, 0]





'''
print(check_material_value(sample_board_1))
print(check_piece_activity(sample_board_1))
print(check_close_to_promotion(sample_board_1))
print(check_king_safety(sample_board_1))

print(check_material_value(sample_board_2))
print(check_piece_activity(sample_board_2))
print(check_close_to_promotion(sample_board_2))
print(check_king_safety(sample_board_2))
'''


def eval_board_state(board_input):
    #return[0,0]
    white_result = check_material_value(board_input)[0] + check_piece_activity(board_input)[0] + \
                   check_close_to_promotion(board_input)[0] + \
                   check_checkmated(board_input)[0] + check_double_bishop(board_input)[0] + \
                   check_knight_bonus(board_input)[0] + check_king_safety(board_input)[0]
    black_result = check_material_value(board_input)[1] + check_piece_activity(board_input)[1] + \
                   check_close_to_promotion(board_input)[1] + \
                   check_checkmated(board_input)[1] + check_double_bishop(board_input)[1] + \
                   check_knight_bonus(board_input)[1] + check_king_safety(board_input)[1]
    return white_result - black_result

'''
print(eval_board_state(sample_board_1))
print(eval_board_state(sample_board_2))
print(eval_board_state(sample_board_3))
'''