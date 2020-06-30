<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-passwordless-user.svg?maxAge=3600)](https://pypi.org/project/django-passwordless-user/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-passwordless-user.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-passwordless-user.py/actions)

### Installation
```bash
$ [sudo] pip install django-passwordless-user
```

#### Pros
+   3rd party/social authentication without password

#### Examples
`settings.py`
```python
AUTH_USER_MODEL = 'users.User'
```

`users/modes.py`
```python
from django.db import models
from django_passwordless_user.models import AbstractBaseUser

class Token(models.Model):
    token = models.TextField()

class User(AbstractBaseUser):
    login = models.TextField(unique=True)

    USERNAME_FIELD = 'login'

    class Meta:
        db_table = 'users_user'

    def get_salted_hmac_value(self):
        token = Token.objects.get(pk=self.pk)
        return token
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>