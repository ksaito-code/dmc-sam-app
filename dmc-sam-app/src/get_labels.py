# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import uuid
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')

from boto3.dynamodb.conditions import Key	# Keyオブジェクトを利用できるようにする

activity_labels_table = dynamodb.Table("ActivityLabels") 

# ActivityLabelsテーブル検索
def query(user_id):
  option = {
      'KeyConditionExpression':
          Key('user_id').eq(user_id)
  }
  resp = activity_labels_table.query(**option)
  return resp.get('Items', [])

def lambda_handler(event, context):

  print("exec : activity labels get api")
  body = json.loads(event["body"])
    
  user_id = body['user_id']
  items = query(user_id)

  return {
      'statusCode': 200,
      'body': json.dumps(items, default=decimal_default_proc)
  }
  
def decimal_default_proc(obj):
  if isinstance(obj, Decimal):
      return float(obj)
  raise TypeError
