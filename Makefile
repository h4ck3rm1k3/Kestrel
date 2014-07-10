flake :
	bash ./flakes.sh

lint :
	bash ./lint.sh

test1:
	PYTHONPATH=. python  tests/unittest_callbacks.py 
