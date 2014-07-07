#

class BaseXMPP :
    def register_plugin(self, name, config=None, module=None):
        pass

    def add_event_handler(self, name, func):
        pass

    @property
    def roster(self):
        pass

    def get_roster(self):
        pass

    def event(self, event):
        pass

    def disconnect(self):
        pass

    def send_presence(self,pfrom=None, pto=None, ptype=None):
        pass

class ClientXMPP(BaseXMPP) :
    def __init__(self, jid, password, host=None, port=None):
        pass

class JID :
    def full (self):
        pass

class ComponentXMPP(BaseXMPP):

    def __init__(self, jid, password, host, port):
        pass



    @property
    def boundjid(self):
        return JID()

class Message:
    pass
