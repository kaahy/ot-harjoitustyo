import sys
from time import time
import pygame
from game import Game
from ui import Ui

def save_results(time, pairs, turns, duration):
    f = open("results.txt", "a")
    f.write(f"\n{time} {pairs} {turns} {duration} {time}")
    f.close()

def print_results(pairs, ui_view):
    tulokset = []

    with open("results.txt") as f:
        lines = f.read().splitlines()

    for line_ in lines:
        line = line_.split()
        if len(line) < 2:
            continue

        if int(line[1]) == pairs:
            turns = int(line[2])
            duration = float(line[3])
            tulokset.append((turns, duration))

    tulokset.sort()

    while True:
        event = pygame.event.wait()

        ui_view.draw_results_view(tulokset[0:5])

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return
            
    return

def start_game(pairs, ui_view):
    game = Game(pairs)

    # pelisilmukka
    while True:
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            # kortin osoitus
            if event.key == pygame.K_LEFT:
                game.point_card(game.state["pointedCard"] - 1)
            if event.key == pygame.K_RIGHT:
                game.point_card(game.state["pointedCard"] + 1)
            if event.key == pygame.K_UP:
                game.point_card(game.state["pointedCard"] - ui_view.grid_size(pairs)["width"])
            if event.key == pygame.K_DOWN:
                game.point_card(game.state["pointedCard"] + ui_view.grid_size(pairs)["width"])

            # (osoituksessa olevan) kortin avaus
            if event.key == pygame.K_SPACE:
                game.open_card()

            if event.key == pygame.K_ESCAPE:
                #### tallenna tulokset
                if game.state["win"]:
                    save_results(time(), game.pairs, game.state["turns"], game.state["duration"])

                return False

        # piirrä ja päivitä pelinäyttö
        ui_view.draw_game_view(game)

        # voittotarkistus/-päivitys
        game.check_win()

        ## tietoa terminaaliin
        ## print("game loop", game.state)

def main():
    ui_view = Ui()
    ui_view.start()

    # pääsilmukka
    while True:
        ui_view.draw_front_view()

        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            break

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                start_game(6, ui_view)

            if event.key == pygame.K_2:
                start_game(10, ui_view)

            if event.key == pygame.K_3:
                start_game(15, ui_view)

            if event.key == pygame.K_4:
                print_results(6, ui_view)

            if event.key == pygame.K_5:
                print_results(10, ui_view)

            if event.key == pygame.K_6:
                print_results(15, ui_view)

            if event.key == pygame.K_ESCAPE:
                break

    pygame.quit()

main()
