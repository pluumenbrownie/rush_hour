from models import RushHour
import pygame


class PygameRushHour(RushHour):
    # Example file showing a circle moving on screen
    def __init__(self, width: int, board_file: str) -> None:
        super().__init__(width, board_file)


        # pygame setup
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)

    def start(self) -> None:
        running = True
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


            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player_pos.y -= 300 * self.dt
            if keys[pygame.K_s]:
                self.player_pos.y += 300 * self.dt
            if keys[pygame.K_a]:
                self.player_pos.x -= 300 * self.dt
            if keys[pygame.K_d]:
                self.player_pos.x += 300 * self.dt

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
    board_file = "gameboards/Rushhour6x6_2.csv"
    newgame = PygameRushHour(6, board_file)
    newgame.start()
