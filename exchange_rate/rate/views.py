from datetime import timedelta
from django.http import JsonResponse
import requests
from .models import ExchangeRate
from django.utils import timezone
from xml.etree import ElementTree as ET



def get_cbr_currency(currency_code='USD'):
    current_datetime = timezone.now()
    date_for_url = current_datetime.strftime('%d/%m/%Y')
    last_date = ExchangeRate.objects.first()

    if last_date:
        if timezone.is_naive(last_date.timestamp):
            last_date_tz = timezone.make_aware(last_date.timestamp)
        else:
            last_date_tz = last_date.timestamp
            
        time_diff = current_datetime - last_date_tz
        if time_diff <= timedelta(seconds=10):
            return get_json()
        
    url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={date_for_url}'
    
    response = requests.get(url)
    response.raise_for_status()

    root = ET.fromstring(response.content)
    
    for valute in root.findall('Valute'):
        if valute.find('CharCode').text == currency_code:
            to_db(currency_code, valute.find('Value').text.replace(',', '.'), current_datetime)
            return get_json()
    
    raise ValueError(f'Валюта {currency_code} не найдена')


def cbr_currency(request, currency_code):
    data_currency =get_cbr_currency(currency_code)
    return data_currency


def get_json():
    db_rate=ExchangeRate.objects.all()
    data = [
        {
            "currency": solo_rate.currency_code,
            "value": float(solo_rate.rate),
            "timestamp": solo_rate.timestamp.isoformat()
        }
        for solo_rate in db_rate
    ]    
    return JsonResponse({"data": data})


def to_db(currency_code, rate, timestamp):
    ExchangeRate.objects.create(currency_code=currency_code, rate=rate, timestamp=timestamp)
