This project does **not** require any GIS library or specific database.
Map data is stored in latitude and longitude (decimal) fields.

Install
=======

Install Django dependencies:

    pip install -r requirements.txt

Initialize database tables:

    python manage.py migrate

Create a super-user for the admin:

    python manage.py createsuperuser

Run
===

    python manage.py runserver

Enter http://127.0.0.1:8000/admin/mushrooms/mushroomspot/add/ to add your first item.