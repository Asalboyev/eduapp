from django.contrib import admin
from .models import Enrollments, Payments


@admin.register(Enrollments)
class EnrollmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'enrolled_at', 'completed_at', 'payment_method', 'payment_amount', 'payment_status')
    list_filter = ('payment_method', 'payment_status', 'enrolled_at')
    search_fields = ('user__email', 'course__title')
    autocomplete_fields = ('user', 'course')
    date_hierarchy = 'enrolled_at'
    ordering = ('-enrolled_at',)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'amount', 'payment_method', 'payment_status', 'transactionID', 'created_at', 'updated_at')
    list_filter = ('payment_method', 'payment_status', 'created_at')
    search_fields = ('user__email', 'transactionID', 'course__title')
    autocomplete_fields = ('user', 'course')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

