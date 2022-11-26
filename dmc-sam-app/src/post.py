# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import uuid
import json

dynamodb = boto3.resource('dynamodb')
daily_moods_table = dynamodb.Table('DailyMoods')

def lambda_handler(event, context):

  print("exec : post api")
  body = json.loads(event["body"])

  response = daily_moods_table.update_item(
      Key={'user_id': body['user_id'], 'date': body['date']},
      UpdateExpression="set mood=:m",
      ExpressionAttributeValues={
          ':m': body['mood']},
      ReturnValues="UPDATED_NEW")

  # print(response)
  
  return {
      'statusCode': 200,
      'body': 'Successfully inserted data!'
  }