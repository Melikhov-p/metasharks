from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from sharks_api.serializers import *
from datetime import datetime


@api_view(['GET'])
def get_all(request, subject):
    if request.method == 'GET':
        if subject == 'colors':
            serializer = ColorSerializer(Color.objects.all(), many=True)
        elif subject == 'brands':
            serializer = BrandSerializer(Brand.objects.all(), many=True)
        elif subject == 'models':
            serializer = ModelSerializer(Model.objects.all(), many=True)
        elif subject == 'orders':
            serializer = OrderSerializer(Order.objects.all(), many=True)
        return Response(serializer.data)


@api_view(['POST'])
def post_in(request, subject):
    if request.method == 'POST':
        if subject == 'colors':
            serializer = ColorSerializer(data=request.data)
        elif subject == 'brands':
            serializer = BrandSerializer(data=request.data)
        elif subject == 'models':
            serializer = ModelSerializer(data=request.data)
        elif subject == 'orders':
            if 'date' not in request.data or request.data['date'] == '':
                request.data['date'] = datetime.now().strftime('%Y-%m-%d')
            serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def color(request, color_id):
    color = Color.objects.get(pk=color_id)
    if request.method == 'GET':
        serializer = ColorSerializer(color)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = ColorSerializer(color, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        color = Color.objects.get(pk=color_id)
        color.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH', 'DELETE'])
def brand(request, brand_id):
    brand = Brand.objects.get(pk=brand_id)
    if request.method == 'GET':
        serializer = BrandSerializer(brand)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = BrandSerializer(brand, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        brand = Brand.objects.get(pk=brand_id)
        brand.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH', 'DELETE'])
def model(request, model_id):
    model = Model.objects.get(pk=model_id)
    if request.method == 'GET':
        serializer = ModelSerializer(model)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = ModelSerializer(model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        model = Model.objects.get(pk=model_id)
        model.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def get_orders_by(request, subject):
    if subject == 'color':
        orders = Order.objects.values('color_id').annotate(Sum('color_id'))
        return Response(data=orders)
    elif subject == 'brand':
        brands = Order.objects.values('brand_id').annotate(Sum('brand_id'))
        return Response(data=brands)
