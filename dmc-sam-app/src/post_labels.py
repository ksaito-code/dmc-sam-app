# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import json

dynamodb = boto3.resource('dynamodb')
from boto3.dynamodb.conditions import Key
activity_labels_table = dynamodb.Table('ActivityLabels')

def lambda_handler(event, context):

  print("exec : post labels api")
  body = json.loads(event["body"])

  user_id = body.get("user_id")
  label_name = body.get("label_name")
  label_id = str(get_label_id(user_id))

  item = {
    "user_id" : user_id,
    "label_name" : label_name,
    "label_id" : label_id,
    "disabled" : False
  }
  
  activity_labels_table.put_item(Item=item)
  
  return {
      'statusCode': 200,
      'body': 'Successfully inserted data!'
  }

# ActivityLabelsテーブル検索
def get_label_id(user_id):
  option = {
      'KeyConditionExpression':
          Key('user_id').eq(user_id)
  }
  items = activity_labels_table.query(**option).get('Items', [])
  return int(items[-1]['label_id']) + 1
