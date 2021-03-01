from django.urls import path

from . import views

app_name = 'billingBot'

urlpatterns = [
    path('users/update_form/<int:pk>/', views.get_user_information, name = 'update_form'),
    path('users/list/', views.UsersView.as_view(), name='user_list'),
    path('users/information/<int:pk>/', views.UserDetailView.as_view(), name='user_information'),
    path('quote/list/', views.QuoteListView.as_view(), name='quote_list'),
    path('quote/detail/<slug:pk>/', views.QuoteDetailView.as_view(), name='quote_detail'),
    path('policy/list/', views.PolicyListView.as_view(), name='policy_list'),
    path('policy/detail/<slug:pk>/', views.PolicyDetailView.as_view(), name='policy_detail'),
    path('make_payment/<slug:pk>/', views.MakeAPayment.as_view(), name='make_a_payment'),
]
