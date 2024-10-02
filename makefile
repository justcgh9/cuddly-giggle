install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

format:
	isort .
	black .

lint:
	mypy .

run:
	python main.py