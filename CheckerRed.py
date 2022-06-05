class Checker_Red:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.posible_move = []
        self.posible_kill = []
    
    def possible_options(self, fields_pos):
        start_dir = ((-1, -1), (1, -1))
        for delta in start_dir:
            if fields_pos[self.i + delta[0]][self.j + delta[1]] == '-':
                self.posible_move.append((self.i + delta[0], self.j + delta[1]))
            elif fields_pos[self.i + delta[0]][self.j + delta[1]] == 'b':
                self.check_kill(self.i + delta[0]*2, self.j + delta[1]*2, fields_pos)
    
    def __repr__(self):
        return f'<Checker_Red i:{self.i}, j:{self.j}>'

    @classmethod
    def check_kill(self, x, y, fields_pos):
        if fields_pos[x][y] != '-':
            return
        start_dir = ((-1, -1), (1, -1))
        for delta in start_dir:
            if fields_pos[x + delta[0]][y + delta[1]] != 'b':
                pass
            else:
                self.check_kill(x + delta[0]*2, y + delta[1]*2, fields_pos)