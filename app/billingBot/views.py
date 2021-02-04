from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from core.models import Quote, Policy, User
from django.shortcuts import render, get_object_or_404

import requests


class QuoteListView(ListView):
    model = Quote
    template_name = '../templates/quotes_list.html'


class QuoteDetailView(DetailView):
    model = Quote
    template_name = '../templates/quotes_detail.html'

    def get_user_policy(self):
        user_policy_qs = Policy.objects.filter(user=self.request.user)
        if user_policy_qs.exists():
            return user_policy_qs.first()
        return None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_policy = self.get_user_policy()
        # context['current_policy'] = str(current_policy.policy)
        return context

class PolicyListView(ListView):
    model = Policy
    template_name = '../templates/policy_list.html'


class PolicyDetailView(DetailView):
    model = Policy
    template_name = '../templates/policy_detail.html'


class MakeAPayment(View):

    def get(self, request, pk, format=None):

        current_policy = Policy.objects.get(user=self.request.user, policy_id=pk)
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
