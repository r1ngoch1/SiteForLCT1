from django.db import models

class News(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Наименование')
    content = models.TextField(blank = True, verbose_name = 'Контент')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата публикации')
    updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Обновлено')
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', verbose_name = 'Фото', blank = True)
    is_published = models.BooleanField(default = True, verbose_name = 'Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class DataBase1(models.Model):
    napr = models.CharField(max_length=3, verbose_name='Направление')
    product_code = models.CharField(max_length=10, verbose_name='Товарный код')
    product_type = models.CharField(max_length=400, verbose_name='Тип товара')
    month = models.CharField(max_length=3, verbose_name='Месяц')
    year = models.CharField(max_length=4, verbose_name='Год')
    id_country = models.CharField(max_length=3, verbose_name='Код страны')
    country = models.CharField(max_length=150, verbose_name='Страна')
    edizm = models.CharField(max_length=150, verbose_name='Единицы измерения')
    edizm_name = models.CharField(max_length=150, verbose_name='Единицы измерения по РУ')
    price = models.FloatField(verbose_name='Стоимость')
    weight = models.FloatField(verbose_name='Масса')
    count = models.FloatField(verbose_name='Количество')
    region = models.CharField(max_length=300, verbose_name='Регион')
    federal_district = models.CharField(max_length=300, verbose_name='Фед округ')


    def __str__(self):
        return self.napr

    class Meta:
        verbose_name = 'База данных'
        verbose_name_plural = 'Базы данных'

class Tnved_Type(models.Model):
    key =  models.CharField(max_length=4, verbose_name='Ключ')
    value =  models.CharField(max_length=1000, verbose_name='Значение')

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = 'Ключ'
        verbose_name_plural = 'Ключи'

class tnved_types_rate_grouped1(models.Model):
    type_name = models.TextField(verbose_name='Имя')
    rating =  models.FloatField(verbose_name='Рейтинг')

    def __str__(self):
        return self.type_name
