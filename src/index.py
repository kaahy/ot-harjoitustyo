import pygame
from game import Game
import math

BACKGROUND_COLOR_FRONT = (50, 50, 50)
BACKGROUND_COLOR_GAME = (5, 5, 5)
CARD_COLOR = (100, 100, 100)
CARD_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255), (255, 0, 255), (255, 255, 0)]
FOUND_CARDS_LINE_COLOR = BACKGROUND_COLOR_GAME
OPEN_CARDS_LINE_COLOR = (100, 100, 100)
POINTED_CARD_LINE_COLOR = (255, 255, 255)
WIDTH = 400
HEIGHT = 400
PADDING = 70

def start_game(screen):
    game = Game() 

    # game loop
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
                game.point_card(game.state["pointedCard"] - 4)
            if event.key == pygame.K_DOWN:
                game.point_card(game.state["pointedCard"] + 4)

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
        print("game loop", game.state)

def draw_front_page(screen):
    screen.fill((BACKGROUND_COLOR_FRONT))
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("[SPACE] Pelaa", True, (255, 255, 255))
    screen.blit(text, (40, 60))
    text = font.render("[ESC] Sulje", True, (255, 255, 255))
    screen.blit(text, (40, 100))
    pygame.display.flip()
    
def draw_game(screen, game):
    state = game.state

    w = (WIDTH-2*PADDING) / 4
    h = (HEIGHT-2*PADDING) / 3

    #PELINÄKYMÄ
    if state["win"] == False:
        screen.fill((0, 0, 0))

        # piirretään kortit ruudukkoon
        i = -1
        for y in range(3):
            for x in range(4):
                i += 1
                fillColor = CARD_COLOR
                lineColor = BACKGROUND_COLOR_GAME
                if i in state["foundCards"]:
                    fillColor = CARD_COLORS[state["cardContents"][i]]
                    lineColor = FOUND_CARDS_LINE_COLOR
                elif i in state["openCards"]:
                    fillColor = CARD_COLORS[state["cardContents"][i]]
                    lineCoLOR = OPEN_CARDS_LINE_COLOR
                if i == state["pointedCard"]:
                    lineColor = POINTED_CARD_LINE_COLOR

                X = PADDING + x*w
                Y = PADDING + y*h
                pygame.draw.rect(screen, fillColor, (X, Y, w, h), 0)
                pygame.draw.rect(screen, lineColor, (X, Y, w, h), 10)
                pygame.draw.rect(screen, BACKGROUND_COLOR_GAME, (X, Y, w, h), 5)

    #VOITTONÄKYMÄ
    elif state["win"] == True:
        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render("Löysit kaikki!", True, (255, 255, 255), (0, 0, 0))
        screen.blit(text, (20, 20))
        text = font.render("[ESC] Alkuun", True, (128, 128, 128), (0, 0, 0) )
        screen.blit(text, (20, HEIGHT-40))

    # näytön päivitys
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Muistipeli")

    while True:
        draw_front_page(screen)

        event = pygame.event.wait()
        
        if event.type == pygame.QUIT:
            break

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                start_game(screen)
            
            if event.key == pygame.K_ESCAPE:
                break

    pygame.quit()

main()