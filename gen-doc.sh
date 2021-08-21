#!/bin/bash

set -e

echo "doc generation..."
poetry run sportbot/main.py readme --output rst > README.rst

echo "rst-linting..."
poetry run rst-lint README.rst
