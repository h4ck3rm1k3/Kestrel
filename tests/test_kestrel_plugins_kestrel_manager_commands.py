import unittest
from kestrel.plugins.kestrel_manager.commands import (
    AdhocCommand, 
    cmd_canceljob)

session = {
    'from' : "bla"
}
expected = None
payload = None
form = "blah"
config = {
    "backend" : "blag"
}

class TestAdhocCommand(unittest.TestCase):
    def setUp(self):
        self.adhoc_command = AdhocCommand(config)

    def test_command_init(self):

        self.assertEqual(expected, self.adhoc_command.command_init())

    def test_plugin_init(self):
        self.assertEqual(expected, self.adhoc_command.plugin_init())

    def test_post_init(self):
        self.assertEqual(expected, self.adhoc_command.post_init())

    def test_session_start(self):
        self.assertEqual(expected, self.adhoc_command.session_start(payload, session))


    def test_start(self):

        self.assertEqual(expected, self.adhoc_command.start(payload, session))


class TestCmdPoolstatus(unittest.TestCase):
    def test_command_init(self):
        cmd_poolstatus = cmd_poolstatus()
        self.assertEqual(expected, cmd_poolstatus.command_init())


    def test_start(self):
        cmd_poolstatus = cmd_poolstatus()
        self.assertEqual(expected, cmd_poolstatus.start(form, session))


class TestCmdJoinpool(unittest.TestCase):
    def test_command_init(self):
        cmd_joinpool = cmd_joinpool()
        self.assertEqual(expected, cmd_joinpool.command_init())


    def test_complete(self):
        cmd_joinpool = cmd_joinpool()
        self.assertEqual(expected, cmd_joinpool.complete(form, session))


    def test_start(self):
        cmd_joinpool = cmd_joinpool()
        self.assertEqual(expected, cmd_joinpool.start(form, session))


class TestCmdSubmitjob(unittest.TestCase):
    def test_command_init(self):
        cmd_submitjob = cmd_submitjob()
        self.assertEqual(expected, cmd_submitjob.command_init())


    def test_complete(self):
        cmd_submitjob = cmd_submitjob()
        self.assertEqual(expected, cmd_submitjob.complete(form, session))


    def test_start(self):
        cmd_submitjob = cmd_submitjob()
        self.assertEqual(expected, cmd_submitjob.start(form, session))


class TestCmdJobstatus(unittest.TestCase):
    def test_command_init(self):
        cmd_jobstatus = cmd_jobstatus()
        self.assertEqual(expected, cmd_jobstatus.command_init())


    def test_start(self):
        cmd_jobstatus = cmd_jobstatus()
        self.assertEqual(expected, cmd_jobstatus.start(form, session))


class TestCmdCanceljob(unittest.TestCase):
    def setUp(self):
        self.cmd =  cmd_canceljob(config)

    def test_command_init(self):
        self.assertEqual(expected, self.cmd.command_init())

    def test_complete(self):
        self.assertEqual(expected, self.cmd.complete(form, session))

    def test_start(self):
        self.assertEqual(expected, self.cmd.start(form, session))


if __name__ == '__main__':
    unittest.main()
