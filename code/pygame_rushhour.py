import pygame
from visualisation.customcolors import COLORS
import random as rd

from classes.models import RushHour


COLOR_NAMES = [name for name in COLORS.keys()]


class PygameRushHour(RushHour):
    def __init__(self, width: int, board_file: str) -> None:
        """ 
        Initalize the game. 
        """
        super().__init__(width, board_file)

        # pygame setup
        pygame.init()

        # Set width and height of the screen 
        self.screen = pygame.display.set_mode((1280, 720))

        # Set internal clock of game 
        self.clock = pygame.time.Clock()
        self.dt = 0

        # Give vehicles a color 
        self.color_vehicles()

    def color_vehicles(self) -> None:
        """ 
        Assign colors to the vehicles. 
        """
        vehicles = self.get_vehicles()
        
        red_used = False
        
        # Assign vehicles a color
        for vehicle in vehicles.values():
            if vehicle.id == "X" and not red_used:
                vehicle.color = "red"
                red_used = True
                COLOR_NAMES.remove("red")
            else:
                vehicle.color = rd.choice(COLOR_NAMES)


    def start(self) -> None:
        """ 
        Start the game and give vehicles a position on the board. 
        """
        running = True
        # Based on pygame quickstart example https://www.pygame.org/docs/
        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the screen with a color to wipe away anything from last frame
            self.screen.fill("white")
            resolution = self.screen.get_size()

            # Assign board a size
            board_size = 600

            # Make sure board is in the middle of the screen 
            board_start_left = (resolution[0] - board_size)//2
            board_start_top = (resolution[1] - board_size)//2

            # Distance between the boxes
            line_spacing = board_size // (self.game_board.width)

            # Create "outside" of board 
            board = pygame.Rect(board_start_left, board_start_top, board_size, board_size)
            pygame.draw.rect(self.screen, "black", board, 3)
            
            # Create the vertical lines 
            for line_y in range(board_start_top + line_spacing, board_start_top + board_size, line_spacing):
                pygame.draw.line(self.screen, "black", (board_start_left, line_y), (board_start_left + board_size - 1, line_y), width=3)

            # Create the horizontal lines  
            for line_x in range(board_start_left + line_spacing, board_start_left + board_size, line_spacing):
                pygame.draw.line(self.screen, "black", (line_x, board_start_top), (line_x, board_start_top + board_size - 1), width=3)
            
            # Make sure there is some white space around the cars 
            car_margin = 10

            vehicles = self.get_vehicles()

            # Give vehicles a position on the board 
            for vehicle in vehicles.values():
                tiles_occupied = vehicle.get_tiles_occupied()
                veh_x = board_start_left + (line_spacing * (tiles_occupied[0][0] - 1)) + car_margin
                veh_y = board_start_top + (line_spacing * (tiles_occupied[0][1] - 1)) + car_margin
                veh_width = line_spacing * (tiles_occupied[-1][0] - tiles_occupied[0][0] + 1) - 2 * car_margin
                veh_height = line_spacing * (tiles_occupied[-1][1] - tiles_occupied[0][1] + 1) - 2 * car_margin

                vehicle_rect = pygame.Rect(veh_x, veh_y, veh_width, veh_height)

                # Vehicle gets placed on the board 
                pygame.draw.rect(self.screen, vehicle.color, vehicle_rect)

            # This will be used later to create a game 
            # TODO: clickable vehicles to move
            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_w]:
            #     self.player_pos.y -= 300 * self.dt
            # if keys[pygame.K_s]:
            #     self.player_pos.y += 300 * self.dt
            # if keys[pygame.K_a]:
            #     self.player_pos.x -= 300 * self.dt
            # if keys[pygame.K_d]:
            #     self.player_pos.x += 300 * self.dt

            # Pop up the display to put your work on screen (or overwrites the screen)
            pygame.display.flip()

            # Limits frames per second (FPS) to 60
            # dt is delta time in seconds since last frame, used for framerate independent physics
            self.dt = self.clock.tick(60) / 1000
        pygame.quit()

    def __del__(self):
        """ 
        End of the game. 
        """
        pygame.quit()

if __name__ == '__main__':
    board_file = "gameboards/Rushhour12x12_7.csv"
    newgame = PygameRushHour(12, board_file)
    newgame.start()
