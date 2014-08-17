import unittest
from kestrel.plugins.kestrel_client import kestrel_client


class TestKestrelClient(unittest.TestCase):

    def setUp(self):
        config = {
            "TOX" :{
                "identity_file" : "idfile" 
            }
        }
        self.client = kestrel_client(config)

    def test_cancel_job(self):
#        xmpp= None 
#        config = None
        expected = None
        job_id= "somejob"
        self.assertEqual(expected, self.client.cancel_job(job_id))
        #assert False  # TODO: implement your test here

    def test_cancel_jobs(self):
        job_ids= ["somejob","somejob2"]
        expected = None
        self.assertEqual(expected, self.client.cancel_jobs(job_ids))
        #assert False  # TODO: implement your test here

    def test_job_status(self):
        expected = None
        job_id= "somejob"
        self.assertEqual(expected, self.client.job_status(job_id))
        assert False  # TODO: implement your test here

    def test_plugin_init(self):
        expected = None
        self.assertEqual(expected, self.client.plugin_init())
        #assert False  # TODO: implement your test here

    def test_pool_status(self):
        expected = None
        self.assertEqual(expected, self.client.pool_status())
        #assert False  # TODO: implement your test here

    def test_submit_job(self):
        expected = None
        job= "somejob"
        self.assertEqual(expected, self.client.submit_job(job))
        #assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
