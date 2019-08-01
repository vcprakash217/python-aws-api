# python-aws-api

REST API to subtract numbers that exist in the same index of two arrays in a JSON format passed in POST payload.

## Input POST Value:
{
  “timestamp”: 1493758596,
  “data”: [
            { “title”: “Part 1”, “values”: [0, 3, 5, 6, 2, 9] },
            { “title”: “Part 2”, “values”: [6, 3, 1, 3, 9, 4] }
          ]
}
The service shall take the array from Part 1 and subtract the values from Part 2, subtracting numbers that exist in the same index of the array. The final array is also the same size (6).
The return value will be a JSON document in the following format containing the resultant array and request ID.

Output:
{ “request_id”: “<request_id>”, “timestamp”: 1493758596, “result”: { “title”: “Result”, “values”: […] } }


## Access 
	Amazon API Gateway was used to expose the API. It can be accessed at below url 
https://4egwkdt5x8.execute-api.us-west-2.amazonaws.com/staging/compute/{requestId}


## Code
API was developed using Python and AWS APIGateway console

## Files
Subtractor.py – Routes, validates and responds to the requests
SubtractorTest.py – unit tests the Subtractor.py file

## Setup
1.	Install Python3.7
2.	Install AWS CLI
3.	Configure AWS access keys, region and format using ‘aws configure’

## Testing
Run unit tests in SubtractorTest.py file


## TODO
1.	Add more endpoints
2.	Handle GET, PUT and DELETE requests

## References
1.	https://www.alexedwards.net/blog/serverless-api-with-go-and-aws-lambda#deploying-the-api
2.	https://sysadmins.co.za/api-gateway-with-lambda-using-python-on-aws-to-post-info-to-rocketchat/
