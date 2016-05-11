import unittest

from metier.MetierAdherent import MetierAdherent


class TestMetierAdherent(unittest.TestCase):
    def test_findAll(self):
        metierAdherent = MetierAdherent()
        self.assertTrue(len(metierAdherent.findAll()), False)


if __name__ == '__main__':
    unittest.main()
