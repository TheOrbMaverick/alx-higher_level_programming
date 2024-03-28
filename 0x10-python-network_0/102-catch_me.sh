#!/bin/bash
# Make a request to the target URL with the correct data to trigger the desired response
curl -sX PUT "http://0.0.0.0:5000/catch_me" -d "user_id=98" > /dev/null
