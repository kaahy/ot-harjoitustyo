import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    # Tehtävä 6:

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataa_rahaa_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_rahaa_ottaessa_saldo_vahenee_oikein_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_rahaa_ottaessa_saldo_ei_vahene_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahaa_ottaessa_paluuarvo_true_tai_false_kertoo_riittivatko_rahat(self):
        a = self.maksukortti.ota_rahaa(500)
        b = self.maksukortti.ota_rahaa(2000)
        self.assertEqual((a, b), (True, False))