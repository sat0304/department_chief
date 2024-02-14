# department_chief
This project provides to view internal relations of eployees in IT department of well known company.

### Описание
```
Дана БД, имеющая две таблицы: сотрудники и подразделение.
Необходимо написать 4 запроса.
3апросы, которые выведут:
1. Сотрудника с максимальной заработной платой.
2. Вывести одно число: максимальную длину цепочки руководителей по таблице
сотрудников (вычислить глубину дерева).
3. Отдел, с максимальной суммарной зарплатой сотрудников.
4. Сотрудника, чье имя начинается на «Р» и заканчивается на «н».
```
### Технологии
```
Django==5.0.2
django-rest-framework==0.1.0
djangorestframework==3.14.0
pytz==2024.1
sqlparse==0.4.4

```
### Запуск проекта в dev-режиме
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/sat0304/department_chief

cd department_chief
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```
cd backend
python3 manage.py migrate
```
Запустить проект.

В папке с файлом manage.py выполните команду:
```
python manage.py runserver
```
Перейти по адресу:
http://127.0.0.1:8000/

Ответы на задание 1 доступны по адресу:
```
1. http://127.0.0.1:8000/employees/get_max_salary/
2. http://127.0.0.1:8000/employees/get_tree_deep/
3. http://127.0.0.1:8000/employees/get_income_department/
4. http://127.0.0.1:8000/employees/get_name_starts_P/
```
В папке department/sql_requests
содержится текстовой файл SQL запросов:
```
sql_requests.txt
```
### Автор
С.А.Токарев
