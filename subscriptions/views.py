from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from subscriptions.models import (
    Payment,
    UserSubscription,
    UserSubscriptionStatus,
    PaymentMethod,
    PaymentStatus,
)
from subscriptions.service import get_payment_url, lookup_khalti_api

# Create your views here.


def list_user_sub(request):
    # user_sub = UserSubscription.objects.filter(status=UserSubscriptionStatus.PENDING)
    # user_sub = UserSubscription.objects.exclude(status=UserSubscriptionStatus.ACTIVE)
    user_sub = UserSubscription.objects.all()
    context = {"user_sub": user_sub}
    return render(request, "user_sub/index.html", context)


def pay(request, id):
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
        context = {"payment": payment["payment_url"]}
        return render(request, "user_sub/pay.html", context)
    else:
        return HttpResponse("something went wrong please contact admin")


def callback(request):
    data = request.GET
    if 'pidx' not in data:
        return HttpResponse("Something went wrong, please contact adim")

    result = lookup_khalti_api(data['pidx'])

    payment = Payment.objects.get(pidx = data['pidx'])
    user_sub = UserSubscription.objects.get(id=payment.subscription.id)
    if result['status'] == "Completed":
        payment.status = PaymentStatus.SUCCESS
        payment.transaction_id = data['transaction_id']
        user_sub.status = UserSubscriptionStatus.ACTIVE
    else:
        payment.status = PaymentStatus.FAILED
        user_sub.status = UserSubscriptionStatus.FAILED
    print(payment)
    payment.save()
    user_sub.save()

    context = {
        "payment":payment
    }


    return render(request, "user_sub/callback.html", context)