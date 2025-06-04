from django.db import models


class ExchangeRate(models.Model):
    currency_code = models.CharField(verbose_name="Код валюты")
    rate = models.FloatField(verbose_name="Курс валюты к RUB")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата запроса")

    class Meta:
        ordering = ['-timestamp']
    #     verbose_name = "Курс валюты"
    #     verbose_name_plural = "Курсы валют"

    # def __str__(self):
    #     return f"1 USD = {self.usd_rate} RUB ({self.timestamp})"
    
    def save(self, *args, **kwargs):
        MAX_ENTRIES = 11  # Максимальное количество записей
        
        # Удаляем самую старую запись, если достигнут лимит
        if ExchangeRate.objects.count() >= MAX_ENTRIES:
            oldest_entry = ExchangeRate.objects.last()
            oldest_entry.delete()
        
        super().save(*args, **kwargs)
