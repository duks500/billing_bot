from django.conf import settings

from .response_code import response_code_api_charge_credit_card, response_code_api_save_credit_card, response_code_api_verify_credit_card, response_code_api_update_credit_card

import requests
import json


def credit_card_save(
    expirationYear,
    expirationMonth,
    name,
    zipcode,
    address,
    city,
    state,
    phone,
    number,
    validationValue,
    callbackId,
    clientReferenceData1,
    customerId
):
    """
    Save credit card to Oneinc endpoint
        Request
            CreditCard(Credit card information, required):
                [
                    ExpirationYear(integer),
                    ExpirationMonth(integer),
                    Holder:
                        [
                            Name(required),
                            Zip(string),
                            Address(string),
                            City(string),
                            State(string),
                            Phone(string)
                        ],
                    Number(string),
                    ValidationValue(string)
                ]
            CallbackId(A callback id associated to save credit card transaction)(string)
            ClientReferenceData(Client reference data):
                [
                    ClientReferenceData1(Used to pass a reference number such as Policy, Quote, or Claim Number. The value will be searchable in the transaction search report)(string)
                ]
            CustomerId(A customer id associated with transaction)(string)
            AuthenticationKey(Instance authentication key, required)(string)

        Response
            Token(ProcessOne payment token)
            TokenCreationTime(Token creation date and time in merchant time zone)
            TimeZone(Short time zone name with daylight saving time suffix)
            BaseCardType(Base Credit Card type)
            ResponseCode(Operation response code)
            Message(Response message)
    """
    URL = 'https://stgapiprocessone.oneincsystems.com/api/CreditCard/Save'
    data = {
        "CreditCard": {
            "ExpirationYear": expirationYear,
            "ExpirationMonth": expirationMonth,
            "Holder": {
                "Name": name,
                "Zip": zipcode,
                "Address": address,
                "City": city,
                "State": state,
                "Phone": phone
            },
            "Number": number,
            "ValidationValue": validationValue
        },
        "CallbackId": callbackId, #Can be changed later
        "ClientReferenceData": {
            "ClientReferenceData1": clientReferenceData1,
        },
        "CustomerId": customerId, #Can be changed later
        "AuthenticationKey": settings.AUTHENTICATIONKEY
    }

    response = requests.post(url=URL, json=data)
    print('SAVE API START')
    response_code_api_save_credit_card(response)
    # print(response.text)
    print('SAVE API END')
    return response


def credit_card_verfiy(
    expirationYear,
    expirationMonth,
    name,
    zipcode,
    address,
    city,
    state,
    phone,
    number,
    validationValue,
    callbackId,
    clientReferenceData1,
    customerId
):
    """
    Veirfy credit card is valid using Oneinc endpoint
        Request
            CreditCard(Credit card information, required):
                [
                    ExpirationYear(integer),
                    ExpirationMonth(integer),
                    Holder:
                        [
                            Name(required)(string),
                            Zip(string),
                            Address(string),
                            City(string),
                            State(string),
                            Phone(string)
                        ],
                    Number(string),
                    ValidationValue(string)
                ]
            CallbackId(A callback id associated to save credit card transaction)(string)
            ClientReferenceData(Client reference data):
                [
                    ClientReferenceData1(Used to pass a reference number such as Policy, Quote, or Claim Number. The value will be searchable in the transaction search report)(string)
                ]
            CustomerId(A customer id associated with transaction)(string)
            AuthenticationKey(Instance authentication key, required)(string)

        Response
            ResponseCode(Operation response code)
            Message(Response message)
    """
    URL = 'https://stgapiprocessone.oneincsystems.com/api/CreditCard/Verify'
    data = {
        "CreditCard": {
            "ExpirationYear": expirationYear,
            "ExpirationMonth": expirationMonth,
            "Holder": {
                "Name": name,
                "Zip": zipcode,
                "Address": address,
                "City": city,
                "State": state,
                "Phone": phone
            },
            "Number": number,
            "ValidationValue": validationValue
        },
        "CallbackId": callbackId, #Can be changed later
        "ClientReferenceData": {
            "ClientReferenceData1": clientReferenceData1,
        },
        "CustomerId": customerId, #Can be changed later
        "AuthenticationKey": settings.AUTHENTICATIONKEY
    }
    response = requests.post(url=URL, json=data)
    print('VERIFY API START')
    print(response.text)
    print('VERIFY API END')
    return response


def credit_card_update(
    token,
    expirationYear,
    expirationMonth,
    zipcode,
    creditCardNetworkType,
    holderaddress,
    city,
    state,
    phone
):
    """
    Update credit card to Oneinc endpoint
        Request
            Token(Saved CreditCard token, required)(string)
            ExpirationYear(Year of the expiration of the credit card)(integer)
            ExpirationMonth(Month of the expiration of the credit card)(integer)
            ZipCode(CreditCard holder Zip code)(string)
            CreditCardNetworkType(Credit Card network type)(value between 0-3)
            HolderAddress(CreditCard holder address)(string)
            City(Customer City)(string)
            State(Customer State)(string)
            phone(Customer Phone)(string)
            AuthenticationKey(Instance authentication key, required)(string)

        Response
            TimeZone(Short time zone name with daylight saving time suffix)
            UpdateTime(Update date and time in merchant time zone)
            ResponseCode(Operation response code)
            Message(Response message)
    """
    URL = 'https://stgapiprocessone.oneincsystems.com/api/CreditCard/Update'
    data = {
        "Token": token,
        "ExpirationYear": expirationYear,
        "ExpirationMonth": expirationMonth,
        "ZipCode": zipcode,
        "CreditCardNetworkType": creditCardNetworkType,
        "HolderAddress": holderaddress,
        "City": city,
        "State": state,
        "Phone": phone,
        "AuthenticationKey": settings.AUTHENTICATIONKEY
    }
    response = requests.post(url=URL, json=data)
    print('UPDATE API START')
    print(response.text)
    print('UPDATE API END')
    return response


def credit_card_charge(
    amount,
    chargeFee,
    token,
    expirationYear,
    expirationMonth,
    name,
    zipcode,
    address,
    city,
    state,
    phone,
    number,
    validationValue,
    clientReferenceData1,
    isRecurring,
    accountGroupCode,
    callbackId,
    save,
    convenienceFeeType,
    customerId,
    splitPayGroupId
):
    """
    Charge credit card to Oneinc endpoint
        Request
            Amount(Charge amount, required)(decimal number)
            ChargeFee(Should we charge with fee (default = true))(boolean)
            Token(Saved CreditCard token, Required if CreditCard is not provided)(string)
            CreditCard(Credit card information, Optional. Either CreditCard or Token parameter is required. If both are provided, Token will be used):
                [
                    ExpirationYear(integer),
                    ExpirationMonth(integer),
                    Holder:
                        [
                            Name(required)(string),
                            Zip(string),
                            Address(string),
                            City(string),
                            State(string),
                            Phone(string)
                        ],
                    Number(string),
                    ValidationValue(string)
                ]
            ClientReferenceData(Client reference data):
                [
                    ClientReferenceData1(Used to pass a reference number such as Policy, Quote, or Claim Number. The value will be searchable in the transaction search report)(string)
                ]
            IsRecurring(Is recurring charge)(boolean)
            AccountGroupCode(Account group code)(string)
            CallbackId(A callback id associated to charge credit card transaction)(string)
            Save(Enables to save and tokenize credit card information)(boolean)
            ConvenienceFeeType(Customizable convenience fee type that is matched with different types of transactions)(string)
            CustomerId(A customer id associated with transaction)(string)
            SplitPayGroupId(A unique number to transactions that are part of "split pay")(string)
            AuthenticationKey(Instance authentication key, required)(string)

        Response
            Token(ProcessOne payment token)
            TransactionId(Transaction ID)
            TransactionDate(Transaction date and time)
            TimeZone(Transaction time zone)
            AuthorizationCode(A gateway Authorization Code)
            BatchNumber(Number of the batch)
            CreditCardType(Credit Card type)
            HolderName(Card Holder Name)
            HolderZip(Card Holder Zip code)
            BaseCardType(Base Credit Card type)
            PostedAmount(Transaction Posted Amount)
            ResponseCode(Operation response code)
            Message(Response message)
    """
    URL = 'https://stgapiprocessone.oneincsystems.com/api/CreditCard/Charge'
    data = {
        "Amount": amount,
        "ChargeFee": chargeFee,
        "Token": token,
        "CreditCard": {
            "ExpirationYear": expirationYear,
            "ExpirationMonth": expirationMonth,
            "Holder": {
                "Name": name,
                "Zip": zipcode,
                "Address": address,
                "City": city,
                "State": state,
                "Phone": phone
            },
            "Number": number,
            "ValidationValue": validationValue
        },
        "ClientReferenceData": {
            "ClientReferenceData1": clientReferenceData1,
        },
        "IsRecurring": isRecurring,
        "AccountGroupCode": accountGroupCode,
        "CallbackId": callbackId,
        "Save": save,
        "ConvenienceFeeType": convenienceFeeType,
        "CustomerId": customerId,
        "SplitPayGroupId": splitPayGroupId,
        "AuthenticationKey": settings.AUTHENTICATIONKEY
    }
    response = requests.post(url=URL, json=data)
    print('CHAREG API START')
    #print(response.text)
    response_code_api_charge_credit_card(response)
    print('CHAREG API END')
    return response
