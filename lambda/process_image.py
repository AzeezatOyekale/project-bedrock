import json

def lambda_handler(event, context):
    # This grabs the filename from the S3 upload event
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        print(f"Image received: {key} from bucket: {bucket}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Image logged successfully!')
    }