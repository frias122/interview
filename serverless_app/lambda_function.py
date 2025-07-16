
import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = os.environ['BUCKET']
    try:
        contents = s3.list_objects_v2(Bucket=bucket)
        files = [obj["Key"] for obj in contents.get("Contents", [])]
        return {
            "statusCode": 200,
            "body": str(files)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
