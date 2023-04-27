import math
from random import shuffle
import pygame

WIDTH = 600
HEIGHT = 600
PADDING = 100
BACKGROUND_COLOR_FRONT = (10, 10, 10)
BACKGROUND_COLOR_GAME = (10, 10, 10)
TEXT_COLOR_BRIGHT = (255, 255, 255)
TEXT_COLOR_DIM = (128, 128, 128)
CARD_COLOR = (100, 100, 100)
POINTED_CARD_LINE_COLOR = (255, 255, 255)
FOUND_CARDS_LINE_COLOR  = BACKGROUND_COLOR_GAME
OPEN_CARDS_LINE_COLOR = (0, 0, 0)
CARD_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255), (255, 0, 255), (255, 255, 0)]
CARD_COLORS += [(128, 0, 0), (0, 128, 0), (0, 0, 128), (0, 128, 128), (128, 0, 128), (128, 128, 0)]
CARD_COLORS += [(255, 128, 0), (128, 64, 0), (255, 255, 255)]
shuffle(CARD_COLORS)

class Ui:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def start(self):
        pygame.init()
        pygame.display.set_caption("Muistipeli")

    def draw_results_view(self, results, pairs):
        self.screen.fill((0, 64, 0))

        font = pygame.font.Font("freesansbold.ttf", 20)

        y = 40
        text = font.render(f"Parhaat tulokset - {pairs} paria", True, TEXT_COLOR_BRIGHT)
        self.screen.blit(text, (20, y))
        y += 60

        if len(results) == 0:
            text = font.render(f"Ei tuloksia", True, TEXT_COLOR_BRIGHT)
            self.screen.blit(text, (20, y))
        else:
            for result in results:
                text = font.render(f"{result[0]} kääntöä ({round(result[1], 2)} s)", True, TEXT_COLOR_BRIGHT)
                self.screen.blit(text, (20, y))
                y += 40

        text = font.render(f"[ESC] Alkuun", True, TEXT_COLOR_DIM)
        self.screen.blit(text, (20, HEIGHT-40))

        pygame.display.flip()

    def draw_front_view(self):
        self.screen.fill((BACKGROUND_COLOR_FRONT))
        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render("Pelaa", True, TEXT_COLOR_DIM)
        self.screen.blit(text, (40, 60))
        text = font.render("[1] Helppo", True, TEXT_COLOR_BRIGHT)
        self.screen.blit(text, (60, 100))
        text = font.render("[2] Keskitaso", True, TEXT_COLOR_BRIGHT)
        self.screen.blit(text, (60, 140))
        text = font.render("[3] Vaikea", True, TEXT_COLOR_BRIGHT)
        self.screen.blit(text, (60, 180))

        text = font.render("Parhaat tulokset", True, TEXT_COLOR_DIM)
        self.screen.blit(text, (40, 240))
        text = font.render("[4] Helppo", True, TEXT_COLOR_BRIGHT)
        self.screen.blit(text, (60, 280))
        text = font.render("[5] Keskitaso", True, TEXT_COLOR_BRIGHT)
        self.screen.blit(text, (60, 320))
        text = font.render("[6] Vaikea", True, TEXT_COLOR_BRIGHT)
        self.screen.blit(text, (60, 360))

        text = font.render("[ESC] Sulje", True, TEXT_COLOR_DIM)
        self.screen.blit(text, (40, 420))
        pygame.display.flip()

    def draw_game_view(self, game):
        grid_w = self.grid_size(game.pairs)["width"]
        grid_h = self.grid_size(game.pairs)["height"]
        card_w = (WIDTH-2*PADDING) / grid_w
        card_h = (HEIGHT-2*PADDING) / grid_h

        #PELINÄKYMÄ
        if not game.state["win"]:
            self.screen.fill(BACKGROUND_COLOR_GAME)
            #tekstit
            font = pygame.font.Font("freesansbold.ttf", 20)
            text = font.render(f"Käännöt: {game.state['turns']}", True, (TEXT_COLOR_BRIGHT), BACKGROUND_COLOR_GAME)
            self.screen.blit(text, (20, 20))
            # piirretään kortit ruudukkoon
            card_id = -1
            for i in range(grid_h):
                for j in range(grid_w):
                    card_id += 1
                    if card_id >= game.pairs*2:
                        break
                    fill_color = CARD_COLOR
                    line_color = BACKGROUND_COLOR_GAME
                    if card_id in game.state["foundCards"]:
                        fill_color = CARD_COLORS[game.state["cardContents"][card_id]]
                        line_color = FOUND_CARDS_LINE_COLOR
                    if card_id == game.state["pointedCard"]:
                        line_color = POINTED_CARD_LINE_COLOR
                    if card_id in game.state["openCards"]:
                        fill_color = CARD_COLORS[game.state["cardContents"][card_id]]
                        line_color = CARD_COLORS[game.state["cardContents"][card_id]]
                    rect = (PADDING+j*card_w, PADDING+i*card_h, card_w, card_h)
                    pygame.draw.rect(self.screen, fill_color, rect, 0)
                    pygame.draw.rect(self.screen, line_color, rect, int(0.1*card_w))
                    pygame.draw.rect(self.screen, BACKGROUND_COLOR_GAME, rect, int(0.05*card_w))

        #VOITTONÄKYMÄ
        elif game.state["win"]:
            font = pygame.font.Font("freesansbold.ttf", 20)
            text = font.render("Löysit kaikki!", True, (TEXT_COLOR_BRIGHT), BACKGROUND_COLOR_GAME)
            self.screen.blit(text, (20, 20))
            text = font.render(f"Käännöt: {game.state['turns']}", True, (TEXT_COLOR_BRIGHT), BACKGROUND_COLOR_GAME)
            self.screen.blit(text, (20, 50))
            text = font.render(f"Aika: {round(game.state['duration'], 1)} s", True, (TEXT_COLOR_BRIGHT), BACKGROUND_COLOR_GAME)
            self.screen.blit(text, (20, 80))
            text = font.render("[ESC] Alkuun", True, (TEXT_COLOR_DIM), BACKGROUND_COLOR_GAME)
            self.screen.blit(text, (20, HEIGHT-40))

        # näytön päivitys
        pygame.display.flip()

    def grid_size(self, pairs):
        grid_w = math.ceil(math.sqrt(pairs*2))
        grid_h = math.ceil((pairs*2) / grid_w)
        return {"width": grid_w, "height": grid_h}
