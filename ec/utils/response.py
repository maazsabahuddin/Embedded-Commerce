
def getResponseObject(success, responseData=None, responseMessage=None):

    response = {
        'success': success,
    }
    if responseData:
        response.update({
            "responseData": responseData
        })
    if responseMessage:
        response.update({
            "responseMessage": responseMessage
        })
    return response
