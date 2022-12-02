# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import uuid
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')

from boto3.dynamodb.conditions import Key	# Keyオブジェクトを利用できるようにする

dmc_table = dynamodb.Table("DailyMoods") 

# DailyMoodsテーブル検索
def query(user_id, start_date, end_date):
  option = {
      'KeyConditionExpression':
          Key('user_id').eq(user_id) & \
          Key('date').between(start_date, end_date)
  }
  resp = dmc_table.query(**option)
  return resp.get('Items', [])

def lambda_handler(event, context):

  print("exec : get api")
  body = json.loads(event["body"])
    
  user_id = body['user_id']
  start_date = body['start_date']
  end_date = body['end_date'] 

  # Dmcテーブルからデータを取得
  items = query(user_id, start_date, end_date)

  return {
      'statusCode': 200,
      'body': json.dumps(items, default=decimal_default_proc)
  }
  
def decimal_default_proc(obj):
  if isinstance(obj, Decimal):
      return float(obj)
  raise TypeError
