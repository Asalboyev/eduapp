from django.db import models
from django.db.models import Model, ForeignKey, CASCADE, TimeField, TextChoices, CharField, DecimalField
from django.utils.timezone import now

from course.models import Course
from users.models.user import User


class Enrollments(Model):
    class PaymentMethod(TextChoices):
        CLICK = 'click', 'Click'
        PAYME = 'payme', 'PayMe'
        CASH = 'cash', 'Cash'
        OTHER = 'other', 'Other'

    class PaymentStatus(TextChoices):
        PENDING = 'pending', 'Pending'
        COMPLETED = 'completed', 'Completed'
        FAILED = 'failed', 'Failed'
        REFUNDED = 'refunded', 'Refunded'

    user = ForeignKey(User, CASCADE, related_name="enrollments")
    course = ForeignKey(Course, CASCADE, related_name="enrollments")
    enrolled_at = models.DateTimeField(default=now)
    completed_at = models.DateTimeField(null=True, blank=True)
    payment_method = CharField(max_length=20, choices=PaymentMethod.choices)
    payment_amount = DecimalField(max_digits=10, decimal_places=2)
    payment_status =CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)


class Payments(Model):
    class PaymentMethod(TextChoices):
        CLICK = 'click','Click'
        PAYME = 'payme','PayMe'
        CASH = 'cash','Cash'
        OTHER = 'other','Other'

    class PaymentStatus(TextChoices):
        PENDING = 'pending','Pending'
        COMPLETED = 'completed','Completed'
        FAILED = 'failed','Failed'
        REFUNDED = 'refunded','Refunded'

    user = ForeignKey(User, CASCADE, related_name="payments")
    course = ForeignKey(Course, CASCADE, related_name="course_payments")
    amount = DecimalField(max_digits=10, decimal_places=2)
    payment_method = CharField(max_length=20, choices=PaymentMethod.choices)
    transactionID = CharField(max_length=100, unique=True)
    payment_status =CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

