# Django Currency API  

Проект возвращает текущий курс валюты к RUB и историю запросов.  

## Как запустить  
1. Установите зависимости:  
   ```bash
   pip install django requests python-dotenv
   ```  
2. Создайте `.env`-файл:  
   ```bash
   SECRET_KEY=ваш_ключ
   ```  
3. Запустите сервер:  
   ```bash
   python manage.py runserver
   ```  

## API  
- **`/get-current-N/`** – возвращает текущий курс валюты N, где N это любой код валюты) и 10 последних запросов.  