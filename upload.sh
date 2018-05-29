#!/bin/bash

aws lambda update-function-code --function-name='Travis-Test' --zip-file=fileb://lambda.zip