import json 
 
def lambda_handler(event, context): 
    return { 
        'statusCode': 200, 
        'body': 'It is gonna rain day' 
    } 
