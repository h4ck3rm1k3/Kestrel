import unittest
import kestrel.plugins.kestrel_executor
import sleekxmpp.plugins
#        self.register_plugin('kestrel_executor',
#                             {'max_tasks': 1},
#                             module='kestrel.plugins.kestrel_executor')
class TestPlugin : 
    def add_event_handler(a,b,c) :
        print ("add")
    def add_command (a,b,c,d,e):
        print ("add command")
    def __getitem__(a,b) :
        print ("get")
        return a
    def __setitem__(a,b,c) :
        print ("set")
        return a
    def makeForm (a, ftype ):
        print ("make form")
        return a
    def boundjid (a  ):
        print ("jidd")
        return "mike@server"
    def addField (a , var , label , required) :
        print ("add field")
        return a
    
class HelloworldTestCase(unittest.TestCase):

    def test_say(self):
        y =  TestPlugin ()
        e = kestrel.plugins.kestrel_executor.kestrel_executor(y, {},)
        e.post_init()
        e.start({},)
        e._handle_task_command(y,y)

#Worker._handle_available of <kestrel.worker.Worker object at 0x90588ac>>, False, False)
        p Presence=
#Presence: <presence to="h4ck3rm1k3_worker10@h4ck3rm1k3-sixxs.mooo.com/9134b62b" from="h4ck3rm1k3_worker10@h4ck3rm1k3-sixxs.mooo.com/47843cd2" />
# (<presence to="h4ck3rm1k3_worker10@h4ck3rm1k3-sixxs.mooo.com/9134b62b" from="h4ck3rm1k3_worker10@h4ck3rm1k3-sixxs.mooo.com/47843cd2" />,)


        print "ok"

def suite():
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        suite.addTest(loader.loadTestsFromTestCase(HelloworldTestCase))
        return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
