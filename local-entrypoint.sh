#!/bin/sh

pip install -r requirements.txt

# Then exec the container's main process (what's set as CMD in the Dockerfile).
exec "$@"
