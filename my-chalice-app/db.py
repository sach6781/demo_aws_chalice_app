import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='your-region')

# Access a DynamoDB table
table = dynamodb.Table('your-table-name')

# Perform DynamoDB operations (e.g., put_item, get_item, scan, etc.)

