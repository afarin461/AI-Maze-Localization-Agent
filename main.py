import pygame
import sys
from maze import Maze
from agent import Agent
from gui import GUI


MAZE_FILE = 'mazes/example_maze.txt'
CELL_SIZE = 40 
STEP_LIMIT = 10

def main():
    pygame.init()
    maze = Maze(MAZE_FILE)
    agent = Agent(maze)
    gui = GUI(maze, agent, CELL_SIZE)


    steps = 0
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(5) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    agent.move('N')
                elif event.key == pygame.K_DOWN:
                    agent.move('S')
                elif event.key == pygame.K_LEFT:
                    agent.move('W')
                elif event.key == pygame.K_RIGHT:
                    agent.move('E')
                else:
                    continue

                steps += 1
                gui.update_log(agent.history[-1]) 

                if len(agent.possible_locations) == 1:
                    agent.reveal_location() 
                    gui.update_log("Agent localized to a unique position! True position revealed.")
                    running = False
                elif steps >= STEP_LIMIT:
                    if len(agent.possible_locations) > 1:
                        agent.reveal_location() 
                        gui.update_log("Limit reached. Localization not achieved. Make better decisions next time!")
                        running = False
                    else: 
                        agent.reveal_location()
                        gui.update_log("Step limit reached. True position revealed.")
                        running = False
        
        gui.draw()

    pygame.time.wait(3000)
    
    print(f"Final True Position: {agent.true_position}")
    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()