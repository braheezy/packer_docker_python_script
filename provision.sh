#!/bin/sh

pip install --no-cache-dir -r /tmp/files/requirements.txt

cp -r /tmp/files /usr/src/$PROJECT_NAME
