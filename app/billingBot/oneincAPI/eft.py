from django.conf import settings

from .response_code import response_code_api_save_eft
import requests
import json


def eft_save(
    routingNumber,
    accountNumber,
    type,
    customerName,
    tokenReusability,
    clientReferenceData1,
    callbackId,
    bypassBankAccountValidation,
    customerId,
    accountGroupCode
):
    """
    Save EFT to Oneinc endpoint
        Request
            EftDetails(Eft details):
                [
                    RoutingNumber(The bank routing number. Must only contain numbers, required)(string)
                    AccountNumber(Account number. Must contain only numbers, required)(string)
                    Type(EFT account type - Checking / Savings)(value between 0-2)
                    CustomerName(Customer name, required)(string)
                    TokenReusability(0=Do not reuse, 1=reuse)(values between 0-1)
                ]
            CallbackId(A callback id associated to save EFT transaction)(string)
            BypassBankAccountValidation(Bypassing bank account validation)(boolean)
            CustomerId(A customer id associated with transaction)(string)
            AccountGroupCode(This field is used to route money to different accounts based on a predefined groups)(string)
            AuthenticationKey(Instance authentication key, required)(string)

        Response
            Token(Saved Eft token)
            BankName(Bank name)
            ServerReferenceData(Additional response data)
            TimeZone(Short time zone name with daylight saving time suffix)
            TokenCreationTime(Token creation date and time in merchant time zone)
            ResponseCode(Operation response code)
            Message(Response message)
    """
    URL = 'https://stgapiprocessone.oneincsystems.com/api/Eft/Save'
    data = {
        "EftDetails": {
            "RoutingNumber": routingNumber,
            "AccountNumber": accountNumber,
            "Type": type,
            "CustomerName": customerName,
            "TokenReusability": tokenReusability
        },
        "ClientReferenceData": {
            "ClientReferenceData1": clientReferenceData1,
        },
        "CallbackId": callbackId,
        "BypassBankAccountValidation": bypassBankAccountValidation,
        "CustomerId": customerId,
        "AccountGroupCode": accountGroupCode,
        "AuthenticationKey": settings.AUTHENTICATIONKEY
    }
    response = requests.post(url=URL, json=data)
    print('EFT SAVE API START')
    # print(response.text)
    response_code_api_save_eft(response)
    print('EFT SAVE API END')
    return response


def eft_debit(
    save,
    chargeFee,
    convenienceFeeType,
    bypassBankAccountValidation,
    transactionOrigination,
    amount,
    token,
    routingNumber,
    accountNumber,
    type,
    customerName,
    tokenReusability,
    clientReferenceData1,
    isRecurring,
    callbackId,
    customerId,
    accountGroupCode
):
    """
    Charge EFT to Oneinc endpoint
        Request
            save(Enables to save and tokenize eft information)(boolean)
            ChargeFee(Should we charge with fee)(boolean)
            ConvenienceFeeType(Customizable convenience fee type that is matched with different types of transactions)(string)
            BypassBankAccountValidation(Bypassing bank account validation)(boolean)
            TransactionOrigination(Establishes transaction origination to define Standard Entry Class (SEC) code type for Automated Clearing House (ACH) File):
                [
                    Undefined(=0, Transaction Origination is undefined),
                        WEB(=1, Reoccurring payment, means authorization was provided over the internet),
                        PPD(=2, Prearranged Payment and Deposit Entry)
                ]
            Amount(Amount to charge, required)(decimal number)
            Token(Saved Eft token)(string)
            EftDetails(Eft details):
                [
                    RoutingNumber(The bank routing number. Must only contain numbers, required)(string)
                    AccountNumber(Account number. Must contain only numbers, required)(string)
                    Type(EFT account type - Checking / Savings)(value between 0-2)
                    CustomerName(Customer name, required)(string)
                    TokenReusability(0=Do not reuse, 1=reuse)(values between 0-1)
                ]
            ClientReferenceData(Client reference data):
                [
                    ClientReferenceData1(Used to pass a reference number such as Policy, Quote, or Claim Number. The value will be searchable in the transaction search report)(string)
                ]
            IsRecurring(Is recurring charge)(boolean)
            CustomerId(A customer id associated with transaction)(string)
            AccountGroupCode(This field is used to route money to different accounts based on a predefined groups)(string)
            AuthenticationKey(Instance authentication key, required)(string)

        Response
            Token(Saved Eft token)
            ServerReferenceData(Additional response data)
            PostedAmount(Transaction Posted Amount)
            BankName(Bank name)
            TransactionId(Transaction ID)
            TransactionDate(Transaction date and time)
            TimeZone(Short time zone name with daylight saving time suffix)
            BatchNumber(Number of the batch)
            ResponseCode(Operation response code)
            Message(Response message)
    """
    URL = 'https://stgapiprocessone.oneincsystems.com/api/Eft/Debit'
    data = {
        "Save": save,
        "ChargeFee": chargeFee,
        "ConvenienceFeeType": convenienceFeeType,
        "BypassBankAccountValidation": bypassBankAccountValidation,
        "TransactionOrigination": transactionOrigination,
        "Amount": amount,
        "Token": token,
        "EftDetails": {
            "RoutingNumber": routingNumber,
            "AccountNumber": accountNumber,
            "Type": type,
            "CustomerName": customerName,
            "TokenReusability": tokenReusability
        },
        "ClientReferenceData": {
            "ClientReferenceData1": clientReferenceData1,
        },
        "IsRecurring": isRecurring,
        "CallbackId": callbackId,
        "CustomerId": customerId,
        "AccountGroupCode": accountGroupCode,
        "AuthenticationKey": settings.AUTHENTICATIONKEY
    }

    response = requests.post(url=URL, json=data)
    print('EFT VERIFY API START')
    print(response.text)
    print('EFT VERIFY API END')
    return response


def eft_verify(
    routingNumber,
    accountNumber,
    type,
    customerName,
    tokenReusability,
    token,
    clientReferenceData1,
    customerId
):
    """
    Veirfy EFT is valid using Oneinc endpoint
        Request
            EftDetails(Eft details):
                [
                    RoutingNumber(The bank routing number. Must only contain numbers, required)(string)
                    AccountNumber(Account number. Must contain only numbers, required)(string)
                    Type(EFT account type - Checking / Savings)(value between 0-2)
                    CustomerName(Customer name, required)(string)
                    TokenReusability(0=Do not reuse, 1=reuse)(values between 0-1)
                ]
            Token(Saved Eft Token)(string)
            ClientReferenceData(Client reference data):
                [
                    ClientReferenceData1(Used to pass a reference number such as Policy, Quote, or Claim Number. The value will be searchable in the transaction search report)(string)
                ]
            CustomerId(A customer id associated with transaction)(string)
            AuthenticationKey(Instance authentication key, required)(string)

        Response
            ServerReferenceData(Additional response data)
            ResponseCode(Operation response code)
            Message(Response message)
    """
    URL = 'https://stgapiprocessone.oneincsystems.com/api/Eft/VerifyBankAccount'
    data = {
        "EftDetails": {
            "RoutingNumber": routingNumber,
            "AccountNumber": accountNumber,
            "Type": type,
            "CustomerName": customerName,
            "TokenReusability": tokenReusability
        },
        "Token": token,
        "ClientReferenceData": {
            "ClientReferenceData1": clientReferenceData1,
        },
        "CustomerId": customerId,
        "AuthenticationKey": settings.AUTHENTICATIONKEY
    }
    response = requests.post(url=URL, json=data)
    print('EFT VERIFY API START')
    print(response.text)
    print('EFT VERIFY API END')
    return response
