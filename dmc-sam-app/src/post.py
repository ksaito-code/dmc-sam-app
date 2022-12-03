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

  user_id = body.get("user_id")
  date = body.get("date")
  mood = body.get("mood")
  sleeps = body.get("sleeps")
  sleep_minutes = body.get("sleep_minutes")
  memo = body.get("memo")


  # response = daily_moods_table.update_item(
  #     Key={'user_id': user_id, 'date': date},
  #     UpdateExpression="set mood = :m",
  #     ExpressionAttributeValues={
  #         ':m': mood
  #         },
  #     ReturnValues="UPDATED_NEW")
  
  item = {
    "user_id" : user_id,
    "date" : date,
    "mood" : mood,
    "sleeps" : sleeps,
    "sleep_minutes" : sleep_minutes,
    "memo" : memo
  }
  
  daily_moods_table.put_item(Item=item)
  
  return {
      'statusCode': 200,
      'body': 'Successfully inserted data!'
  }