#!/bin/bash

set -e

sh code-format.sh

echo "linting : ruff..."
poetry run ruff check sportbot tests

echo "linting : pylint..."
poetry run pylint sportbot tests

echo "linting : flake8..."
poetry run flake8 sportbot tests

echo "static type checking : mypy..."
poetry run mypy sportbot tests