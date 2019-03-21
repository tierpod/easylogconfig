venv:
	virtualenv -p /usr/bin/python venv

.PHONY: init-dev
init-dev:
	pip install -U -r requirements-dev$(PY).txt
	pip install -U --editable .

.PHONY: clean
clean:
	rm -rf build dist *.egg-info
	find ./ -name '*.pyc' -delete
	find ./ -name __pycache__ -type d -print | xargs rm -r

.PHONY: archive
archive:
	python setup.py sdist

