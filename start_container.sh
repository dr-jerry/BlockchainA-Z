#!/bin/sh

docker run --rm -it -v `pwd`:/app/ blockpy python /app/blockchain.py
