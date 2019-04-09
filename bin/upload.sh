#!/bin/bash

zip -r code.zip lambda_function.py package_info.py __init__.py
aws lambda update-function-code --function-name='civicSandboxPackages' --zip-file=fileb://code.zip