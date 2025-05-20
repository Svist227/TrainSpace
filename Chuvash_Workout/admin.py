from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import training, MyUsers, Reviews


# Register your models here.


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "slug", 'free', 'brienf_info')
    list_display_links = ('id', 'name')
    ordering = ['name', 'slug']
    list_editable = ['slug']
    list_per_page = 5
    actions = ['action']
    @admin.display(description="Описание")
    def brienf_info(self, train: training):
        return f'Контент содержит {len(train.content)} символов'
    @admin.action(description="Обновить поле доступа")
    def action(self,request, queryet): # request -обьект запроса, queryset - объект записи
        queryet.update(free = '0')

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name','reviews')
    list_display_links = [ 'name']
    list_editable = ['reviews']
    list_per_page = 7
class MyUsersAdmin(admin.ModelAdmin):
    list_display = ('user','photo','date_bitrh')
    list_display_links = ['user']
    list_editable = ['photo','date_bitrh']
    list_per_page = 5
    actions = ['action']
admin.site.register(training, WorkoutAdmin)
admin.site.register(MyUsers, MyUsersAdmin)
admin.site.register(Reviews, ReviewsAdmin)