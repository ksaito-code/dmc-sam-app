# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import uuid
import json

dynamodb = boto3.resource('dynamodb')

from boto3.dynamodb.conditions import Key	# Keyオブジェクトを利用できるようにする

dmc_table = dynamodb.Table("DailyMoods") 

# DailyMoodsテーブル検索
def get_item(user_id, date):
  response = dmc_table.get_item(
    Key={
      'user_id': user_id,
      'date': date
    }
  )
  return response['Item']

def lambda_handler(event, context):

  print("exec : get api")
  body = json.loads(event["body"])
    
  user_id = body['user_id']
  date = body['date']

  # Dmcテーブルからデータを取得
  items = get_item(user_id, date)

  return {
      'statusCode': 200,
      'body': json.dumps(items)
  }