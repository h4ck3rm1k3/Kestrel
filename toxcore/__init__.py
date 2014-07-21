#import toxcore
# from toxcore import JID

class Item :
    def __getitem__(self, item):
        return Item()

    def add_identity(self, category, itype, name):
        pass

    def add_feature(self, cap=None, name=None):
        pass

class BaseXMPP :
    def __init__(self):
        self._plugins={
            #'xep_0030' : Plugin()
        }
    def register_plugin(self, name, config=None, module=None):
        pass

    @property
    def plugin(self):
        return self._plugins

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
    def __init__(self, jid, password, host=None, port=None):
        pass

class JID :
    @property
    def full (self):
        return "TODO"

    @property
    def bare(self):
        return "TODO"

class ComponentXMPP(BaseXMPP):

    def __init__(self, jid=None, password=None, host=None, port=None):
        pass
    def add_command (self,b,c,d,e):
        print ("add command")

    @property
    def boundjid(self):
        return JID()

class Message:
    pass
