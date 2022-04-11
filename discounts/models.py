import uuid
import base64
import hashlib
from django.db import models


class Discount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand_name = models.CharField(max_length=100, unique=True)
    discount_percentage = models.PositiveSmallIntegerField()
    number_of_codes = models.PositiveIntegerField()
    enabled = models.BooleanField(default=False)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand_name


class DiscountCode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField(default=None, blank=True, null=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='discount_codes')
    enabled = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def code(self):
        seed = hashlib.sha1(str(self.id).encode())
        return base64.urlsafe_b64encode(seed.digest()[:10]).decode()

    def __str__(self):
        return self.code


