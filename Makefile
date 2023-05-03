SRC_DIR = ./src

lint:
	black $(SRC_DIR)
	flake8 $(SRC_DIR)
	isort $(SRC_DIR)
	mypy $(SRC_DIR)
