import unittest
from kestrel.manager import Manager

class TestManager(unittest.TestCase):
    def test___init__(self):

        config = {
            "TOX" :{
                "identity_file" : "idfile" 
            }
        }
        manager = Manager(config)
        #assert False  # TODO: implement your test here

    def test_start(self):

        config = {
            "TOX" :{
                "identity_file" : "idfile" 
            }
        }
        manager = Manager( config)
        expected = None
        event = "start"
        self.assertEqual(expected, manager.start(event))
        #assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
