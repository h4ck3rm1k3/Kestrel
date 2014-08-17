import unittest
from kestrel.config import load_config
from kestrel.config import load_xml_config
from kestrel.config import RedisConfig
from kestrel.config import WorkerConfig

class TestWorkerConfig(unittest.TestCase):
    def test_get_features(self):
        worker_config = WorkerConfig()
        expected = set([])
        self.assertEqual(expected, worker_config.get_features())
        assert False  # TODO: implement your test here

class TestRedisConfig(unittest.TestCase):
    def test_get_port(self):
        redis_config = RedisConfig()
        expected = 6379
        self.assertEqual(expected, redis_config.get_port())
        #assert False  # TODO: implement your test here

class TestLoadXmlConfig(unittest.TestCase):
    def test_load_xml_config(self):
        expected = None
        file_name = "tests/xmlconfig.xml"
        config = load_xml_config(file_name)
        self.assertIsNotNone(config)
        #assert False  # TODO: implement your test here

class TestLoadConfig(unittest.TestCase):
    def test_load_config(self):
        file_name= 'test.conf'
        config = load_config(file_name) 
        self.assertIsNotNone(config )
        #assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
