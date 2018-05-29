#!/bin/bash
zip -r code.zip lambda_function.py
aws lambda update-function-code --function-name='Travis-Test' --zip-file=fileb://code.zip