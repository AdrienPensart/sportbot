#!/bin/bash

set -e

echo "linting : pylint..."
poetry run pylint sportbot

echo "linting : flake8..."
poetry run flake8 sportbot

echo "static type checking : mypy..."
poetry run mypy sportbot
