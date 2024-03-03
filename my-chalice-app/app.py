from chalice import Chalice

app = Chalice(app_name='my-chalice-app')

# DynamoDB Table
app.dynamodb.create_table(
    TableName='my_table',
    KeySchema=[
        {'AttributeName': 'id', 'KeyType': 'HASH'}
    ],
    AttributeDefinitions=[
        {'AttributeName': 'id', 'AttributeType': 'N'}
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }

)

# CRUD Operations
@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/items', methods=['GET'])
def list_items():
    return app.dynamodb.tables['my_table'].scan()

@app.route('/items/{item_id}', methods=['GET'])
def get_item(item_id):
    return app.dynamodb.tables['my_table'].get_item(Key={'id': int(item_id)})

@app.route('/items', methods=['POST'])
def create_item():
    request = app.current_request
    item = request.json_body
    app.dynamodb.tables['my_table'].put_item(Item=item)
    return {'status': 'success'}

@app.route('/items/{item_id}', methods=['PUT'])
def update_item(item_id):
    request = app.current_request
    updated_item = request.json_body
    app.dynamodb.tables['my_table'].update_item(
        Key={'id': int(item_id)},
        UpdateExpression='SET #attrName = :attrValue',
        ExpressionAttributeNames={'#attrName': 'attribute_name'},
        ExpressionAttributeValues={':attrValue': updated_item['attribute_name']}
    )
    return {'status': 'success'}

@app.route('/items/{item_id}', methods=['DELETE'])
def delete_item(item_id):
    app.dynamodb.tables['my_table'].delete_item(Key={'id': int(item_id)})
    return {'status': 'success'}






  





















