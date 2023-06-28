import pygame
from visualisation.customcolors import COLORS
import random as rd
import csv

from classes.models import RushHour


COLOR_NAMES = [name for name in COLORS.keys()]


class PygameRushHour(RushHour):
    """
    An interactive verstion of the `RushHour` class. Run the `.start()` method to
    show a pygame render of the game board.
    
    Inputs:
    - `width: int` - The size of the board.
    - `board_file: str` - The file location of the board layout.
    - `solution_file: str | None = None` - When given a file with vehicle moves for
    the current board, pygame can animate the moves made in the file.
    """
    def __init__(
        self, width: int, board_file: str, solution_file: str | None = None
    ) -> None:
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
        self.board_start_left = (self.resolution[0] - self.board_size) // 2
        self.board_start_top = (self.resolution[1] - self.board_size) // 2

        # Distance between the boxes
        self.line_spacing = self.board_size // (self.game_board.width)

        self.solution_moves: list[tuple[str, int]] = []
        if solution_file:
            with open(solution_file, "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                header = True
                for line in csv_reader:
                    if header:
                        header = False
                        continue
                    self.solution_moves.append((line[0], int(line[1])))
            self.total_moves = len(self.solution_moves)
        self.cars_per_frame = 1.0

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
        """
        Draw the grid of the Rush Hour board.
        """
        # Create "outside" of board
        board = pygame.Rect(
            self.board_start_left,
            self.board_start_top,
            self.board_size,
            self.board_size,
        )
        pygame.draw.rect(self.screen, "black", board, 3)

        # Create the vertical lines
        for line_y in range(
            self.board_start_top + self.line_spacing,
            self.board_start_top + self.board_size,
            self.line_spacing,
        ):
            pygame.draw.line(
                self.screen,
                "black",
                (self.board_start_left, line_y),
                (self.board_start_left + self.board_size - 1, line_y),
                width=3,
            )

        # Create the horizontal lines
        for line_x in range(
            self.board_start_left + self.line_spacing,
            self.board_start_left + self.board_size,
            self.line_spacing,
        ):
            pygame.draw.line(
                self.screen,
                "black",
                (line_x, self.board_start_top),
                (line_x, self.board_start_top + self.board_size - 1),
                width=3,
            )

    def draw_cars(self) -> None:
        """
        Draw the cars on the board.
        """
        # Give vehicles a position on the board
        for vehicle in self.vehicles.values():
            tiles_occupied = vehicle.get_tiles_occupied()
            veh_x = (
                self.board_start_left
                + (self.line_spacing * (tiles_occupied[0][0] - 1))
                + self.car_margin
            )
            veh_y = (
                self.board_start_top
                + (self.line_spacing * (tiles_occupied[0][1] - 1))
                + self.car_margin
            )
            veh_width = (
                self.line_spacing * (tiles_occupied[-1][0] - tiles_occupied[0][0] + 1)
                - 2 * self.car_margin
            )
            veh_height = (
                self.line_spacing * (tiles_occupied[-1][1] - tiles_occupied[0][1] + 1)
                - 2 * self.car_margin
            )

            vehicle_rect = pygame.Rect(veh_x, veh_y, veh_width, veh_height)

            # Vehicle gets placed on the board
            pygame.draw.rect(self.screen, vehicle.color, vehicle_rect)

    def draw_playbutton(self) -> pygame.Rect:
        """
        Draws a play button next to the game board. Returns an object corresponding
        to the button for use in detecting mouse clicks.
        """
        button_x = self.board_size + self.board_start_left + 50
        button_y = self.board_start_top
        button_size = 100
        return pygame.draw.polygon(
            self.screen,
            "black",
            (
                (button_x, button_y),
                (button_x, button_y + button_size),
                (button_x + button_size, button_y + button_size // 2),
            ),
        )

    def draw_speed_setting(self, turn_nr: int) -> tuple[pygame.Rect, pygame.Rect]:
        """
        Draws a speed indicator for the amount of moves made per second; an indicator
        for how many moves have been made and how much are left; and buttons to change
        the speed. Returns objects corresponding to the minus and plus buttons,
        respectively.
        """
        display_x = self.board_size + self.board_start_left + 50
        display_y = self.board_size + self.board_start_top - 100
        font_path = pygame.font.match_font(pygame.font.get_default_font())
        text_font = pygame.font.Font(font_path, 100)
        small_text_font = pygame.font.Font(font_path, 30)

        if self.cars_per_frame > 1:
            cps_text = round(60*self.cars_per_frame)
        else:
            cps_text = round(60*self.cars_per_frame, 1)


        plus_text_surface = text_font.render("+", True, "black", "white")
        minus_text_surface = text_font.render("-", True, "black", "white")
        speed_text_surface = text_font.render(
            f"{cps_text}", True, "black", "white"
        )
        description_text_surface = small_text_font.render(
            "Moves per second:", True, "black", "white"
        )
        counter_text_surface = small_text_font.render(
            f"{turn_nr}/{self.total_moves}", True, "black", "white"
        )

        minus = self.screen.blit(minus_text_surface, (display_x - 30, display_y))
        plus = self.screen.blit(plus_text_surface, (display_x + 160, display_y))
        self.screen.blit(speed_text_surface, (display_x, display_y))
        self.screen.blit(description_text_surface, (display_x - 30, display_y - 25))
        self.screen.blit(counter_text_surface, (display_x - 30, display_y + 75))

        return minus, plus

    def start(self) -> None:
        """
        Start the game and give vehicles a position on the board.
        """
        play_pressed = False
        detect_hold = False
        running = True
        turn_nr = 0
        playback_frame_counter = 0
        # Based on pygame quickstart example https://www.pygame.org/docs/
        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            mouse_position = pygame.mouse.get_pos()
            mouse_first_button_pressed = (
                pygame.mouse.get_pressed()[0] if not detect_hold else False
            )
            detect_hold = pygame.mouse.get_pressed()[0]

            # Fill the screen with a color to wipe away anything from last frame
            self.screen.fill("white")

            self.draw_board()
            self.draw_cars()

            if self.solution_moves:
                play_button = self.draw_playbutton()
                minus_button, plus_button = self.draw_speed_setting(turn_nr)
                # clicked on play
                if (
                    mouse_first_button_pressed
                    and play_button.collidepoint(mouse_position)
                ):
                    play_pressed = True
                # clicked on --
                if (
                    mouse_first_button_pressed
                    and minus_button.collidepoint(mouse_position)
                ):
                    self.cars_per_frame /= 2 if self.cars_per_frame > 0.01 else 1
                # clicked on +
                if (
                    mouse_first_button_pressed
                    and  plus_button.collidepoint(mouse_position)
                ):
                    self.cars_per_frame *= 2 if self.cars_per_frame < 100 else 1

                if play_pressed:
                    turn_nr, playback_frame_counter = self.play_frame(turn_nr, playback_frame_counter)

            # Pop up the display to put your work on screen (or overwrites the screen)
            pygame.display.flip()

            # Limits frames per second (FPS) to 60
            # dt is delta time in seconds since last frame, used for framerate independent physics
            self.dt = self.clock.tick(60) / 1000
        pygame.quit()

    def play_frame(self, turn_nr: int, playback_frame_counter: int) -> tuple[int, int]:
        # Move vehicles every frame
        if self.cars_per_frame >= 1:
            try:
                for _ in range(round(self.cars_per_frame)):
                    game_move = self.solution_moves.pop(0)
                    self.process_turn(*game_move)
                    turn_nr += 1
            except IndexError:
                # program tries to pop more items than are in the list at the end of the solution
                pass
        # Wait one frame or more between each move
        elif playback_frame_counter % (1/self.cars_per_frame) == 0:
            game_move = self.solution_moves.pop(0)
            self.process_turn(*game_move)
            turn_nr += 1

        return turn_nr, playback_frame_counter + 1

    def __del__(self):
        """
        End of the game.
        """
        pygame.quit()


if __name__ == "__main__":
    board_file = "gameboards/Rushhour9x9_6.csv"
    results_file = "results/random_optimized_moves_6x6_1.csv"
    newgame = PygameRushHour(9, board_file, results_file)
    newgame.start()
