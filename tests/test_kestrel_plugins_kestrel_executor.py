import unittest
from kestrel.plugins.kestrel_executor import kestrel_executor

class TestKestrelExecutor(unittest.TestCase):
    def setUp(self):
        config = {}
        self.executor = kestrel_executor(config)

    def test_plugin_init(self):
        expected = None
        self.assertEqual(expected, self.executor.plugin_init())
        #assert False  # TODO: implement your test here

    def test_post_init(self):
        expected = None
        self.assertEqual(expected, self.executor.post_init())
        
    def test_start(self):
        expected = None
        event = "test"
        self.assertEqual(expected, self.executor.start(event))


if __name__ == '__main__':
    unittest.main()
