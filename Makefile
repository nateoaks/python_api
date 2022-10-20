.DEFAULT_GOAL := install

REV=head

install:
	poetry install

test: test-full
test-unit: # `-n auto` for distributed testing
	poetry run pytest -vv -m "not integration" tests/
test-int:
	poetry run pytest -vv -m "integration" tests/
test-full:
	poetry run pytest -vv tests/
test-cov:
	poetry run pytest -vv --cov=python_api --cov-report term-missing tests/

lint:
	poetry run pylint python_api tests
static:
	poetry run mypy -p python_api
bandit:
	poetry run bandit -r python_api

format:
	poetry run isort .
	poetry run black .

check: lint bandit static
prepare: format test check

clean:
	rm -rf dist
	rm -rf .mypy_cache
	rm -rf .pytest_cache
