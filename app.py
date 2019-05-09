import json

def lambda_handler(event, context):
    # TODO implement
    QUESTION = 'test'
    responseBody = buildAlexaJson(QUESTION)
    returnObj =  {
        'statusCode': 200,
        'body': json.dumps(responseBody)
    }
    print(returnObj)
    return returnObj

def buildAlexaJson(question):
    RETURNJSON = {}
    RETURNJSON["body"] = {}
    RETURNJSON["body"]["version"] = '1.0'
    RETURNJSON["body"]["response"] = {}
    RETURNJSON["body"]["response"]["outputSpeech"] = {}
    RETURNJSON["body"]["response"]["outputSpeech"]["type"] = "SSML"
    RETURNJSON["body"]["response"]["outputSpeech"]["ssml"] = "<speak>Hi Eric!</speak>"
    RETURNJSON["body"]["response"]["type"] = "_DEFAULT_RESPONSE"
    RETURNJSON["body"]["sessionAttributes"] = {}
    RETURNJSON["body"]["userAgent"] = 'ask-node/2.3.0 Node/v8.10.0'
    return RETURNJSON