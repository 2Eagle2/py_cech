import unittest as ut
import unittest.mock as moc
from scripts import pycech
import itertools


class PyCechTester(ut.TestCase):

    def test_pycech(self):

        str_values = [None, " ", 0]

        pycech.pycech(True, False, None, None, None)
        pycech.pycech(False, True, None, None, None)
        pycech.pycech(False, False, " ", None, None)
        pycech.pycech(False, False, "Meno", 0, None)
        pycech.pycech(False, False, "Meno", None, 0)

        with self.assertRaises(RuntimeError):
            pycech.pycech(False, False, "Meno", 0, 0)
        with self.assertRaises(RuntimeError):
            pycech.pycech(True, True, None, None, None)
        with self.assertRaises(RuntimeError):
            pycech.pycech(True, False, " ", None, None)
        with self.assertRaises(RuntimeError):
            pycech.pycech(True, False, " ", 0, None)
        with self.assertRaises(RuntimeError):
            pycech.pycech(True, False, " ", 0, 0)
        with self.assertRaises(RuntimeError):
            pycech.pycech(True, False, None, 0, 0)
        with self.assertRaises(RuntimeError):
            pycech.pycech(True, False, None, 0, None)
        with self.assertRaises(RuntimeError):
            pycech.pycech(True, False, None, None, 0)


if __name__ == "__main__":
    ut.main()