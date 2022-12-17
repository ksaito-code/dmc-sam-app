# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
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
  activities = body.get("activities")
  
  item = {
    "user_id" : user_id,
    "date" : date,
    "mood" : mood,
    "sleeps" : sleeps,
    "sleep_minutes" : sleep_minutes,
    "memo" : memo,
    "activities" : activities
  }
  
  daily_moods_table.put_item(Item=item)
  
  return {
      'statusCode': 200,
      'body': 'Successfully inserted data!'
  }