import pygame
from pygame.colordict import THECOLORS
import random as rd

from models import RushHour


COLOR_NAMES = [name for name in THECOLORS.keys()]


class PygameRushHour(RushHour):
    def __init__(self, width: int, board_file: str) -> None:
        super().__init__(width, board_file)


        # pygame setup
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.dt = 0

<<<<<<< HEAD
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        
    
=======
>>>>>>> c0d2ff0103cb57da1549fa6ef76df5836d9ac3e0
        self.color_vehicles()

    
    def color_vehicles(self) -> None:
        vehicles = self.get_vehicles()
        for vehicle in vehicles.values():
            if vehicle.id == "X":
                vehicle.color = "red"
            else:
                vehicle.color = rd.choice(COLOR_NAMES)


    def start(self) -> None:
        running = True
        # Based on pygame quickstart example https://www.pygame.org/docs/
        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("white")
            resolution = self.screen.get_size()

            board_size = 600
            board_start_left = (resolution[0] - board_size)//2
            board_start_top = (resolution[1] - board_size)//2
            line_spacing = board_size // (self.game_board.width)

            board = pygame.Rect(board_start_left, board_start_top, board_size, board_size)
            pygame.draw.rect(self.screen, "black", board, 3)
            
            for line_y in range(board_start_top + line_spacing, board_start_top + board_size, line_spacing):
                pygame.draw.line(self.screen, "black", (board_start_left, line_y), (board_start_left + board_size - 1, line_y), width=3)
                
            for line_x in range(board_start_left + line_spacing, board_start_left + board_size, line_spacing):
                pygame.draw.line(self.screen, "black", (line_x, board_start_top), (line_x, board_start_top + board_size - 1), width=3)
            
            car_margin = 10
            vehicles = self.get_vehicles()
            for vehicle in vehicles.values():
                tiles_occupied = vehicle.get_tiles_occupied()
                veh_x = board_start_left + (line_spacing * (tiles_occupied[0][0] - 1)) + car_margin
                veh_y = board_start_top + (line_spacing * (tiles_occupied[0][1] - 1)) + car_margin
                veh_width = line_spacing * (tiles_occupied[-1][0] - tiles_occupied[0][0] + 1) - 2 * car_margin
                veh_height = line_spacing * (tiles_occupied[-1][1] - tiles_occupied[0][1] + 1) - 2 * car_margin

                vehicle_rect = pygame.Rect(veh_x, veh_y, veh_width, veh_height)
                pygame.draw.rect(self.screen, vehicle.color, vehicle_rect)


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

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            self.dt = self.clock.tick(60) / 1000
        pygame.quit()

    def __del__(self):
        pygame.quit()

if __name__ == '__main__':
    board_file = "gameboards/Rushhour12x12_7.csv"
    newgame = PygameRushHour(12, board_file)
    newgame.start()
