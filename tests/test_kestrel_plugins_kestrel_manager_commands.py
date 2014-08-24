import unittest
from kestrel.plugins.kestrel_manager.commands import (
    AdhocCommand, 
    cmd_canceljob,
    cmd_jobstatus,
    cmd_joinpool,
    cmd_submitjob,
    cmd_poolstatus,
    

)

class Blah:
    def __init__(self, astr):
        self._str=astr
    def bare (self):
        return self._str

class Session :
    @property
    def from_user(self):
        return Blah("ba")


from kestrel.plugins.xep_0004 import Form

session = Session()

expected = None
payload = None


form = Form()

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
    def setUp(self):
        self.cmd = cmd_poolstatus(config)

    def test_command_init(self):
        self.assertEqual(expected, self.cmd.command_init())

    def test_start(self):
        self.assertEqual(expected, self.cmd.start(form, session))


class TestCmdJoinpool(unittest.TestCase):
    def setUp(self):
        self.cmd =  cmd_joinpool(config)

    def test_command_init(self):
        self.assertEqual(expected, self.cmd.command_init())

    def test_complete(self):
        self.assertEqual(expected, self.cmd.complete(form, session))

    def test_start(self):
        self.assertEqual(expected, self.cmd.start(form, session))


class TestCmdSubmitjob(unittest.TestCase):

    def setUp(self):
        self.cmd =  cmd_submitjob(config)

    def test_command_init(self):
        self.assertEqual(expected, self.cmd.command_init())

    def test_complete(self):
        self.assertEqual(expected, self.cmd.complete(form, session))

    def test_start(self):
        self.assertEqual(expected, self.cmd.start(form, session))


class TestCmdJobstatus(unittest.TestCase):
    def setUp(self):
        self.cmd =  cmd_jobstatus(config)

    def test_command_init(self):
        self.assertEqual(expected, self.cmd.command_init())

    def test_start(self):

        self.assertEqual(expected, self.cmd.start(form, session))


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
