
from django.urls import path

from subscriptions.api.views import UserPlanPayment

urlpatterns = [
    path('payment/<int:id>',UserPlanPayment.as_view() )
]
