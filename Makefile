clean:
	pip uninstall -y django || true

1_4:
	pip install Django==1.4.1

1_3:
	pip install Django==1.3.3

dependencies:
	pip install raven

test:
	python -m unittest test
