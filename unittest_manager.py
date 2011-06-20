import unittest

class HelloworldTestCase(unittest.TestCase):

    def test_say(self):
        print "ok"

def suite():
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        suite.addTest(loader.loadTestsFromTestCase(HelloworldTestCase))
        return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
