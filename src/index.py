import pygame
from game import Game
import math

BACKGROUND_COLOR = (20, 20, 20)
CARD_COLOR = (100, 100, 100)
CARD_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255), (255, 0, 255), (255, 255, 0)]
FOUND_CARDS_LINE_COLOR = BACKGROUND_COLOR
OPEN_CARDS_LINE_COLOR = (100, 100, 100)
POINTED_CARD_LINE_COLOR = (255, 255, 255)

WIDTH = 400
HEIGHT = 400

PADDING = 70

def draw_game(screen, game):
    state = game.state

    w = (WIDTH-2*PADDING) / 4
    h = (HEIGHT-2*PADDING) / 3

    #PELINÄKYMÄ
    if state["win"] == False:
        # piirretään kortit ruudukkoon
        i = -1
        for y in range(3):
            for x in range(4):
                i += 1
                fillColor = CARD_COLOR
                lineColor = BACKGROUND_COLOR
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
                pygame.draw.rect(screen, BACKGROUND_COLOR, (X, Y, w, h), 5)

    #VOITTONÄKYMÄ
    elif state["win"] == True:
        text_box = pygame.Surface((WIDTH, HEIGHT))
        text_box.set_alpha(1)
        text_box.fill((0, 0, 0))
        screen.blit(text_box, (0, 0))

        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render("Voitit!", True, (255, 255, 255), (0, 0, 0))
        screen.blit(text, text.get_rect())



        print("Voitit! Lopulliset tiedot:", state)

    # näytön päivitys
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Muistipeli")
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()

    game = Game() 

    while True:

        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break

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

        # piirrä ja päivitä pelinäyttö
        draw_game(screen, game)

        # voittotarkistus/-päivitys
        game.check_win()

        ## tietoa terminaaliin
        ## print(game.state)
        
    pygame.quit()

main()