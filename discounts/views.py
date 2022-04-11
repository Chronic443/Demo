import datetime

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from discounts.models import DiscountCode, Discount
from discounts.serializers import DiscountSerializer


@api_view(['GET'])
def validate_token(request, brand_name, user_id):
    pass


@api_view(['GET'])
def disable_code(request, brand_name, user_id):
    pass


@api_view(['GET'])
def get_discount(request, brand_name, user_id):
    if isinstance(brand_name, str) and isinstance(user_id, str):
        discount = Discount.objects.get(brand_name=brand_name, enabled=1)
        if discount:
            if discount.valid_from >= datetime.datetime.now() > discount.valid_to:
                if (dc := DiscountCode.objects.filter(user_id=user_id, enabled=1).first()) is not None:
                    return JsonResponse({"CODE": dc.code}, status=200)

                discount_codes = DiscountCode.objects.filter(discount=discount, user_id=None).first()
                if discount_codes is not None:
                    discount_codes.user_id = user_id
                    discount_codes.save()
                    return JsonResponse({"CODE": discount_codes.code}, status=200)
                else:
                    return Response('All discount codes spent', status=404)
            else:
                return Response('No available tokens', status=404)
        else:
            return Response(f'No codes from {brand_name}', status=404)
    else:
        return Response("Bad Request", status=400)


@api_view(['PUT'])
def update_discount(request):
    if 'brand_name' in request.data and isinstance(request.data['brand_name'], str):
        discount = Discount.objects.get(brand_name=request.data['brand_name'])
        if discount:
            serializer = DiscountSerializer(discount, data=request.data)
            if serializer.is_valid():
                serializer.save()
                if 'number_of_codes' in request.data:
                    for i in range(0, int(request.data['number_of_codes'])):
                        DiscountCode.objects.create(discount=discount)

                return JsonResponse(serializer.data)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return Response(f'No brand name {request.data["brand_name"]}', status=404)
    else:
        return Response(status=400)


@api_view(['POST'])
def generate_discount_tokens(request):
    serializer = DiscountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        discount = Discount.objects.get(brand_name=request.data['brand_name'])
        for i in range(0, int(request.data['number_of_codes'])):
            DiscountCode.objects.create(discount=discount)

        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
