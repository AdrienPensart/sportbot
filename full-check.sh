#!/bin/sh

set -e
trap '[ $? -eq 0 ] && exit 0 || echo "$0 FAILED"' EXIT

bash linting.sh
bash gen-doc.sh

poetry run pytest
