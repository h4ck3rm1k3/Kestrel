import toxcore

class Xep0050(toxcore.ComponentXMPP):
    pass
      
class XMPP(toxcore.ComponentXMPP):
    def __init__(self):
        self._components = {}
        self._components['xep_0050']=Xep0050()

    def __getitem__(self, x):
        return self._components[x]

from toxcore import JID
        
class Config:

    def get(self, name, default=""):
        if name == 'jid':
            return JID(default)
        else:
            print "config get %s with default %s" %(name,default)
            return default


class base_plugin :

    def __init__(self, xmpp, config):
        self._xmpp= XMPP()
        
    @property
    def config (self):
        return Config()

    @property
    def xmpp (self):
        return self._xmpp

    def post_init(self):
        pass

    def whitelist(self):
        pass

    @property
    def jid(self):
        return toxcore.JID()
