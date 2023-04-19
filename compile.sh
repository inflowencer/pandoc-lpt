#!/bin/bash

docker build -t pandoc-lpt --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) .