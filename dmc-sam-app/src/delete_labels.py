# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import json

dynamodb = boto3.resource('dynamodb')
from boto3.dynamodb.conditions import Key
activity_labels_table = dynamodb.Table("ActivityLabels")

def lambda_handler(event, context):

  print("exec : activity labels delete api")
  body = json.loads(event["body"])
  user_id = body['user_id']
  label_id = body['label_id']

  activity_labels_table.update_item(
    Key={'user_id': user_id, 'label_id': label_id},
    UpdateExpression="set disabled = :d",
    ExpressionAttributeValues={
        ':d': True
        },
    ReturnValues="UPDATED_NEW")

  return {
      'statusCode': 200,
      'body': 'Successfully disabled data!'
  }