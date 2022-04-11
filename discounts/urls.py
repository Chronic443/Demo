from django.urls import path
from .views import generate_discount_tokens, update_discount, get_discount

urlpatterns = [
    path('generate-discount-tokens/', generate_discount_tokens, name='generate-discount-tokens'),
    path('update_discount/', update_discount, name='update-discount'),
    path('get_discount/<brand_name>/<user_id>/', get_discount, name='get-discount')
]
