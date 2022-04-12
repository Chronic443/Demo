from django.test import TestCase
import datetime

from .models import Discount, DiscountCode


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


class TestViews(TestCase):
    def setUp(self):
        d = Discount.objects.create(brand_name="TEST_BRAND",
                                    discount_percentage=10,
                                    number_of_codes=50,
                                    enabled=1,
                                    valid_from=datetime.datetime(2022, 4, 11, 7, 29, 33, tzinfo=datetime.timezone.utc),
                                    valid_to=datetime.datetime(2023, 4, 11, 7, 29, 33, tzinfo=datetime.timezone.utc)
                                    )
        DiscountCode.objects.create(user_id="68150717-4604-4603-906d-bbb325e25902",
                                    enabled=1,
                                    discount=d)

    def test_get_discount(self):
        response = self.client.get('/discounts/get_discount/TEST_BRAND/68150717-4604-4603-906d-bbb325e25902/')
        self.assertEqual(response.status_code, 200)

    def test_get_discount_404(self):
        response = self.client.get('/discounts/get_discount/TEST_BRAND_2/68150717-4604-4603-906d-bbb325e25902/')
        self.assertEqual(response.status_code, 404)
