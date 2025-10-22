import random

class Agent:
    def __init__(self, maze):
        self.maze = maze
        self.possible_locations = set([(x, y) for y in range(maze.height) for x in range(maze.width) if not maze.is_wall(x, y)])
        self.true_position = random.choice(list(self.possible_locations))
        self.history = [("Initial", f"Possible locations: {len(self.possible_locations)}")]
        self.true_path_history = [] 

        self.revealed = False 

    def move(self, direction):
        dx, dy = {'N': (0, -1), 'S': (0, 1), 'W': (-1, 0), 'E': (1, 0)}[direction]
        
        prev_true_x, prev_true_y = self.true_position
        new_true_x, new_true_y = prev_true_x + dx, prev_true_y + dy

        if not self.maze.is_wall(new_true_x, new_true_y):
            self.true_position = (new_true_x, new_true_y)
        
        current_percept = self.maze.get_percept(self.true_position[0], self.true_position[1])
        
        self.true_path_history.append((prev_true_x, prev_true_y, direction, current_percept))
        
        self._update_belief_state()

        self.history.append(f"Attempted {direction}. Percept: {''.join(map(str, current_percept))}. Possible: {len(self.possible_locations)}")

    def _update_belief_state(self):
        newly_possible_locations = set()

        all_free_cells = [(x, y) for y in range(self.maze.height) for x in range(self.maze.width) if not self.maze.is_wall(x, y)]

        for initial_candidate_x, initial_candidate_y in all_free_cells:
            current_sim_x, current_sim_y = initial_candidate_x, initial_candidate_y
            
            is_consistent_path = True
            
            for prev_true_x, prev_true_y, attempted_direction, actual_percept in self.true_path_history:
                
                dx, dy = {'N': (0, -1), 'S': (0, 1), 'W': (-1, 0), 'E': (1, 0)}[attempted_direction]
                
                next_sim_x, next_sim_y = current_sim_x + dx, current_sim_y + dy
                
                if self.maze.is_wall(next_sim_x, next_sim_y):
                    pass 
                else:
                    current_sim_x, current_sim_y = next_sim_x, next_sim_y

                simulated_percept = self.maze.get_percept(current_sim_x, current_sim_y)
                
                if simulated_percept != actual_percept:
                    is_consistent_path = False
                    break 

            if is_consistent_path:
                newly_possible_locations.add((current_sim_x, current_sim_y))
        
        self.possible_locations = newly_possible_locations

    def reveal_location(self):
        
        self.revealed = True
        