.PHONY: clean-pyc clean-build docs clean

# Browser Tools
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

# UCloud Tools
GENERATE_TEMPLATE_PATH=../ucloud-api-model-v2/apisdk/lang/python/templates/bash.tpl

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "dist - package"
	@echo "install - install the package to the active Python's site-packages"

# unit test
test: clean
	pytest

test-cov: clean
	pytest --cov=ucloud

test-acc: clean
	USDK_ACC=1 pytest --cov=ucloud

test-all: clean
	tox

lint:
	black --check ucloud/

fmt:
	@black ./ucloud

dev:
	@pip install -e .[dev]

docs:
	#sphinx-apidoc -o docs/services ucloud/services
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

docs-preview:
	$(BROWSER) docs/_build/html/index.html

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

migrate:
	git clone https://github.com/ucloud/ucloud-sdk-python3.git .migrate
	python scripts/migrate.py --source .migrate/ucloud --output ucloud
	python scripts/migrate.py --source .migrate/tests --output tests
	rm -rf .migrate
	black ucloud tests

gen:
	ucloud-model sdk apis --lang python2 --type=public --template
	${GENERATE_TEMPLATE_PATH} --output ./gen.sh
