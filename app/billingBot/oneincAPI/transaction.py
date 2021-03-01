from django.conf import settings

import requests
import json

def get_transaction_by_id(
    transactionID
):
    """
    Get transaction by ID from Oneinc server
            Request
                TransactionId(A Transaction Id)(string)
                AuthenticationKey(Instance authentication key, required)(string)

            Response
                TransactionInformation(A transaction information)
                ResponseCode(Operation response code)
                Message(Response message)
    """

    URL = 'https://stgapiprocessone.oneincsystems.com/api/Transaction/GetTransactionById'
    data = {
        "TransactionId": transactionID,
        "AuthenticationKey": settings.AUTHENTICATIONKEY
    }
    response = requests.post(url=URL, json=data)
    print('GET TRANSACTION ID API START')
    print(response.text)
    print('GET TRANSACTION ID API END')
    return response

def get_transaction_by_batch_if(
    queryAuthenticationKeys,
    batchId,
    transactionStatuses
):
    """
    Get transactions using batch ID from Oneinc server
            Request
                QueryAuthenticationKeys(Authentication keys to limit search query, required)(collection of string)
                BatchId(A Transaction Batch Id)(string)
                TransactionStatuses(Transaction statuses to limit search query)(Collection of TransactionStatus)
                AuthenticationKey(Instance authentication key, required)(string)

            Response
                Transactions(A transaction information)
                ResponseCode(Operation response code)
                Message(Response message)
    """

    URL = '	https://stgapiprocessone.oneincsystems.com/api/Transaction/GetTransactionsByBatchId'
    data = {
        "QueryAuthenticationKeys": [
            queryAuthenticationKeys,
            settings.AUTHENTICATIONKEY
        ],
        "BatchId": batchId,
        "TransactionStatuses": transactionStatuses,
        "AuthenticationKey": settings.AUTHENTICATIONKEY
    }
    response = requests.post(url=URL, json=data)
    print('GET TRANSACTIONS ID BY BATCHID API START')
    print(response.text)
    print('GET TRANSACTIONS ID BY BATCHID API END')
    return response