from django.http import HttpResponse
from django.shortcuts import render
from subscriptions.models import UserSubscription, UserSubscriptionStatus
from subscriptions.service import get_payment_url

# Create your views here.


def list_user_sub(request):
    # user_sub = UserSubscription.objects.filter(status=UserSubscriptionStatus.PENDING)
    # user_sub = UserSubscription.objects.exclude(status=UserSubscriptionStatus.ACTIVE)
    user_sub = UserSubscription.objects.all()
    context = {
        "user_sub":user_sub
    }
    return render(request,'user_sub/index.html', context)


def pay(request, id):
    user_sub = UserSubscription.objects.get(id=id)
    payment = get_payment_url(
        amount = int(user_sub.plan.price*100),
        purchase_order_id = user_sub.id,
        purchase_order_name = f'{user_sub.user}-{user_sub.plan.name}',
        name = user_sub.user.username,
        email = user_sub.user.email,
        product_id = user_sub.plan.id,
        quantity = user_sub.plan.duration_days,
        unit_price = int(int(user_sub.plan.price * 100) / int(user_sub.plan.duration_days))
    )
    if payment.get('pidx'):
        context = {
            'payment':payment['payment_url']
        }
        return render(request, 'user_sub/pay.html', context)
    else:
        return HttpResponse("something went wrong please contact admin")