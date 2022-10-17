#!/bin/bash
# This script displays the size of the body of a HTTP response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
