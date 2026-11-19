# Funding Atlas
Django + SQLite funding directory. Plain CSS, no Tailwind. All 386 funding records are included, with keyword search, five filters, pagination, complete record details, provider links and Django admin.

## Run locally
    python -m pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver 127.0.0.1:8000

Open http://127.0.0.1:8000/. The included database is populated. To rebuild a new database, run python manage.py loaddata funding after migrate. Optional admin account: python manage.py createsuperuser.

## Data
Original workbook: data/FUndingDB.xlsx. All rows are retained. Known encoding corruption repaired in 20 cells. The lost character in O308 was restored as an apostrophe from context. No funding availability or website validation has been performed. Blank source cells display as not specified. Filters use complete source categories; combined instruments and applicant groups remain combined source values.

## Deployment
Defaults are for local development. For production set DJANGO_DEBUG=0, DJANGO_SECRET_KEY and DJANGO_ALLOWED_HOSTS (comma-separated), configure static file serving and use a production WSGI/ASGI server. No public deployment is included.
