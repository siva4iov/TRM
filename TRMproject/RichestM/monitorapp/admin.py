from django.contrib import admin
from .models import Citizenship, Industry, Photos, Person


class PhotosAdmin(admin.ModelAdmin):
    list_display = ('persons',)


class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', 'fortune')


class CitizenshipAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)


class IndustryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Photos, PhotosAdmin)
admin.site.register(Industry, IndustryAdmin)
admin.site.register(Citizenship, CitizenshipAdmin)