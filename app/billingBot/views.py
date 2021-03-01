from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views import View
from core.models import Quote, Policy, User
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views.generic.edit import FormView

import requests
import json

from .forms import UserInformation, UserPayment
from .oneincAPI.credit_card import credit_card_save, credit_card_verfiy, \
                                    credit_card_update, credit_card_charge
from .oneincAPI.eft import eft_save, eft_verify, eft_debit
from .oneincAPI.transaction import get_transaction_by_id, get_transaction_by_batch_if
from .bot.bot_logic import monthly_or_yearly_bot


def get_user_information(request, pk=None):
    """Get the user information function"""
    user = get_object_or_404(User , pk=pk)
    user_model = User.objects.get(pk=request.user.pk)
    # if post = process the data
    if request.method == 'POST':
        form1 = UserInformation(request.POST, instance=user)
        if form1.is_valid():
            form1.save()
            test_get_transaction_patchid = get_transaction_by_batch_if(
                queryAuthenticationKeys='Authentication Key',
                batchId=None,
                transactionStatuses=None
            )
            print('TEST START')
            print(test_get_transaction_patchid.json()['responseCode'])
            print('TEST END')
            # test_get_transaction_id = get_transaction_by_id(
            #     transactionID='15380557'
            # )
            # print('TEST START')
            # print(test_get_transaction_id.json()['responseCode'])
            # print('TEST END')
            # test_charge = credit_card_charge(
            #     amount=100.00,
            #     chargeFee=False,
            #     token=user_model.token_oneinc,
            #     expirationYear='2035',
            #     expirationMonth='9',
            #     name='CHARGE',
            #     zipcode='29201',
            #     address='521 College st',
            #     city='Columbia',
            #     state='SC',
            #     phone='8032430632',
            #     number='4111111111111111',
            #     validationValue='123',
            #     clientReferenceData1='PA-12345',
            #     isRecurring=False,
            #     accountGroupCode="Default",
            #     callbackId=None,
            #     save=False,
            #     convenienceFeeType=None,
            #     customerId=None,
            #     splitPayGroupId=None
            # )
            # print('TEST START')
            # print(test_charge.json()['responseCode'])
            # print('TEST END')
            return redirect(f'/billingbot/users/update_form/{pk}')
    # if get = generate a new form
    else:
        form1 = UserInformation()
        # form2 = UserPayment()

    return render(request, '../templates/user_form.html', {'form1': form1, 'user': user})

def test_verify_credit_card(request):
    """Test function to check the verify credit card api call"""
    test_verify = credit_card_verfiy(
        expirationYear='2035',
        expirationMonth='9',
        name='VERIFY',
        zipcode='29201',
        address='521 College st',
        city='Columbia',
        state='SC',
        phone='8032430632',
        number='4111111111111111',
        validationValue='123',
        callbackId=None,
        clientReferenceData1='1111111',
        customerId=None
    )
    print('TEST START')
    print(test_verify.json()['responseCode'])
    print('TEST END')


def test_save_credit_card(request, pk=None):
    """Test function to save the credit card using api call"""
    test_save = credit_card_save(
        expirationYear='2025',
        expirationMonth='11',
        name='SAVE',
        zipcode='29201',
        address='521 College st',
        city='Columbia',
        state='SC',
        phone='8032430632',
        number='4111111111111111',
        validationValue='123',
        callbackId=None,
        clientReferenceData1='PA-12345',
        customerId=None
    )
    #there is a need to save the token in the database for easy access later
    User.objects.filter(pk=request.user.pk).update(token_oneinc=test_save.json()['token'])
    print('TEST START')
    print(test_save.json()['responseCode'])
    print('TEST END')


def test_update_credit_card(request):
    """Test function to update the credit card information using api call"""
    test_update = credit_card_update(
        token = user_model.token_oneinc,
        expirationYear=2029,
        expirationMonth=10,
        zipcode=29201,
        creditCardNetworkType=None,
        holderaddress=None,
        city=None,
        state=None,
        phone=None
    )
    print('TEST START')
    print(test_update.json()['responseCode'])
    print('TEST END')


def test_charge_credit_card(request):
    """Test function to charge the user credit card using api call"""
    test_charge = credit_card_charge(
        amount=100.00,
        chargeFee=False,
        token=user_model.token_oneinc,
        expirationYear='2035',
        expirationMonth='9',
        name='CHARGE',
        zipcode='29201',
        address='521 College st',
        city='Columbia',
        state='SC',
        phone='8032430632',
        number='4111111111111111',
        validationValue='123',
        clientReferenceData1='PA-12345',
        isRecurring=False,
        accountGroupCode="Default",
        callbackId=None,
        save=False,
        convenienceFeeType=None,
        customerId=None,
        splitPayGroupId=None
    )
    print('TEST START')
    print(test_charge.json()['responseCode'])
    print('TEST END')


def test_verify_eft(request):
    """Test function to verify the eft using api call"""
    test_eft_verify = eft_verify(
        routingNumber='121042882',
        accountNumber='1234567890',
        type=None,
        customerName='EFT ITAY',
        tokenReusability='0',
        token=None,
        clientReferenceData1='PA-11111',
        customerId='None'
    )
    print('TEST START')
    print(test_eft_verify.json()['responseCode'])
    print('TEST END')


def test_save_eft(request):
    """Test function to save the eft using api call"""
    test_eft_save =  eft_save(
        routingNumber='121042882',
        accountNumber='1234567890',
        type=None,
        customerName='ITAY EFT',
        tokenReusability=0,
        clientReferenceData1='PA-54321',
        callbackId=None,
        bypassBankAccountValidation=False,
        customerId=None,
        accountGroupCode=None
    )
    print('TEST START')
    print(test_eft_save.json()['responseCode'])
    print('TEST END')


def test_debit_eft(request):
    """Test function to charge the user eft using api call"""
    test_eft_debit =  eft_debit(
        save=False,
        chargeFee=False,
        convenienceFeeType=None,
        bypassBankAccountValidation=False,
        transactionOrigination=None,
        amount=99.98,
        token=None,
        routingNumber='121042882',
        accountNumber='1234567890',
        type=None,
        customerName='ITAY EFT',
        tokenReusability=0,
        clientReferenceData1='PA-54321',
        isRecurring=False,
        callbackId=None,
        customerId=None,
        accountGroupCode=None
    )
    print('TEST START')
    print(test_eft_debit.json()['responseCode'])
    print('TEST END')



class UsersView(View):
    template_name = '../templates/user_list.html'

    def get(self, request):
        users = User.objects.all()
        return render(request, self.template_name, {'users': users})


class UserDetailView(View):
    template_name = '../templates/user_information.html'

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        user_test = monthly_or_yearly_bot(pk)
        return render(request, self.template_name, {'user': user})


class QuoteListView(ListView):
    model = Quote
    template_name = '../templates/quotes_list.html'


class QuoteDetailView(View):
    model = Quote
    template_name = '../templates/quotes_detail.html'

    def get(self, request, pk):
        # quote = Policy.objects.get(pk=pk)
        quote = get_object_or_404(Quote, pk=pk)
        return render(request, self.template_name, {'quote': quote})

    # def get_user_policy(self):
    #     user_policy_qs = Policy.objects.filter(user=self.request.user)
    #     if user_policy_qs.exists():
    #         return user_policy_qs.first()
    #     return None
    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     current_policy = self.get_user_policy()
    #     # context['current_policy'] = str(current_policy.policy)
    #     return context

class PolicyListView(ListView):
    model = Policy
    template_name = '../templates/policy_list.html'


class PolicyDetailView(View):
    model = Policy
    template_name = '../templates/policy_detail.html'

    def get(self, request, pk):
        policy = monthly_or_yearly_bot(pk)
        return render(request, self.template_name, {'policy': policy})

class MakeAPayment(View):

    def get(self, request, pk, format=None):

        current_policy = Policy.objects.get(user=self.request.user, policy_id=pk)
        print(self.request.user.id)
        print(current_policy)
        URL = 'https://stgportalone.processonepayments.com/Api/Api/Session/Create?PortalOneAuthenticationKey=0ae16856-aef9-4170-86d6-8d3daa96cd14'
        PARAMS = {'PortalOneAuthenticationKey': '0ae16856-aef9-4170-86d6-8d3daa96cd14'}
        r = requests.get(url=URL, headers=PARAMS)
        data = r.json()

        return render(request, '../templates/make_payment.html',
            {
                'user': self.request.user,
                'policy': current_policy,
                'key': data
            })
