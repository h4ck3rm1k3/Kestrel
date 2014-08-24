
test :
	~/.local/bin/nosetests
flake :
	bash ./flakes.sh

lint :
	bash ./lint.sh


test1:
	PYTHONPATH=. python  tests/unittest_callbacks.py 

testone :
	PYTHONPATH=${HOME}/new3/xmpp/Kestrel/ python  tests/test_kestrel_plugins_kestrel_client.py
