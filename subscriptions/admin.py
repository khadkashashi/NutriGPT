from django.contrib import admin
from .models import SubscriptionPlan, UserSubscription, Payment


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration_days', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name']
    ordering = ['price']


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan', 'start_date', 'end_date', 'status']
    list_filter = ['status', 'plan']
    search_fields = ['user__username', 'plan__name']
    ordering = ['-start_date']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'subscription', 'amount', 'payment_method', 'status']
    list_filter = ['status', 'payment_method']
    search_fields = ['transaction_id', 'subscription__user__username']
    ordering = ['-id']