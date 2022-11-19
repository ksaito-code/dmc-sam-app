# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import uuid
import json

dynamodb = boto3.resource('dynamodb')

from boto3.dynamodb.conditions import Key	# Keyオブジェクトを利用できるようにする

dmc_table = dynamodb.Table("DmcData") # Dmcテーブル

# Dmcテーブル検索
def dmc_query(user_id_date):
  queryData = dmc_table.query(
    IndexName='user_id_date-created_at-index',
    KeyConditionExpression = Key("user_id_date").eq(user_id_date)
  )
  items=queryData['Items']
  return items

# Dmcテーブルアイテム削除
def dmc_item_delete(id):
  response = dmc_table.delete_item(
    Key={
        'id': id
    },
  )
  return response 

def lambda_handler(event, context):

  print("exec : delete api")
  body = json.loads(event["body"])
  user_id = body['user_id']
  date = body['date']

  # Dmcテーブルからデータを取得
  dmc_items = dmc_query(user_id+date)
  for dmc_item in dmc_items:
    dmc_item_delete(dmc_item['id'])

  return {
      'statusCode': 200,
      'body': 'Successfully inserted data!'
  }