#

class Item :
    def __getitem__(self, item):
        return Item()


class ElementBase:

    def __init__(self, xml=None, str=None):
        pass

    def findall(self, pattern):
        pass

    def _get_sub_text(self, name):
        pass

    def setup(self, xml):
        pass

    @property
    def xml(self):
        pass

    def __getitem__(self, item):
        return Item()

from xml.etree import cElementTree as ET

# class ET:
#     @staticmethod
#     def fromstring(astr):
#         return astr
#     def member(self):
#         pass
#     class Element :
#         def __init__(self, string):
#             pass
#         def append(self, x):
#             pass


def register_stanza_plugin(x,y) :
    pass
