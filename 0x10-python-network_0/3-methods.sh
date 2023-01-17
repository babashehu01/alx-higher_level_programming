#!/bin/bash
# Script that displays all HTTP methods a server can accept
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
