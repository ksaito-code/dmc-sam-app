# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import uuid
import json

dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):

  print("exec : post api")
  body = json.loads(event["body"])

  dynamodb_client.put_item(TableName='DmcData', Item={'id': {'S': str(uuid.uuid4())}, \
                                                      'user_id': {'S': body['user_id']}, \
                                                      'date': {'S': body['date']}, \
                                                      'mood': {'S': body['mood']}})
  return {
      'statusCode': 200,
      'body': 'Successfully inserted data!'
  }