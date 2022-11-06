from django.contrib import admin

from .models import News, Category, DataBase1,Tnved_Type

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class BaseDataAdmin(admin.ModelAdmin):
    list_display = ( 'napr', 'product_code', 'product_type', 'month', 'year', 'id_country','country','edizm','edizm_name','price','weight','count','region','federal_district')
    list_display_links = ('price',)

class Tnved_TypeAdmin(admin.ModelAdmin):
    list_display = ( 'key', 'value')
    list_display_links = ('key',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(DataBase1, BaseDataAdmin)
admin.site.register(Tnved_Type, Tnved_TypeAdmin)


