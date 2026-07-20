

from django.urls import reverse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from subscriptions.models import Payment, PaymentMethod, PaymentStatus, UserSubscription

from subscriptions.service import get_payment_url
from rest_framework import status
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Plan'])
class UserPlanPayment(GenericAPIView):
    queryset = UserSubscription.objects.all()

    def get(self,request, id):
        user_sub = UserSubscription.objects.get(id=id)
        payment = get_payment_url(
            url=request.build_absolute_uri(reverse("callback")),
            amount=int(user_sub.plan.price * 100),
            purchase_order_id=user_sub.id,
            purchase_order_name=f"{user_sub.user}-{user_sub.plan.name}",
            name=user_sub.user.username,
            email=user_sub.user.email,
            product_id=user_sub.plan.id,
            quantity=user_sub.plan.duration_days,
            unit_price=int(
                int(user_sub.plan.price * 100) / int(user_sub.plan.duration_days)
            ),
        )

        if payment.get("pidx"):
            payment_data = Payment.objects.create(
                pidx=payment.get("pidx"),
                payment_method=PaymentMethod.KHALTI,
                status=PaymentStatus.PENDING,
                amount=user_sub.plan.price,
                subscription=user_sub,
            )
            return Response(payment)
        else:
            return Response({
                "error":"Pidx doesnot create from khalti"
            }, status.HTTP_400_BAD_REQUEST)