class Maze:
    def __init__(self, filename):
        self.grid = []
        with open(filename, 'r') as f:
            for line in f:
                self.grid.append([int(c) for c in line.strip()])
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def is_wall(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True
        return self.grid[y][x] == 1 

    def get_percept(self, x, y):
        n_wall = self.is_wall(x, y - 1)
        s_wall = self.is_wall(x, y + 1)
        e_wall = self.is_wall(x + 1, y)
        w_wall = self.is_wall(x - 1, y)
        return (int(n_wall), int(s_wall), int(e_wall), int(w_wall))