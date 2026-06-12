import json
import boto3
import pandas as pd

s3 = boto3.client('s3')

def handler(event, context):
    records = event.get('records', [])
    df = pd.DataFrame(records)
    
    # Save to S3
    s3.put_object(
        Bucket='analytics-raw-data',
        Key=f"raw/{context.aws_request_id}.csv",
        Body=df.to_csv(index=False)
    )
    
    return {'statusCode': 200, 'records': len(records)}
