from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import data_people
from django.core.validators import MinLengthValidator,MaxLengthValidator

@deconstructible
class MyValidator():
    ALLOWED_CHARS = 'йцукенгшщзхъфывапролджэячсмитьбю'
    code = 'russian'
    def __init__(self, message = None):
        self.message= message if message else 'У нас только маленькие буквы русского алфавита'
    def __call__(self, value, *args, **kwargs):
        if not (set(value)) <= set(self.ALLOWED_CHARS):
            raise ValidationError(self.message, code=self.code)

