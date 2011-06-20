import unittest
import logging
import sleekxmpp
import kestrel.plugins.kestrel_executor
import pprint

class TestXmpp:
    def add_event_handler(a,b,c) :
        print("test")

class HelloworldTestCase(unittest.TestCase):

    def test_say(self):
        xmpp = TestXmpp()
        config ={}
        executor = kestrel.plugins.kestrel_executor.kestrel_executor(xmpp,config)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint (executor)
        executor.plugin_init()
        print "ok"

def suite():
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        suite.addTest(loader.loadTestsFromTestCase(HelloworldTestCase))
        return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
