import unittest
from kestrel.backend import Kestrel
import redis

class TestKestrel(unittest.TestCase):
    def setUp(self):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
        
    def test___init__(self):
        kestrel = Kestrel(self.redis)
        assert kestrel  # TODO: implement your test here

    def test_available_workers(self):
        kestrel = Kestrel(self.redis)
        expected = set([])
        self.assertEqual(expected, kestrel.available_workers())
#        assert False  # TODO: implement your test here

    def test_busy_workers(self):
        kestrel = Kestrel(self.redis)
        expected = set([])
        self.assertEqual(expected, kestrel.busy_workers())
#        assert False  # TODO: implement your test here

    def test_cancel_job(self):
        kestrel = Kestrel(self.redis)
        expected = None
        job = None
        canceller = None
        self.assertEqual(expected, kestrel.cancel_job(job, canceller))
#        assert False  # TODO: implement your test here

    def test_clean(self):
        kestrel = Kestrel(self.redis)
        expected = None
        self.assertEqual(expected, kestrel.clean())
#        assert False  # TODO: implement your test here

    def test_get_job(self):
        kestrel = Kestrel(self.redis)
        expected = {'requirements': set([]), 'cleanup': 'None', 'command': 'None', 'owner': 'None', 'id': None, 'size': '1'}
        job = None
        self.assertEqual(expected, kestrel.get_job(job))
#        assert False  # TODO: implement your test here

    def test_get_jobs(self):
        kestrel = Kestrel(self.redis)
        expected = {'None': 'None'}
        self.assertEqual(expected, kestrel.get_jobs())
#        assert False  # TODO: implement your test here

    def test_job_id(self):
        kestrel = Kestrel(self.redis)
        expected = '15'
        self.assertLess(expected, kestrel.job_id())
#        assert False  # TODO: implement your test here

    def test_job_matches(self):
        kestrel = Kestrel(self.redis)
        expected = {}
        job = None
        self.assertEqual(expected, kestrel.job_matches(job))
#        assert False  # TODO: implement your test here

    def test_job_status(self):
        kestrel = Kestrel(self.redis)
        expected =  {'None': {'requested': '1', 'completed': 0, 'running': 0, 'owner': 'None', 'queued': 1, 'pending': 0}}
        job = None
        self.assertEqual(expected, kestrel.job_status(job))
#        assert False  # TODO: implement your test here

    def test_known_worker(self):
        kestrel = Kestrel(self.redis)
        expected = False
        name = "funk"
        self.assertEqual(expected, kestrel.known_worker(name))
#        assert False  # TODO: implement your test here

    def test_online_workers(self):
        kestrel = Kestrel(self.redis)
        expected = set(['test'])
        self.assertEqual(expected, kestrel.online_workers())
#        assert False  # TODO: implement your test here

    def test_pool_status(self):
        kestrel = Kestrel(self.redis)
        expected = {'available': 0, 'busy': 0, 'online': 1}

        self.assertEqual(expected, kestrel.pool_status())
#        assert False  # TODO: implement your test here

    def test_register_worker(self):
        kestrel = Kestrel(self.redis)
        expected = None
        name = 'test'
        capabilities=[]
        self.assertEqual(expected, kestrel.register_worker(name, capabilities))
#        assert False  # TODO: implement your test here

    def test_reset_pending_tasks(self):
        kestrel = Kestrel(self.redis)
        expected = set([])
        self.assertEqual(expected, kestrel.reset_pending_tasks())
#        assert False  # TODO: implement your test here

    def test_reset_stalled_tasks(self):
        kestrel = Kestrel(self.redis)
        expected= set([])
        self.assertEqual(expected, kestrel.reset_stalled_tasks())
#        assert False  # TODO: implement your test here

    def test_submit_job(self):
        kestrel = Kestrel(self.redis)
        expected=(None, {})
        job=None
        owner=None
        command=None
        size=1
        requirements=[]
        cleanup=None
        self.assertEqual(expected, kestrel.submit_job(job, owner, command, cleanup, size, requirements))
#        assert False  # TODO: implement your test here

    def test_task_finish(self):
        kestrel = Kestrel(self.redis)
        expected=False
        worker=None
        job=None
        task=None
        self.assertEqual(expected, kestrel.task_finish(worker, job, task))
#        assert False  # TODO: implement your test here

    def test_task_reset(self):
        kestrel = Kestrel(self.redis)
        expected=None
        worker=None
        job=None
        task=None
        self.assertEqual(expected, kestrel.task_reset(worker, job, task))
#        assert False  # TODO: implement your test here

    def test_task_start(self):
        kestrel = Kestrel(self.redis)
        expected=None
        worker=None
        job=None
        task=None
        self.assertEqual(expected, kestrel.task_start(worker, job, task))
#        assert False  # TODO: implement your test here

    def test_user_jobs(self):
        kestrel = Kestrel(self.redis)
        expected= set([])
        user=None
        self.assertEqual(expected, kestrel.user_jobs(user))
#        assert False  # TODO: implement your test here

    def test_worker_available(self):
        kestrel = Kestrel(self.redis)
        expected=None
        name=None
        self.assertEqual(expected, kestrel.worker_available(name))
#        assert False  # TODO: implement your test here

    def test_worker_busy(self):
        kestrel = Kestrel(self.redis)
        expected=None
        name=None
        self.assertEqual(expected, kestrel.worker_busy(name))
#        assert False  # TODO: implement your test here

    def test_worker_capabilities(self):
        kestrel = Kestrel(self.redis)
        expected=set([])
        name=None
        self.assertEqual(expected, kestrel.worker_capabilities(name))
#        assert False  # TODO: implement your test here

    def test_worker_offline(self):
        kestrel = Kestrel(self.redis)
        expected=None
        name=None
        self.assertEqual(expected, kestrel.worker_offline(name))
#        assert False  # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
