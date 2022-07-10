#!/bin/bash
nodemon --watch . --ext py --exec "python3 -m server 127.0.0.1 $2"