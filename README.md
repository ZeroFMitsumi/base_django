# Base de project Django

### ***Credit*** :
- Video Tutorial du project d'origine par [Andreas Jud](https://github.com/andyjud) :
    > https://youtu.be/SQ4A7Q6_md8

## ***Description*** :

- Base de project Django prêt à utiliser
- Remplacement de `send_email_confirmation()` par 
```python
    from allauth.account.models import EmailAddress

    from allauth.account.internal.flows.email_verification import (
        send_verification_email_to_address,
    )

    ...

    email_address = EmailAddress.objects.get_primary(request.user)
    send_verification_email_to_address(request, email_address)
```

## ***Installation*** :
Pensez a créer un dossier `media` a la racine du project pour les images d'avatars et autres fichiers medias

Create Virtual Environment
### ArchLinux

``` python
    sudo pacman -S python-virtualenv

    # Dans le dossier du project
    virtualenv [nom_du_virtualenv]

    source venv/bin/activate
```
### Mac/Linux

``` python
    python3 -m venv venv
    source venv/bin/activate
```

### Windows

``` python
python3 -m venv venv
```
``` powershell
(Powershell:) .\venv\Scripts\Activate.ps1
```

``` bash
(or Command Prompt:) venv\Scripts\activate 
(or Git Bash:) source venv/Scripts/activate
```
### ***Dépandances*** :

- `pip install --upgrade pip`

- `pip install -r requirements.txt`

## ***Usage*** :

- `python manage.py migrate`  pour migrer la base de données

- `python manage.py createsuperuser`  pour créer un super utilisateur

***Lancer l'application*** :

> - `python manage.py runserver`  pour lancer le serveur

> - `python manage.py runserver --insecure`  pour lancer le serveur sans https

> - `python manage.py runserver 0.0.0.0:8000`  pour lancer le serveur sur l'adresse 0.0.0.0:8000

> - `python manage.py runserver 0.0.0.0:8000 --insecure`  pour lancer le serveur sur l'adresse 0.0.0.0:8000 sans https

> - `python manage.py runserver 0.0.0.0:8000 --insecure --noreload`  pour lancer le serveur sur l'adresse 0.0.0.0:8000 sans https et sans reload

> - `python manage.py runserver 0.0.0.0:8000 --insecure --noreload --nothreading`  pour lancer le serveur sur l'adresse 0.0.0.0:8000 sans https, sans reload et sans threading

## ***pour la mise en production*** :

- `python manage.py collectstatic`  pour collecter les fichiers statiques

- `python manage.py compress`  pour compresser les fichiers statiques

- `python manage.py migrate`  pour migrer la base de données

- Generate Secret Key ( ! Important for deployment ! )

``` python
    python manage.py shell

    from django.core.management.utils import get_random_secret_key
    
    print(get_random_secret_key())
    
    exit()
```

## ***Documentation*** :

- [Django](https://www.djangoproject.com/)

- [Django REST Framework](https://www.django-rest-framework.org/)

- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)

- [Django Browser Reload](https://django-browser-reload.readthedocs.io/en/latest/)

- [Django HTMX](https://django-htmx.readthedocs.io/en/latest/)

- [Pillow](https://pillow.readthedocs.io/en/stable/)

- [Markdown](https://python-markdown.github.io/markdown/)

