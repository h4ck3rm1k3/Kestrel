#import toxcore
# from toxcore import JID

from time import sleep, time
import os.path

class Item :
    def __getitem__(self, item):
        return Item()

    def add_identity(self, category, itype, name, jid=None, lang=None):
        pass

    def add_feature(self, cap=None, name=None):
        pass

from tox import Tox




class BaseXMPP(Tox) :
    def __init__(self,config):
        
        self._config=config
        self._identity_file = config.get("TOX","identity_file")
        self.bootstrap_ip = config.get("TOX","node_ip")
        self.bootstrap_port = config.get("TOX","port" )
        self.bootstrap_id = config.get("TOX","ID")

        self._plugins={
            #'xep_0030' : Plugin()
        }
    def register_plugin(self, name, config=None, module=None):
        pass

    # def connect(self):
    #     print 'connecting'
    #     super(self).connect()
    def connect(self):

        if  os.path.exists(self._identity_file):
            self.load_from_file(self._identity_file)

        self.set_name("Kestrel")
        print('ID: %s' % self.get_address())

        print('connecting...')
        self.bootstrap_from_address(self.bootstrap_ip, 
                                    1, 
                                    int(self.bootstrap_port), 
                                    self.bootstrap_id
        )

        # check if connected
        checked = False

        while True:
            print "do"
            self.do()
            status = self.isconnected()

            print "waiting status",status
            if not checked and status:
                print('Connected to DHT.')

                self.save_to_file(self._identity_file)

                checked = True
                return True
            sleep(2)

    @property
    def plugin(self):
        return self._plugins

    def process(self, threaded=None):
        print "enter process",threaded
        checked = False
        while True:
            status = self.isconnected()
            if not checked and status:
                print('Connected to DHT.')
                checked = True
            if checked and not status:
                print('Disconnected from DHT.')
                self.connect()
                checked = False
            self.do()
            sleep(0.01)
        self.do()
        return True

    def register_handler(self, callback):
        pass

    @property
    def default_ns(self):
        return 'something'

    def add_event_handler(self, name, func, threaded=None):
        pass

    @property
    def roster(self):
        pass

    def get_roster(self):
        pass

    def event(self, event, param=None):
        pass

    def disconnect(self):
        pass

    def send_presence(self,pfrom=None, pto=None, ptype=None, pstatus=None):
        pass
    def send_message(self,mto=None, mfrom=None, mbody=None):
        pass

    def response_timeout(self):
        return 60 # just some number for now

    def schedule(self, name, number, event, repeat=None):
        pass

    @property
    def stop(self):
        return

    def __getitem__(self, item):
        return Item()

class ClientXMPP(BaseXMPP) :
    def __init__(self, identity_file, config):
        super(ClientXMPP,self).__init__(identity_file, config)

class JID :
    def __init__(self, value=None):
        pass

    @property
    def full (self):
        return "TODO"

    @property
    def bare(self):
        return "TODO"

class ComponentXMPP(BaseXMPP):

    def add_command (self,b,c,d,e):
        print ("add command")

    @property
    def boundjid(self):
        return JID()

class Message:
    pass
