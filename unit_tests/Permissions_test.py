import unittest

from Project_functions.Permissions import *


class test_can_read(unittest.TestCase):
    def test_can_read(self):
        self.assertEqual(can_read())
