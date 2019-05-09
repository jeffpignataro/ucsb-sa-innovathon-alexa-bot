import json

def handler(event, context):
    # TODO implement
    QUESTION = 'test'
    responseBody = buildDummyJson(QUESTION)
    returnObj =  {
        'statusCode': 200,
        'body': '{}'.format(json.dumps(responseBody))
    }
    print(returnObj)
    return returnObj

def buildDummyJson(question):
    RETURNJSON = {}
    RETURNJSON["body"] = {}
    RETURNJSON["body"]["version"] = '1.0'
    RETURNJSON["body"]["response"] = {}
    RETURNJSON["body"]["response"]["outputSpeech"] = {}
    RETURNJSON["body"]["response"]["outputSpeech"]["type"] = "PlainText"
    RETURNJSON["body"]["response"]["outputSpeech"]["text"] = "Hi Eric"
    RETURNJSON["body"]["sessionAttributes"] = {}
    RETURNJSON["body"]["userAgent"] = 'ask-node/2.3.0 Node/v8.10.0'
    return RETURNJSON

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