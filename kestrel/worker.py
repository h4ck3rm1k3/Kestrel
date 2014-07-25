"""
    Kestrel: An XMPP-based Job Scheduler
    Copyright (C) 2011 Lance Stout
    This file is part of Kestrel.

    See the file LICENSE for copying permission.
"""

#import logging
#logging.basicConfig()
import toxcore


class Worker(toxcore.ClientXMPP):

    def __init__(self, identity_file, config):
        toxcore.ClientXMPP.__init__(self, identity_file, config)

        if config is None:
            config = {}
        self._config = config
        self._manager_id = self._config.get('worker','manager_id')

        self.register_plugin('kestrel_executor',
                             {'max_tasks': 1},
                             module='kestrel.plugins.kestrel_executor')

        self.add_event_handler("session_start", self.start)
        self.add_event_handler("got_online", self.manager_online)

    def start(self, event):
        self.get_roster()
        self.send_presence()
        self.manager_online(direct=True)

    def manager_online(self, presence=None, direct=False):
        if direct or presence['from'] == self.manager:
            resp = self['xep_0050'].send_command(jid=self.manager,
                                                node='join_pool')
            if resp['type'] == 'result':
                sessionid = resp['command']['sessionid']
                caps = self.config['features']
                form = self['xep_0004'].makeForm(ftype='submit')
                form.addField(ftype='text-multi',
                              var='capabilities',
                              value="\n".join(caps))
                self['xep_0050'].send_command(jid=self.manager,
                                             node='join_pool',
                                             sessionid=sessionid,
                                             action='complete',
                                             payload=form)
