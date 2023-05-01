# Arkkitehtuurikuvaus

```mermaid
classDiagram
    index --> Ui
    index --> Game
    index --> Repository
    index: main()
    index: start_game()
    class Ui{
      screen
      start()
      draw_front_view()
      draw_game_view()
      draw_results_view()
    }
    class Game{
      pairs
      dict state
      point_card()
      open_card()
      check_win()
    }
    class Repository{
      file
      save_results()
      get_top_results()

    }
 ```
    
*Game* vastaa pelin tilannetietojen muokkaamisesta ja säilyttämisestä, *Ui* sovelluksen graafisen käyttöliittymän piirtämisestä ja *Repository* tietojen pysyvästä tallentamisesta, sekä *index.py* ohjaa sovelluksen toimintaa, seuraa käyttäjän toimintoja ja käyttää edellä mainittuja luokkia.