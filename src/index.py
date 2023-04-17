import pygame
from game import Game
import math
from random import shuffle

BACKGROUND_COLOR_FRONT = (10, 10, 10)
BACKGROUND_COLOR_GAME = (10, 10, 10)
CARD_COLOR = (100, 100, 100)
CARD_COLORS = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (108, 0, 255),  (255, 0, 255), (255, 0, 128), (128, 0, 0), (128, 128, 0), (0, 128, 0), (0, 128, 128), (0, 0, 128), (128, 0, 128)]
shuffle(CARD_COLORS)
FOUND_CARDS_LINE_COLOR  = BACKGROUND_COLOR_GAME
OPEN_CARDS_LINE_COLOR = (0, 0, 0)
POINTED_CARD_LINE_COLOR = (255, 255, 255)
WIDTH = 600
HEIGHT = 600
PADDING = 100
TEXT_COLOR_BRIGHT = (255, 255, 255)
TEXT_COLOR_DIM = (128, 128, 128)

def grid_size(pairs):
    grid_w = math.ceil(math.sqrt(pairs*2))
    grid_h = math.ceil((pairs*2) / grid_w)
    return {"width": grid_w, "height": grid_h}

def start_game(screen, pairs):
    game = Game(pairs)

    # pelisilmukka
    while True:
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            exit()
    
        if event.type == pygame.KEYDOWN:
            
            # kortin osoitus
            if event.key == pygame.K_LEFT:
                game.point_card(game.state["pointedCard"] - 1)
            if event.key == pygame.K_RIGHT:
                game.point_card(game.state["pointedCard"] + 1)
            if event.key == pygame.K_UP:
                game.point_card(game.state["pointedCard"] - grid_size(pairs)["width"])
            if event.key == pygame.K_DOWN:
                game.point_card(game.state["pointedCard"] + grid_size(pairs)["width"])

            # (osoituksessa olevan) kortin avaus
            if event.key == pygame.K_SPACE:
                game.open_card()

            # (osoituksessa olevan) kortin avaus
            if event.key == pygame.K_ESCAPE:
                return False

        # piirrä ja päivitä pelinäyttö
        draw_game(screen, game)

        # voittotarkistus/-päivitys
        game.check_win()

        ## tietoa terminaaliin
        ## print("game loop", game.state)

def draw_front_page(screen):
    screen.fill((BACKGROUND_COLOR_FRONT))
    font = pygame.font.Font("freesansbold.ttf", 20)

    text = font.render("Pelaa", True, TEXT_COLOR_DIM)
    screen.blit(text, (40, 60))

    text = font.render("[1] Helppo", True, TEXT_COLOR_BRIGHT)
    screen.blit(text, (60, 100))

    text = font.render("[2] Keskitaso", True, TEXT_COLOR_BRIGHT)
    screen.blit(text, (60, 140))

    text = font.render("[3] Vaikea", True, TEXT_COLOR_BRIGHT)
    screen.blit(text, (60, 180))

    text = font.render("[ESC] Sulje", True, TEXT_COLOR_DIM)
    screen.blit(text, (40, 240))

    pygame.display.flip()
    
def draw_game(screen, game):
    state = game.state

    grid_w = grid_size(game.pairs)["width"]
    grid_h = grid_size(game.pairs)["height"]

    card_w = (WIDTH-2*PADDING) / grid_w
    card_h = (HEIGHT-2*PADDING) / grid_h

    #PELINÄKYMÄ
    if state["win"] == False:
        screen.fill(BACKGROUND_COLOR_GAME)

        # piirretään kortit ruudukkoon
        i = -1
        for y in range(grid_h):
            for x in range(grid_w):
                i += 1

                if i < game.pairs*2:
                    fillColor = CARD_COLOR
                    lineColor = BACKGROUND_COLOR_GAME
                    if i in state["foundCards"]:
                        fillColor = CARD_COLORS[state["cardContents"][i]]
                        lineColor = FOUND_CARDS_LINE_COLOR
                    if i == state["pointedCard"]:
                        lineColor = POINTED_CARD_LINE_COLOR
                    if i in state["openCards"]:
                        fillColor = CARD_COLORS[state["cardContents"][i]]
                        lineColor = CARD_COLORS[state["cardContents"][i]]

                    X = PADDING + x*card_w
                    Y = PADDING + y*card_h

                    pygame.draw.rect(screen, fillColor, (X, Y, card_w, card_h), 0)
                    pygame.draw.rect(screen, lineColor, (X, Y, card_w, card_h), int(0.1*card_w))
                    pygame.draw.rect(screen, BACKGROUND_COLOR_GAME, (X, Y, card_w, card_h), int(0.05*card_w))

    #VOITTONÄKYMÄ
    elif state["win"] == True:
        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render("Löysit kaikki!", True, (TEXT_COLOR_BRIGHT), BACKGROUND_COLOR_GAME)
        screen.blit(text, (20, 20))
        text = font.render("[ESC] Alkuun", True, (TEXT_COLOR_DIM), BACKGROUND_COLOR_GAME)
        screen.blit(text, (20, HEIGHT-40))

    # näytön päivitys
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Muistipeli")

    # pääsilmukka
    while True:
        draw_front_page(screen)

        event = pygame.event.wait()
        
        if event.type == pygame.QUIT:
            break

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                start_game(screen, 6)

            if event.key == pygame.K_2:
                start_game(screen, 10)

            if event.key == pygame.K_3:
                start_game(screen, 15)
            
            if event.key == pygame.K_ESCAPE:
                break

    pygame.quit()

main()