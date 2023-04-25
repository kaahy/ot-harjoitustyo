# Muistipeli

Muistipelissä tavoitteena on löytää parit nurin käännetyistä korteista katsomalla aina kahta korttia kerrallaan.

Ohjelmistotekniikka-kurssin harjoitustyö.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/kaahy/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuuri](https://github.com/kaahy/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
- [Tyoaikakirjanpito](https://github.com/kaahy/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/kaahy/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet: `poetry install`
2. Käynnistä sovellus: `poetry run invoke start`

## Komentorivitoiminnot

Ohjelman suoritus:
```
poetry run invoke start
```

Testien suoritus:
```
poetry run invoke test
```

Testikattavuusraportin generointi (htmlcov-hakemistoon):
```
poetry run invoke coverage-report
```

Pylint-tarkistusten (määritelty tiedostossa .pylintrc) suoritus:
```
poetry run invoke lint
```