from rest_framework import serializers
from .models import Discount, DiscountCode


class DiscountCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = ['user_id']

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.save()
        return instance


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['brand_name',
                  'discount_percentage',
                  'number_of_codes',
                  'enabled',
                  'valid_from',
                  'valid_to',
                  ]

    def update(self, instance, validated_data):
        instance.brand_name = validated_data.get('brand_name', instance.brand_name)
        instance.discount_percentage = validated_data.get('discount_percentage', instance.discount_percentage)
        instance.number_of_codes = validated_data.get('number_of_codes', instance.number_of_codes)
        instance.enabled = validated_data.get('enabled', instance.enabled)
        instance.valid_from = validated_data.get('valid_from', instance.valid_from)
        instance.valid_to = validated_data.get('valid_to', instance.valid_to)
        instance.save()
        return instance


