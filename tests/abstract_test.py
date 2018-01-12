import unittest

from abstract import abstract

class AbstractTest(unittest.TestCase):

  def test_abstract(self):
    a = abstract.Abstract()
    a.test()
