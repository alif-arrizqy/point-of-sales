
## Installation

### Install packages with pip

```bash
  pip install -r requirements.txt
```

#### Api Gateway Service

change directory to api_gateway/

```bash
    cd api_gateway
```

copy .env.example to .env
```bash
    cp .env.example .env
```

running command

```bash
    python manage.py runserver
```

#### User Service

change directory to user_app/

```bash
    cd user_app
```

migration database

```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
```

running command

```bash
    python manage.py runserver
```

#### Item Service

change directory to item_app/

```bash
    cd item_app
```

migration database

```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
```

running command

```bash
    python manage.py runserver
```

#### Transaction Service

change directory to transaction_app/

```bash
    cd transaction_app
```

migration database

```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
```

running command

```bash
    python manage.py runserver
```
