from django import forms

from core.models import Quote, Policy, User


class UserInformation(forms.ModelForm):

    class Meta:
        model = User
        fields = ['phone_number', 'address_1', 'address_2', 'city', 'zipcode', 'state']


class UserPayment(forms.Form):

    expYear = forms.IntegerField(min_value='0', max_value='2050')
    # expMonth = forms.IntegerField(min_value='01', max_value='12')
    # creditNumber = forms.IntegerField(min_value='0', max_value='9999999999999999')
    # creditValue = forms.IntegerField(min_value='000', max_value='999')
