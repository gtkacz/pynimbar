build:
	python -m pip install --upgrade setuptools wheel
	python setup.py sdist bdist_wheel

install:
	python -m pip install --upgrade pip
	python -m pip install -e .

deploy:
	build
	python -m twine upload dist/*