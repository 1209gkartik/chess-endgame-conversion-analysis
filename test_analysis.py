import unittest
from analysis import *
class Tests(unittest.TestCase):
    def test_model(self):
        self.assertEqual(list(simulate(10)),list(simulate(10)))
        self.assertEqual(summarize([dict(rating=1500,clock=10,advantage=2,win=1),dict(rating=1500,clock=20,advantage=2,win=0)])[0][-1],.5)
if __name__=='__main__': unittest.main()
