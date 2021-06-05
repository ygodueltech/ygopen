.PHONY: build run help

INFILE=./pyoutput/Trains_vs_Orcust_2.yrpX.pb
ABS_INFILE=$(shell readlink -f "${INFILE}")

all: default

default: help

buildproto: ## build all prootos into python
	protoc --python_out=pyoutput -I=include/ygopen/proto $(shell find include/ygopen/proto -iname "*.proto")

runpy: ## tojson. can pass INFILE=/path/to/foo.pb
	cd pyoutput && poetry run python say.py print-as-json $(ABS_INFILE)


help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
