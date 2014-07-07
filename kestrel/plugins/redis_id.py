"""
    Toxcore: The Sleek XMPP Library replacement
    Copyright (C) 2011  Nathanael C. Fritz, Lance J.T. Stout
    This file is part of Toxcore.

    See the file LICENSE for copying permission.
"""

import redis

#import toxcore
from toxcore.plugins.base import base_plugin


class redis_id(base_plugin):

    """
    Redis ID

    Synchronize the ID values for stanzas between component
    instances. Prevents instances where multiple components
    communicate with a single client and use the same ID values
    for two different Iq sessions.

    Redis keys:
        toxcore:id

    Methods:
        new_id --
        get_id --
    """

    def plugin_init(self):
        """
        """
        self.description = 'Redis ID'
        self.redis = redis.Redis(host=self.config.get('host', 'localhost'),
                                 port=self.config.get('port', 6379),
                                 db=self.config.get('db', 0))

    def post_init(self):
        """"""
        self.redis.setnx('toxcore:id', 0)
        self.xmpp.new_id = self.new_id
        self.xmpp.get_id = self.get_id

    def new_id(self):
        """"""
        return "%X" % self.redis.incr('toxcore:id')

    def get_id(self):
        """"""
        return "%X" % int(self.redis.get('toxcore:id'))
