#!/bin/bash

for dfile in */Dockerfile; do
	docker build -t rust:$(dirname $dfile) -f $dfile .
done
