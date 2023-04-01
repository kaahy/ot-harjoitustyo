```mermaid
classDiagram
    Pelilauta "1" -- "1" Peli
    Ruutu "40" -- "1" Pelilauta
    Pelinappula "0..8" -- "1" Ruutu
    Pelaaja "1" -- "1" Pelinappula
    Noppa "2" -- "1" Peli
    Ruutu "1" -- "0" Ruutu
    Pelaaja "2..8" -- "1" Peli
```
