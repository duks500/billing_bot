import json


def response_code_api_charge_credit_card(api_response):
    """Return the response code as a message for credit card"""
    print(api_response.json())
    response_code = api_response.json()['responseCode']

    if response_code == 'Success':
        current_response_code = success(response_code)
    elif response_code == 'InvalidAuthenticationKey':
        current_response_code = invalidAuthenticationKey(response_code)
    elif response_code == 'MerchantDisabled':
        current_response_code = merchantDisabled(response_code)
    elif response_code == 'IncorrectValidationValue':
        current_response_code = incorrectValidationValue(response_code)
    elif response_code == 'AvsVerificationFailed':
        current_response_code = avsVerificationFailed(response_code)
    elif response_code == 'InvalidCardNumber':
        current_response_code = invalidCardNumber(response_code)
    elif response_code == 'CardExpired':
        current_response_code = cardExpired(response_code)
    elif response_code == 'MaxAllowablePaymentsExceeded':
        current_response_code = maxAllowablePaymentsExceeded(response_code)
    elif response_code == 'CardTypeNotAccepted':
        current_response_code = cardTypeNotAccepted(response_code)
    elif response_code == 'Declined':
        current_response_code = declined(response_code)
    elif response_code == 'Call':
        current_response_code = call(response_code)
    elif response_code == 'GatewayInternalError':
        current_response_code = gatewayInternalError(response_code)
    elif response_code == 'CreditCardCustomerNameMissing':
        current_response_code = creditCardCustomerNameMissing(response_code)
    elif response_code == 'OverMaximumPayment':
        current_response_code = overMaximumPayment(response_code)
    elif response_code == 'InvalidCreditCardAmount':
        current_response_code = invalidCreditCardAmount(response_code)
    elif response_code == 'DuplicateTransaction':
        current_response_code = duplicateTransaction(response_code)
    elif response_code == 'InvalidZipcode':
        current_response_code = invalidZipcode(response_code)
    elif response_code == 'InvalidExpirationDate':
        current_response_code = invalidExpirationDate(response_code)
    elif response_code == 'NoProcessorResponse':
        current_response_code = noProcessorResponse(response_code)


def response_code_api_save_credit_card(api_response):
    """Return the response code as a message for credit card"""
    print(api_response.json())
    response_code = api_response.json()['responseCode']

    if response_code == 'Success':
        current_response_code = success(response_code)
    elif response_code == 'InvalidAuthenticationKey':
        current_response_code = invalidAuthenticationKey(response_code)
    elif response_code == 'MerchantDisabled':
        current_response_code = merchantDisabled(response_code)
    elif response_code == 'InvalidCardNumber':
        current_response_code = invalidCardNumber(response_code)
    elif response_code == 'CardExpired':
        current_response_code = cardExpired(response_code)
    elif response_code == 'CardTypeNotAccepted':
        current_response_code = cardTypeNotAccepted(response_code)
    elif response_code == 'Declined':
        current_response_code = declined(response_code)
    elif response_code == 'Call':
        current_response_code = call(response_code)
    elif response_code == 'GatewayInternalError':
        current_response_code = gatewayInternalError(response_code)
    elif response_code == 'CreditCardCustomerNameMissing':
        current_response_code = creditCardCustomerNameMissing(response_code)
    elif response_code == 'InvalidZipcode':
        current_response_code = invalidZipcode(response_code)
    elif response_code == 'InvalidExpirationDate':
        current_response_code = invalidExpirationDate(response_code)
    elif response_code == 'NoProcessorResponse':
        current_response_code = noProcessorResponse(response_code)


def response_code_api_verify_credit_card(api_response):
    """Return the response code as a message for credit card"""
    print(api_response.json())
    response_code = api_response.json()['responseCode']

    if response_code == 'Success':
        current_response_code = success(response_code)
    elif response_code == 'InvalidAuthenticationKey':
        current_response_code = invalidAuthenticationKey(response_code)
    elif response_code == 'MerchantDisabled':
        current_response_code = merchantDisabled(response_code)
    elif response_code == 'InvalidCardNumber':
        current_response_code = invalidCardNumber(response_code)
    elif response_code == 'CardExpired':
        current_response_code = cardExpired(response_code)
    elif response_code == 'CardTypeNotAccepted':
        current_response_code = cardTypeNotAccepted(response_code)
    elif response_code == 'Declined':
        current_response_code = declined(response_code)
    elif response_code == 'Call':
        current_response_code = call(response_code)
    elif response_code == 'GatewayInternalError':
        current_response_code = gatewayInternalError(response_code)
    elif response_code == 'CreditCardCustomerNameMissing':
        current_response_code = creditCardCustomerNameMissing(response_code)
    elif response_code == 'InvalidZipcode':
        current_response_code = invalidZipcode(response_code)
    elif response_code == 'InvalidExpirationDate':
        current_response_code = invalidExpirationDate(response_code)
    elif response_code == 'NoProcessorResponse':
        current_response_code = noProcessorResponse(response_code)


def response_code_api_update_credit_card(api_response):
    """Return the response code as a message for credit card"""
    print(api_response.json())
    response_code = api_response.json()['responseCode']

    if response_code == 'Success':
        current_response_code = success(response_code)
    elif response_code == 'InvalidAuthenticationKey':
        current_response_code = invalidAuthenticationKey(response_code)
    elif response_code == 'MerchantDisabled':
        current_response_code = merchantDisabled(response_code)
    elif response_code == 'IncorrectTransactionId':
        current_response_code = incorrectTransactionId(response_code)
    elif response_code == 'GatewayInternalError':
        current_response_code = gatewayInternalError(response_code)
    elif response_code == 'InvalidZipcode':
        current_response_code = invalidZipcode(response_code)
    elif response_code == 'InvalidExpirationDate':
        current_response_code = invalidExpirationDate(response_code)
    elif response_code == 'NoProcessorResponse':
        current_response_code = noProcessorResponse(response_code)


def response_code_api_save_eft(api_response):
    """Return the response code as a message for EFT"""
    print(api_response.json())
    response_code = api_response.json()['responseCode']

    if response_code == 'Success':
        current_response_code = success(response_code)
    elif response_code == 'InvalidAuthenticationKey':
        current_response_code = invalidAuthenticationKey(response_code)
    elif response_code == 'MerchantDisabled':
        current_response_code = merchantDisabled(response_code)
    elif response_code == 'GatewayInternalError':
        current_response_code = gatewayInternalError(response_code)
    elif response_code == 'InvalidRoutingNumber':
        current_response_code = invalidRoutingNumber(response_code)
    elif response_code == 'InvalidAccountNumber':
        current_response_code = invalidAccountNumber(response_code)
    elif response_code == 'BlockedBankAccount':
        current_response_code = blockedBankAccount(response_code)
    elif response_code == 'EFTCustomerNameMissing':
        current_response_code = eFTCustomerNameMissing(response_code)
    elif response_code == 'NoProcessorResponse':
        current_response_code = noProcessorResponse(response_code)


def response_code_api_debit_eft(api_response):
    """Return the response code as a message for EFT"""
    print(api_response.json())
    response_code = api_response.json()['responseCode']

    if response_code == 'Success':
        current_response_code = success(response_code)
    elif response_code == 'InvalidAuthenticationKey':
        current_response_code = invalidAuthenticationKey(response_code)
    elif response_code == 'MerchantDisabled':
        current_response_code = merchantDisabled(response_code)
    elif response_code == 'MaxAllowablePaymentsExceeded':
        current_response_code = maxAllowablePaymentsExceeded(response_code)
    elif response_code == 'GatewayInternalError':
        current_response_code = gatewayInternalError(response_code)
    elif response_code == 'InvalidRoutingNumber':
        current_response_code = invalidRoutingNumber(response_code)
    elif response_code == 'InvalidAccountNumber':
        current_response_code = invalidAccountNumber(response_code)
    elif response_code == 'BlockedBankAccount':
        current_response_code = blockedBankAccount(response_code)
    elif response_code == 'InvalidEFTAmount':
        current_response_code = invalidEFTAmount(response_code)
    elif response_code == 'EFTCustomerNameMissing':
        current_response_code = eFTCustomerNameMissing(response_code)
    elif response_code == 'ACHTransactionFailed':
        current_response_code = aCHTransactionFailed(response_code)
    elif response_code == 'OverMaximumPayment':
        current_response_code = overMaximumPayment(response_code)
    elif response_code == 'DuplicateTransaction':
        current_response_code = duplicateTransaction(response_code)
    elif response_code == 'NoProcessorResponse':
        current_response_code = noProcessorResponse(response_code)


def success(response_code):
    """Check for success response"""
    if response_code == 'Success':
        print('Success')
        return response_code


def invalidAuthenticationKey(response_code):
    """Check for InvalidAuthenticationKey response"""
    if response_code == 'InvalidAuthenticationKey':
        print('Invalid Authentication Key')
        return response_code


def merchantDisabled(response_code):
    """Check for MerchantDisabled response"""
    if response_code == 'MerchantDisabled':
        print('Your Merchant account is disabled')
        return response_code


def incorrectValidationValue(response_code):
    """Check for IncorrectValidationValue response"""
    if response_code == 'IncorrectValidationValue':
        print('The CVV2 code is invalid')
        return response_code


def avsVerificationFailed(response_code):
    """Check for AvsVerificationFailed response"""
    if response_code == 'AvsVerificationFailed':
        print('AVS failed')
        return response_code


def incorrectTransactionId(response_code):
    """Check for IncorrectTransactionId response"""
    if response_code == 'IncorrectTransactionId':
        print('Indicates that the transactionID that you are sending for a refund or void is not a valid transaction or cannot be found')
        return response_code

def invalidCardNumber(response_code):
    """Check for InvalidCardNumber response"""
    if response_code == 'InvalidCardNumber':
        print('This is an invalid card number')
        return response_code


def cardExpired(response_code):
    """Check for CardExpired response"""
    if response_code == 'CardExpired':
        print('The Card is Expired')
        return response_code


def maxAllowablePaymentsExceeded(response_code):
    """Check for MaxAllowablePaymentsExceeded response"""
    if response_code == 'MaxAllowablePaymentsExceeded':
        print('Maximum Allowable payments exceeded for policy or account')
        return response_code


def cardTypeNotAccepted(response_code):
    """Check for CardTypeNotAccepted response"""
    if response_code == 'CardTypeNotAccepted':
        print('The card type provided is not supported')
        return response_code


def declined(response_code):
    """Check for Declined response"""
    if response_code == 'Declined':
        print('The transaction was declined by the issuing bank')
        return response_code


def call(response_code):
    """Check for Call response"""
    if response_code == 'Call':
        print('Indicates that the merchant should call the issuing bank. It is likely fraud')
        return response_code


def gatewayInternalError(response_code):
    """Check for GatewayInternalError response"""
    if response_code == 'GatewayInternalError':
        print('This generic error can happen for different reasons. The error description will contain more detailed information as to the core of the problem')
        return response_code


def invalidRoutingNumber(response_code):
    """Check for InvalidRoutingNumber response"""
    if response_code == 'InvalidRoutingNumber':
        print('You have sent in an invalid Routing Number')
        return response_code


def invalidAccountNumber(response_code):
    """Check for InvalidAccountNumber response"""
    if response_code == 'InvalidAccountNumber':
        print('You have sent in an invalid Account Number')
        return response_code


def blockedBankAccount(response_code):
    """Check for BlockedBankAccount response"""
    if response_code == 'BlockedBankAccount':
        print('This bank account has been blocked due to past failed payments')
        return response_code


def invalidEFTAmount(response_code):
    """Check for InvalidEFTAmount response"""
    if response_code == 'InvalidEFTAmount':
        print('Amount must be greater than $0')
        return response_code


def eFTCustomerNameMissing(response_code):
    """Check for EFTCustomerNameMissing response"""
    if response_code == 'EFTCustomerNameMissing':
        print('When processing an EFT, you must supply the customer name or you will receive this error')
        return response_code


def creditCardCustomerNameMissing(response_code):
    """Check for CreditCardCustomerNameMissing response"""
    if response_code == 'CreditCardCustomerNameMissing':
        print('When saving a credit card you must provide the customer name')
        return response_code


def aCHTransactionFailed(response_code):
    """Check for ACHTransactionFailed response"""
    if response_code == 'ACHTransactionFailed':
        print('Returned when an error returns for processing EFTDebit transactions')
        return response_code


def creditCardVoidFailed(response_code):
    """Check for CreditCardVoidFailed response"""
    if response_code == 'CreditCardVoidFailed':
        print('The voiding of the credit card transaction has failed')
        return response_code


def batchHasBeenClosed(response_code):
    """Check for BatchHasBeenClosed response"""
    if response_code == 'BatchHasBeenClosed':
        print('This error message is returned when you attempt to void a transaction when the batch has already been closed')
        return response_code


def overMaximumPayment(response_code):
    """Check for OverMaximumPayment response"""
    if response_code == 'OverMaximumPayment':
        print('Payment Amount has exceeded maximum allowed')
        return response_code


def invalidCreditCardAmount	(response_code):
    """Check for InvalidCreditCardAmount response"""
    if response_code == 'InvalidCreditCardAmount':
        print('You have sent in an invalid amount for credit card transaction. Usually occurs when sending in a zero dollar amount')
        return response_code


def duplicateTransaction(response_code):
    """Check for DuplicateTransaction response"""
    if response_code == 'DuplicateTransaction':
        print('A duplicate payment has been entered into the system with the same Amount')
        return response_code


def invalidZipcode(response_code):
    """Check for InvalidZipcode response"""
    if response_code == 'InvalidZipcode':
        print('An invalid zip code was passed')
        return response_code


def invalidExpirationDate(response_code):
    """Check for InvalidExpirationDate response"""
    if response_code == 'InvalidExpirationDate':
        print('An invalid expiration date was passed')
        return response_code


def unableToRefundTransaction(response_code):
    """Check for UnableToRefundTransaction response"""
    if response_code == 'UnableToRefundTransaction':
        print('Transaction has already been refunded')
        return response_code


def partialRefundIsNotAllowed(response_code):
    """Check for PartialRefundIsNotAllowed response"""
    if response_code == 'PartialRefundIsNotAllowed':
        print('Your merchant is not setup to process partial refunds. Please reach out to the support team if you would like this feature enabled')
        return response_code


def batchHasNotBeenClosed(response_code):
    """Check for BatchHasNotBeenClosed response"""
    if response_code == 'BatchHasNotBeenClosed':
        print('You have attempted to refund a payment but the batch has not closed. You should void payment instead')
        return response_code


def noProcessorResponse(response_code):
    """Check for NoProcessorResponse response"""
    if response_code == 'NoProcessorResponse':
        print('An attempt to authorize a card through the card network has timed out. You should try again')
        return response_code


def operationNotSupportedByGateway(response_code):
    """Check for OperationNotSupportedByGateway response"""
    if response_code == 'OperationNotSupportedByGateway':
        print('This error may occur when trying to execute operation with incorrect settings')
        return response_code


def operationNotSupportedByMerchant(response_code):
    """Check for OperationNotSupportedByMerchant response"""
    if response_code == 'OperationNotSupportedByMerchant':
        print('This error may occur when trying to execute operation which is currently disabled for merchant')
        return response_code
