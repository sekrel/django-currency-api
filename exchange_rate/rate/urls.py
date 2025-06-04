from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.StringUrlСurrency, "slugCurrency")

urlpatterns = [
    path("<slugCurrency:currency_code>/", views.cbr_currency, name = 'home'),

]
