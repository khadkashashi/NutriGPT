from django.contrib import admin

from .models import SubscriptionPlan, UserSubscription, Payment


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "duration_days",
        "is_active",
        "created_at",
    )
    list_filter = (
        "is_active",
        "created_at",
    )
    search_fields = (
        "name",
        "description",
    )
    ordering = ("name",)
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Subscription Details",
            {
                "fields": (
                    "name",
                    "price",
                    "duration_days",
                    "description",
                    "is_active",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": ("collapse",),
            },
        ),
    )


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "plan",
        "status",
        "start_date",
        "end_date",
    )
    list_filter = (
        "status",
        "plan",
        "start_date",
        "end_date",
    )
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
        "plan__name",
    )
    autocomplete_fields = (
        "user",
        "plan",
    )
    date_hierarchy = "start_date"
    ordering = ("-start_date",)



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "subscription",
        "amount",
        "payment_method",
        "transaction_id",
        "status",
    )
    list_filter = (
        "payment_method",
        "status",
    )
    search_fields = (
        "transaction_id",
        "subscription__user__username",  # Assuming UserSubscription has FK to User
        "subscription__user__email",
    )
    readonly_fields = (
        "transaction_id",
    )
    list_per_page = 25
    ordering = ("-id",)

    fieldsets = (
        (
            "Payment Information",
            {
                "fields": (
                    "subscription",
                    "amount",
                    "payment_method",
                    "transaction_id",
                    "status",
                )
            },
        ),
    )