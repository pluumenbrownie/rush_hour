import pygame
from visualisation.customcolors import COLORS
import random as rd
import csv

from classes.models import RushHour


COLOR_NAMES = [name for name in COLORS.keys()]


class PygameRushHour(RushHour):
    def __init__(self, width: int, board_file: str, solution_file: str|None = None) -> None:
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

        self.vehicles = self.get_vehicles()

        # Give vehicles a color 
        self.color_vehicles()

        # Assign board a size
        self.board_size = 600
        # Make sure there is some white space around the cars 
        self.car_margin = 10
        self.resolution = self.screen.get_size()

        # Make sure board is in the middle of the screen 
        self.board_start_left = (self.resolution[0] - self.board_size)//2
        self.board_start_top = (self.resolution[1] - self.board_size)//2

        # Distance between the boxes
        self.line_spacing = self.board_size // (self.game_board.width)

        self.solution_moves: list[tuple[str, int]] = []
        if solution_file:
            with open(solution_file, 'r') as csv_file: 
                csv_reader = csv.reader(csv_file, delimiter=',')
                header = True
                for line in csv_reader: 
                    if header:
                        header = False
                        continue
                    self.solution_moves.append((line[0], int(line[1])))

    def color_vehicles(self) -> None:
        """ 
        Assign colors to the vehicles. 
        """
        vehicles = self.get_vehicles()
        
        # Assign vehicles a color
        for vehicle in vehicles.values():
            if vehicle.id == "X":
                vehicle.color = "red"                
            else:
                vehicle.color = rd.choice(COLOR_NAMES)

    def draw_board(self) -> None:
        # Create "outside" of board 
        board = pygame.Rect(self.board_start_left, self.board_start_top, self.board_size, self.board_size)
        pygame.draw.rect(self.screen, "black", board, 3)
        
        # Create the vertical lines 
        for line_y in range(self.board_start_top + self.line_spacing, self.board_start_top + self.board_size, self.line_spacing):
            pygame.draw.line(self.screen, "black", (self.board_start_left, line_y), (self.board_start_left + self.board_size - 1, line_y), width=3)

        # Create the horizontal lines  
        for line_x in range(self.board_start_left + self.line_spacing, self.board_start_left + self.board_size, self.line_spacing):
            pygame.draw.line(self.screen, "black", (line_x, self.board_start_top), (line_x, self.board_start_top + self.board_size - 1), width=3)
    
    def draw_cars(self) -> None:
        # Give vehicles a position on the board 
        for vehicle in self.vehicles.values():
            tiles_occupied = vehicle.get_tiles_occupied()
            veh_x = self.board_start_left + (self.line_spacing * (tiles_occupied[0][0] - 1)) + self.car_margin
            veh_y = self.board_start_top + (self.line_spacing * (tiles_occupied[0][1] - 1)) + self.car_margin
            veh_width = self.line_spacing * (tiles_occupied[-1][0] - tiles_occupied[0][0] + 1) - 2 * self.car_margin
            veh_height = self.line_spacing * (tiles_occupied[-1][1] - tiles_occupied[0][1] + 1) - 2 * self.car_margin

            vehicle_rect = pygame.Rect(veh_x, veh_y, veh_width, veh_height)

            # Vehicle gets placed on the board 
            pygame.draw.rect(self.screen, vehicle.color, vehicle_rect)
        
    def draw_playbutton(self) -> pygame.Rect:
        button_x = self.board_size + self.board_start_left + 50
        button_y = self.board_start_top
        button_size = 100
        return pygame.draw.polygon(
            self.screen, 
            "black", 
            (
                (button_x, button_y), 
                (button_x, button_y + button_size), 
                (button_x+button_size, button_y + button_size//2)
            )
        )

    def start(self) -> None:
        """ 
        Start the game and give vehicles a position on the board. 
        """
        play_pressed = False
        running = True
        # Based on pygame quickstart example https://www.pygame.org/docs/
        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            mouse_position = pygame.mouse.get_pos()
            mouse_first_button_pressed = pygame.mouse.get_pressed()[0]

            # Fill the screen with a color to wipe away anything from last frame
            self.screen.fill("white")

            self.draw_board()
            self.draw_cars()
            
            if self.solution_moves:
                play_button = self.draw_playbutton()
                if mouse_first_button_pressed and play_button.collidepoint(mouse_position):
                    play_pressed = True
                
                if play_pressed:
                    game_move = self.solution_moves.pop(0)
                    self.process_turn(*game_move)



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
    board_file = "gameboards/Rushhour6x6_1.csv"
    results_file = "results/output_optimized.csv"
    newgame = PygameRushHour(6, board_file, results_file)
    newgame.start()
