#!/bin/bash

cd /Users/safo/Downloads/tests_demo/api/api_tests2/

# Extract the value of POSTMAN_ENVIRONMENT_JSON into a variable
postman_environment_json=$POSTMAN_ENVIRONMENT_JSON

# Save the environment JSON to a file named postman_environment.json
echo "$postman_environment_json" > postman_environment.json

newman run postman_collection.json --environment postman_environment.json  \
 --reporters cli,junit --reporter-junit-export newman_report.xml

