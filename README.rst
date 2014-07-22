====================================================
Kestrel: An XMPP-based Many-Task Computing Framework
====================================================

Description:
------------
Kestrel is a job scheduler and dispatcher for distributed computing systems,
particularly Virtual Organization Clusters, and uses XMPP_ for monitoring the
state of all compute elements in the cluster and dispatching tasks.

Dependencies:
-------------
Kestrel depends on the 1.0 release (presently the develop branch) of the
SleekXMPP_ library, but there currently is no SleekXMPP package on PyPI_.
Download and install a copy from GitHub_ before installing ``kestrel``.

It uses XEP-0014 and your xmpp server needs to support that. http://xmpp.org/extensions/xep-0114.html#proto
See also : https://bitbucket.org/legastero/kestrel/wiki/XMPP


.. _XMPP: http://xmpp.org
.. _SleekXMPP: http://github.com/fritzy/SleekXMPP
.. _GitHub: http://github.com/fritzy/SleekXMPP
.. _PyPI: http://pypi.python.org


Run :

PYTHONPATH=/mnt/data/home/mdupont/new3/Kestrel python scripts/kestrel_driver.py worker
PYTHONPATH=/mnt/data/home/mdupont/new3/Kestrel python scripts/kestrel_driver.py manager
PYTHONPATH=/mnt/data/home/mdupont/new3/Kestrel python scripts/kestrel_driver.py submit
PYTHONPATH=/mnt/data/home/mdupont/new3/Kestrel python scripts/kestrel_driver.py cancel
PYTHONPATH=/mnt/data/home/mdupont/new3/Kestrel python  scripts/kestrel_driver.py status
