init:
	pip install -r requirements.txt

run:
	env FLASK_APP=flask/main flask run

.PHONY :clean
clean:
	$(shell find . | grep -E "(__pycache__|\.pyc|\.pyo$ )" | xargs rm -rf)

test:
	python -m unittest discover . -v