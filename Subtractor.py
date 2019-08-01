from http import HTTPStatus
import json

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        return subtract(event)
    # TODO
    # elif event['httpMethod'] == 'GET':
    # elif event['httpMethod'] == 'PUT':
    # elif event['httpMethod'] == 'DELETE':
    else:
        return client_error(HTTPStatus.METHOD_NOT_ALLOWED)

def subtract(event):
    try:
        request_id = event['pathParameters']['requestId']
    except:
        return client_error(HTTPStatus.BAD_REQUEST)

    if not event['body'] or not len(event['body']):
        return client_error(HTTPStatus.BAD_REQUEST)

    try:
        # two loads to escape the double-quotes when encoding an object as a JSON string
        inputJSONObject = json.loads(json.loads(event['body']))
    except:
        return client_error(HTTPStatus.BAD_REQUEST)

    if not inputJSONObject['timestamp'] or not inputJSONObject['data']:
        return client_error(HTTPStatus.BAD_REQUEST)

    part1_list = []
    part2_list = []
    for data in inputJSONObject['data']:
        if 'title' in data:
            if data['title'].replace(' ', '').lower() == 'part1':
                part1_list = data['values']
            elif data['title'].replace(' ', '').lower() == 'part2':
                part2_list = data['values']

    if not len(part1_list) or not len(part2_list):
        return client_error(HTTPStatus.BAD_REQUEST)

    result = map(lambda n1,n2: n1-n2, part2_list, part1_list)

    result_dict = {}
    result_dict['title'] = 'Result'
    result_dict['values'] = list(result)

    response_dict = {}
    response_dict['request_id'] = request_id
    response_dict['timestamp'] = inputJSONObject['timestamp']
    response_dict['result'] = result_dict

    return {
        "statusCode": HTTPStatus.OK,
        "body": json.dumps(response_dict)
    }

def client_error(status):
    return {
        'statusCode': status.value,
        'body': status.description
    }