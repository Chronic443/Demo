from django.test import TestCase
from .models import Discount

import datetime


class TestModels(TestCase):
    def setUp(self):
        Discount.objects.create(brand_name="TEST_BRAND",
                                discount_percentage=10,
                                number_of_codes=50,
                                enabled=1,
                                valid_from=datetime.datetime(2022, 4, 11, 7, 29, 33, tzinfo=datetime.timezone.utc),
                                valid_to=datetime.datetime(2023, 4, 11, 7, 29, 33, tzinfo=datetime.timezone.utc)
                                )

    def test_discount_model(self):
        discount = Discount.objects.get(brand_name="TEST_BRAND")
        self.assertEqual(discount.brand_name, "TEST_BRAND")
        self.assertEqual(discount.discount_percentage, 10)
        self.assertEqual(discount.number_of_codes, 50)
        self.assertEqual(discount.enabled, 1)
        self.assertEqual(discount.valid_from, datetime.datetime(2022, 4, 11, 7, 29, 33, tzinfo=datetime.timezone.utc))
        self.assertEqual(discount.valid_to, datetime.datetime(2023, 4, 11, 7, 29, 33, tzinfo=datetime.timezone.utc))

    def test_update_discount_model(self):
        discount = Discount.objects.get(brand_name="TEST_BRAND")
        discount.enabled = 0
        discount.save()
        self.assertEqual(discount.enabled, 0)
