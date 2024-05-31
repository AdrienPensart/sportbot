#!/bin/sh

export SETUPTOOLS_USE_DISTUTILS=stdlib

set -e

poetry run isort sportbot tests
poetry run black sportbot tests


