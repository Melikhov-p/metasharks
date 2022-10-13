from django.urls import path, include
from sharks_api.views import *
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='METASHARKS API')

urlpatterns = [
    path('', schema_view),
    path('get_all/<str:subject>', get_all, name='api_get_all'),
    path('post_in/<str:subject>', post_in, name='api_post_in'),
    path('color/<int:color_id>/', color, name='api_color'),
    path('brand/<int:brand_id>', brand, name='api_brand'),
    path('model/<int:model_id>', model, name='api_model'),
    path('get_orders_by_<str:subject>', get_orders_by, name='api_get_orders_by')
]
