from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from workout_21 import settings


# Create your models here.
# class workout_images(models.Model):
#     title =models.CharField(max_length=100)
#     cover = models.ImageField(upload_to='images/')
#     workout_images = models.FileField


class training(models.Model):
    objects = True
    name = models.CharField(max_length=250, db_index=True, unique=True, verbose_name='Заголовок')
    content = models.CharField(max_length=500, verbose_name= 'Основной контент')
    free = models.IntegerField(verbose_name='Доступ')
    slug = models.SlugField(max_length=250,unique=True, db_index=True,verbose_name= "Отображение url" )
    main_description = models.CharField(blank=True,default='',db_index=True, null=True,verbose_name= "Индивидуальный основной контент",max_length=500 )
    description1= models.CharField(blank=True,default='',db_index=True, null=True,verbose_name= "Поле параграфа 1",max_length=500)
    description2 = models.CharField(blank=True,default='',db_index=True, null=True,verbose_name= "Поле параграфа 2",max_length=500)
    class Meta:
        verbose_name = 'Программы тренировок'
        verbose_name_plural = 'Программы тренировок'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.slug


class data_people(models.Model):
    objects = None
    name = models.CharField(max_length=250, verbose_name='Имя')
    surname = models.CharField(max_length=250, verbose_name='Фамилия')
    logins = models.CharField(max_length=250, verbose_name='Логин')
    passwords = models.CharField(max_length=250, verbose_name='Пароль')
    gender = models.SlugField(max_length=250, verbose_name='Пароль')
    def __str__(self):
        return self.name

class Reviews(models.Model):
    objects = None
    name = models.CharField(max_length=250,verbose_name='Имя отправителя',default='user')
    reviews = models.CharField(max_length=250, null=False, verbose_name='Отзыв')
    class Meta:
        verbose_name = 'Отзывы участников'
        verbose_name_plural = 'Отзывы участников'
    def __str__(self):
        return self.name



# Create your models here.
# class AddUsers(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='add', )
#     photos = models.CharField(max_length=255, null=True,verbose_name='photo')
#     data_birth = models.CharField(max_length=255, verbose_name='birth')
#     def __str__(self):
#         return self.user
#return reverse('programs', kwargs={'slug_id':self.slug})
#from Chuvash_Workout.models import programs
#python manage.py makemigrations
#python manage.py migrate
class MyUsers(models.Model):
    objects = None
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='add')
    photo = models.ImageField(verbose_name='Фотография', upload_to='photos/%Y/%m/%d',default=None,)
    date_bitrh = models.DateTimeField(verbose_name='Дата рождения')
    class Meta:
        verbose_name = 'Доп данные для User'
        verbose_name_plural = 'Доп данные для User'


def content_file_name(instance, filename):
    return '/'.join(['photos/%Y/%m/%d', instance.user.username, filename])