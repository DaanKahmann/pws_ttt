import itertools
from copy import deepcopy

# define all rotations (clockwise)
_rotations = [
    [
        [(2, 0), (1, 0), (0, 0)],
        [(2, 1), (1, 1), (0, 1)],
        [(2, 2), (1, 2), (0, 2)]
    ],
    [
        [(2, 2), (2, 1), (2, 0)],
        [(1, 2), (1, 1), (1, 0)],
        [(0, 2), (0, 1), (0, 0)]
    ],
    [
        [(0, 2), (1, 2), (2, 2)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 0), (1, 0), (2, 0)]
    ]
]

# flip along vertical axis
_flip = [
    [(0, 2), (0, 1), (0, 0)],
    [(1, 2), (1, 1), (1, 0)],
    [(2, 2), (2, 1), (2, 0)]
]

_win_conditions = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],

    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],

    [(0, 0), (1, 1), (2, 2)],
    [(2, 0), (1, 1), (0, 2)],
]


# returns a state based on an original state and a translation matrix
def _translate(state, translation):
    new_state = [[state[cell[0]][cell[1]] for cell in row] for row in translation]
    return new_state


# returns a flattened, string version of a state
def _state_str(state):
    return_string = ""
    for line in state:
        return_string += "{} | {} | {}\n".format(line[0], line[1], line[2])
    return return_string


# compare all variations of the board and return the one with the smallest string representation
def _get_minimal_rotation(state):
    smallest_state = state
    flipped = False
    rotated = [[(0, 0), (0, 1), (0, 2)],
                [(1, 0), (1, 1), (1, 2)],
                [(2, 0), (2, 1), (2, 2)]]

    # check if the flipped state is smaller
    flipped_state = _translate(state, _flip)
    if _state_str(flipped_state) < _state_str(smallest_state):
        smallest_state = flipped_state
        flipped = True

    # check all rotations of both regular and flipped
    for rotation in _rotations:
        if _state_str(_translate(state, rotation)) < _state_str(smallest_state):
            smallest_state = _translate(state, rotation)
            rotated = rotation
            flipped = False
        if _state_str(_translate(flipped_state, rotation)) < _state_str(smallest_state):
            smallest_state = _translate(flipped_state, rotation)
            rotated=rotation
            flipped = True

    return smallest_state, flipped, rotated


# return the state with a specific cell changed to value
# TODO: make it so you could call board[x, y] = value to a get a new board with that change
def _state_set_cell(state, coordinate, value):
    new_state = deepcopy(state)
    new_state[coordinate[0]][coordinate[1]] = value
    return new_state


class Board:
    def __str__(self):
        return _state_str(self.state)

    # Make it possible to use == on two boards
    def __eq__(self, other):
        smallest, _, _ = _get_minimal_rotation(self.state)
        other_smallest, _, _ = _get_minimal_rotation(other.state)
        return _state_str(smallest) == _state_str(other_smallest)

    # Allows Boards to be used as the key in a set
    def __hash__(self):
        smallest, _, _ = _get_minimal_rotation(self.state)
        return hash(str(_state_str(smallest)))

    def __init__(self, state=None, minimal=False):
        # If no initial state is give, generate an empty board
        # Otherwise, use the given state
        if state is None:
            self.state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        elif minimal:
            self.state, _, _ = _get_minimal_rotation(deepcopy(state))
        else:
            self.state = state

    # Returns 'False' if there is no winner yet
    # Returns 1 or 2 to indicate the winning player, or 3 to indicate a draw
    def winner(self):   #geeft aan wie wint of geeft aan dat het een gelijkspel is.
        for condition in _win_conditions:
            # A win condition is always a list of 3 coordinates
            if self.cell(condition[0]) == self.cell(condition[1]) == self.cell(condition[2]):
                # "empty" cells do not represent a win condition...
                if self.cell(condition[0]) != 0:
                    return self.cell(condition[0])
        else:
            if self.ronde() == 9:
                # No win condition but the board is full, this is a draw
                return 3
            return False

    def mogelijkheden(self, uniek=True):    #geeft de mogelijkheden die de speler heeft om een X of een O neer te zetten
        moves = {}
        potential_moves = [[(x, y) for y in range(3) if self.state[x][y] == 0] for x in range(3)]
        if uniek:
            for potential_move in itertools.chain(*potential_moves):
                moves[Board(state=_state_set_cell(self.state, potential_move, self.speler()))] = potential_move
            return list(moves.values())
        else:
            return list(itertools.chain(*potential_moves))

    # def draw_board(self):   #geeft het bord (we weten niet zeker of deze wel nodig is)
    '''
    Draw hoort meer mij de GUI naar mijn mening.
    Dat gezegd hebbende willen we wel de waarde in een cell op kunnen vragen. Op die manier kan bijvoorbeeld de GUI het
    goede symbool voor een specifieke locatie achterhalen.
    '''
    def cell(self, coordinate):
        return self.state[coordinate[0]][coordinate[1]]

    '''
    De volgende functies hebben jullie niet gevraagd maar had ik wel, misschien heb je er iets aan?
    '''

    # The most recent move is equal to the number of none zero cells
    # i.e. the most recent move on a board with one cell set was the first move
    def ronde(self):
        count = 0
        for cell in itertools.chain(*self.state):
            if cell > 0:
                count += 1
        return count

    def make_move(self, coordinate, player=None, minimal=False):
        if player is not None and player is not self.speler():
            raise ValueError('It is not that player\'s move')
        if self.state[coordinate[0]][coordinate[1]] != 0:
            print("oeps!!")
            return self
        new_state = _state_set_cell(self.state, coordinate, self.speler())
        return Board(new_state, minimal)

    # Returns the player who should make the next move (player 1 or player 2)
    def speler(self):
        return (self.ronde() % 2) + 1

    def translate(self, other_board, coordinate):
        if other_board.is_minimal():
            minimal_state, flipped, rotated = _get_minimal_rotation(self.state)
            coordinate = rotated[coordinate[0]][coordinate[1]]
            if flipped:
                coordinate = _flip[coordinate[0]][coordinate[1]]
            return coordinate
        else:
            raise ValueError('second board should be in minimal state')

    def is_minimal(self):
        _, flipped, rotated = _get_minimal_rotation(self.state)
        if ( flipped not in _flip and rotated not in _rotations):
            return True
        else:
            return False