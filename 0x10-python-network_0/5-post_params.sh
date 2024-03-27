#!/bin/bash
# The script sends POST parameters email and subject with specified values
curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
