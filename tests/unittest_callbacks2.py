import unittest
import kestrel.plugins.kestrel_executor
#import toxcore.plugins
#        self.register_plugin('kestrel_executor',
#                             {'max_tasks': 1},
#                             module='kestrel.plugins.kestrel_executor')
class TestPlugin : 
    def add_event_handler(self,b,c) :
       print ("add")
    def add_command (self,b,c,d,e):
       print ("add command")
    def __getitem__(self,b) :
        print ("get")
        return self
    def __setitem__(self,b,c) :
        print ("set")
        return self
    def makeForm (self, ftype ):
        print ("make form")
        return self
    def boundjid (self  ):
        print ("jidd")
        return "mike@server"

    def addField (self , var , label , required) :
        print ("add field")
        return self
    
class HelloworldTestCase(unittest.TestCase):

    def test_say(self):
        y =  TestPlugin ()
        e = kestrel.plugins.kestrel_executor.kestrel_executor(y, {},)
        e.post_init()
        e.start({},)
        e._handle_task_command(y,y)

#Worker._handle_available of <kestrel.worker.Worker object at 0x90588ac>>, False, False)
        #p Presence=
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
