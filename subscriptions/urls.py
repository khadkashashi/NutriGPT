from django.urls import path
from subscriptions.views import list_user_sub, pay, callback
urlpatterns = [
    path('',list_user_sub, name="user_sub"),
    path('pay/<int:id>',pay, name="pay"),
    path('callback',callback, name="callback")

]