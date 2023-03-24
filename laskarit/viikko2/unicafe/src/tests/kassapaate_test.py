import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

# Tehtävä 8

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_luodun_kassapaatteen_rahamaara_ja_myytyjen_lounaiden_maara_oikein(self):
        rahamaara = self.kassa.kassassa_rahaa
        maukkaita = self.kassa.maukkaat
        edullisia= self.kassa.edulliset
        self.assertEqual((rahamaara, maukkaita, edullisia), (100000, 0, 0))


    def test_syo_edullisesti_kateisella_toimii_kun_maksu_riittää(self):
        maksu = 300
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(maksu)
        rahamaara = self.kassa.kassassa_rahaa
        maukkaita = self.kassa.maukkaat
        edullisia = self.kassa.edulliset
        self.assertEqual((rahamaara, vaihtoraha, edullisia, maukkaita), (100000+240, maksu-240, 1, 0))

    def test_syo_maukkaasti_kateisella_toimii_kun_maksu_riittää(self):
        maksu = 400
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(maksu)
        rahamaara = self.kassa.kassassa_rahaa
        maukkaita = self.kassa.maukkaat
        edullisia = self.kassa.edulliset
        self.assertEqual((rahamaara, vaihtoraha, edullisia, maukkaita), (100000+400, maksu-400, 0, 1))

    def test_syo_edullisesti_kateisella_toimii_oikein_kun_maksu_ei_riita(self):
        maksu = 235
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(maksu)
        rahamaara = self.kassa.kassassa_rahaa
        maukkaita = self.kassa.maukkaat
        edullisia = self.kassa.edulliset
        self.assertEqual((rahamaara, vaihtoraha, edullisia, maukkaita), (100000, maksu, 0, 0))

    def test_syo_maukkaasti_kateisella_toimii_oikein_kun_maksu_ei_riita(self):
        maksu =  395
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(maksu)
        rahamaara = self.kassa.kassassa_rahaa
        maukkaita = self.kassa.maukkaat
        edullisia = self.kassa.edulliset
        self.assertEqual((rahamaara, vaihtoraha, edullisia, maukkaita), (100000, maksu, 0, 0))


    def test_syo_edullisesti_kortilla_toimii_kun_kortilla_tarpeeksi_rahaa(self):
        truefalse = self.kassa.syo_edullisesti_kortilla(self.kortti)
        kortin_saldo = str(self.kortti)
        edullisia = self.kassa.edulliset
        maukkaita = self.kassa.maukkaat
        kassan_rahat = self.kassa.kassassa_rahaa

        self.assertEqual((truefalse, kortin_saldo, edullisia, maukkaita, kassan_rahat), (True, "Kortilla on rahaa {:0.2f} euroa".format((1000-240)/100), 1, 0, 100000))

    def test_syo_maukkaasti_kortilla_toimii_kun_kortilla_tarpeeksi_rahaa(self):
        truefalse = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        kortin_saldo = str(self.kortti)
        edullisia = self.kassa.edulliset
        maukkaita = self.kassa.maukkaat
        kassan_rahat = self.kassa.kassassa_rahaa

        self.assertEqual((truefalse, kortin_saldo, edullisia, maukkaita, kassan_rahat), (True, "Kortilla on rahaa {:0.2f} euroa".format((1000-400)/100), 0, 1, 100000))

    def test_syo_edullisesti_kortilla_toimii_oikein_kun_kortilla_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(200)

        truefalse = self.kassa.syo_edullisesti_kortilla(kortti)
        kortin_saldo = str(kortti)
        edullisia = self.kassa.edulliset
        maukkaita = self.kassa.maukkaat
        kassan_rahat = self.kassa.kassassa_rahaa

        self.assertEqual((truefalse, kortin_saldo, edullisia, maukkaita, kassan_rahat), (False, "Kortilla on rahaa {:0.2f} euroa".format(200/100), 0, 0, 100000))

    def test_syo_maukkaasti_kortilla_toimii_oikein_kun_kortilla_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(300)

        truefalse = self.kassa.syo_maukkaasti_kortilla(kortti)
        kortin_saldo = str(kortti)
        edullisia = self.kassa.edulliset
        maukkaita = self.kassa.maukkaat
        kassan_rahat = self.kassa.kassassa_rahaa

        self.assertEqual((truefalse, kortin_saldo, edullisia, maukkaita, kassan_rahat), (False, "Kortilla on rahaa {:0.2f} euroa".format(300/100), 0, 0, 100000))

    
    def test_lataa_rahaa_kortille_toimii_positiivisella_latauksella(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, 1000)

        self.assertEqual((self.kassa.kassassa_rahaa, str(kortti)), (100000+1000, "Kortilla on rahaa {:0.2f} euroa".format(1000/100)))


    # Tehtävä 9:

    def test_lataa_rahaa_kortille_toimii_oikein_negatiivisella_latauksella(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, -1000)
        
        self.assertEqual((self.kassa.kassassa_rahaa, str(kortti)), (100000, "Kortilla on rahaa {:0.2f} euroa".format(0)))