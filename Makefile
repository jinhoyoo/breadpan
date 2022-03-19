build:
	python3 -m pip install --upgrade build
	python3 -m build
	

.PHONY :clean
clean:
	$(shell find . | grep -E "(__pycache__|\.pyc|\.pyo$ )" | xargs rm -rf)
	rm -rf dist/


test:
	python -m unittest discover . -v