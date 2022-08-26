venv:
	python3 -m venv $@

.PHONY: init-dev
init-dev:
	python3 -m pip install -U -r requirements-dev.txt
	python3 -m pip install -U --editable .

.PHONY: clean
clean:
	rm -rf build dist *.egg-info
	find ./ -name '*.pyc' -delete
	find ./ -name __pycache__ -type d -print | xargs rm -rf

.PHONY: archive
archive:
	python3 setup.py sdist bdist_wheel

.PHONY: pypi-test-upload
pypi-test-upload:
	twine upload --repository testpypi dist/*

.PHONY: pypi-upload
pypi-upload:
	twine upload --repository pypi dist/*
