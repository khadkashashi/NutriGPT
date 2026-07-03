from django.contrib.auth.models import User
from django.db import models


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.PositiveIntegerField(help_text="Duration in days")
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "subscription_plan"


class UserSubscriptionStatus(models.TextChoices):
    ACTIVE =  "Active"
    EXPIRED ="Expired"
    CANCELLED= "Cancelled"
    PENDING= "Pending"
    PAUSED = "Paused"


class UserSubscription(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriptions"
    )
    plan = models.ForeignKey(
        SubscriptionPlan, on_delete=models.CASCADE, related_name="user_subscriptions"
    )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=UserSubscriptionStatus.choices, default=UserSubscriptionStatus.PENDING)

    def __str__(self):
        return f"{self.user.username} - {self.plan} ({self.status})"

    class Meta:
        db_table = "user_subscription"


class PaymentMethod(models.TextChoices):
    ESEWA = "esewa"
    KHALTI = "khalti"
    BANK_TRANSFER = "bank_transfer"
    CASH = "cash"


class PaymentStatus(models.TextChoices):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

class Payment(models.Model):
    subscription = models.ForeignKey(
        UserSubscription, on_delete=models.CASCADE, related_name="payments"
    )
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices, default=PaymentMethod.KHALTI)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)

    def str(self):
        return f"{self.transaction_id} - {self.status}"

    class Meta:
        db_table = "payments"