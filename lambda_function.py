import json 
 
def lambda_handler(event, context): 
    print("Hello from Lambda Function") 
    return { 
        'statusCode': 200, 
        'body': 'Winter is coming' 
    } 
