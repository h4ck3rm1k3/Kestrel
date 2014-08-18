import toxcore

class Xep0050(toxcore.ComponentXMPP):
    pass

class Form :
    def addField(self, var=None, label=None, required=None):
        pass

class Xep0004(toxcore.ComponentXMPP):
    def makeForm(self, ftype=None):
        return Form()
      
class XMPP(toxcore.ComponentXMPP):
    def __init__(self, config):
        self._components = {}
        self._components['xep_0050']=Xep0050(config)
        self._components['xep_0004']=Xep0004(config)

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

    def __init__(self, config, xmpp=None):
        self._xmpp= XMPP(config)
    
    
    @property
    def pool_jid(self):
        return "somejid"


    @property
    def submit_jid(self):
        pass

    @property
    def config (self):
        return Config()

    @property
    def xmpp (self):
        return self._xmpp

    def post_init(self):
        pass

    @property
    def whitelist(self):
        pass

    @property
    def jid(self):
        return toxcore.JID()
