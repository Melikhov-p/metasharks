### pip list  
asgiref             3.5.2   
certifi             2022.9.24   
charset-normalizer  2.1.1   
coreapi             2.3.3   
coreschema          0.0.4   
Django              4.1.2   
django-rest-swagger 2.2.0   
djangorestframework 3.14.0   
idna                3.4   
itypes              1.2.0   
Jinja2              3.1.2   
MarkupSafe          2.1.1   
openapi-codec       1.3.2   
pip                 21.1.2   
psycopg2            2.9.4   
pytz                2022.4   
requests            2.28.1   
setuptools          57.0.0   
simplejson          3.17.6   
sqlparse            0.4.3   
tzdata              2022.4   
uritemplate         4.1.1   
urllib3             1.26.12   
wheel               0.36.2   
---------------------------
БД на PostgreSQL, backup БД в репозитории, данные для подключения в settings.py
---------------------------
### Описание API (Адрес - пояснение - доступные методы):     
http://127.0.0.1:8000/api/ - Swagger с API   
http://127.0.0.1:8000/api/get_all/{subject} - получить все {subject} (варианты: Цвета/Марки/Модели/Заказы | Пример: http://127.0.0.1:8000/api/get_all/colors) - [GET]   
http://127.0.0.1:8000/api/post_in/{subject} - создать новый {subject} (варианты: Цвет/Марку/Модель/Заказ | Пример: http://127.0.0.1:8000/api/post_in/brands) - [POST]   
http://127.0.0.1:8000/api/{subject}/{id} - Получить/Обновить/Удалить {subject} с ID {id} (Пример: http://127.0.0.1:8000/api/order/1) - ['GET', 'PATCH', 'DELETE']   
http://127.0.0.1:8000/api/get_orders_by_{subject} - Получить количество заказов по цвету/марке (Пример: http://127.0.0.1:8000/api/get_orders_by_brand) - ['GET']   
--------------------------
### Постраничный вывод таблицы заказов с возможностью фильтрации по марке    
http://127.0.0.1:8000/orders - Пагинация по 10 записей на страницу, для фильтрации по марке нажать на название марки   
--------------------------
### Скрины  
![image](https://user-images.githubusercontent.com/72454035/195590008-b2d6c092-2691-4a03-8ac2-e53a98e54a75.png)   
![image](https://user-images.githubusercontent.com/72454035/195590078-ed2018a9-7b3b-4feb-aea8-0e429223a0b7.png)   
