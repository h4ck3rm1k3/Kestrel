import unittest
from kestrel.plugins.kestrel_executor import kestrel_executor

class TestKestrelExecutor(unittest.TestCase):
    def test_plugin_init(self):
        executor = kestrel_executor()
        self.assertEqual(expected, executor.plugin_init())
        #assert False  # TODO: implement your test here

    def test_post_init(self):
        executor = kestrel_executor()
        self.assertEqual(expected, executor.post_init())
        assert False  # TODO: implement your test here

    def test_start(self):
        executor = kestrel_executor()
        self.assertEqual(expected, executor.start(event))
        #assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
