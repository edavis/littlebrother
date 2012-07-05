#!/usr/bin/env bash

env="littlebrother-env"
dist="$(python setup.py --fullname).tar.gz"

if [ -d $env ]; then
    echo "deleting $env"
    rm -rf $env;
fi

virtualenv $env
${env}/bin/pip install dist/$dist
