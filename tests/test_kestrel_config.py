import unittest
from kestrel.config import load_config

class TestWorkerConfig(unittest.TestCase):
    def test_get_features(self):
        worker_config = WorkerConfig()
        self.assertEqual(expected, worker_config.get_features())
        assert False  # TODO: implement your test here

class TestRedisConfig(unittest.TestCase):
    def test_get_port(self):
        redis_config = RedisConfig()
        self.assertEqual(expected, redis_config.get_port())
        #assert False  # TODO: implement your test here

class TestLoadXmlConfig(unittest.TestCase):
    def test_load_xml_config(self):
        self.assertEqual(expected, load_xml_config(file_name))
        #assert False  # TODO: implement your test here

class TestLoadConfig(unittest.TestCase):
    def test_load_config(self):
        file_name= 'test.conf'
        expected={}
        self.assertEqual(expected, load_config(file_name))
        #assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
