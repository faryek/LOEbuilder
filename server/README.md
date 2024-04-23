Для установки модулей
`pip install -r requirements.txt`

для запуска сервера
`py -m uvicorn main:app --reload`

для создания таблиц и посева
`py seed.py`

файлы
database.py - подключение к БД
models.py - таблицы со связями
seed.py - посев
pyd - pydantic модели для валидации