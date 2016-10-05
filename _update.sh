#!/bin/bash
set -e
./_getdata.py
git submodule update --remote
