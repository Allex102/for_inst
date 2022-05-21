from django.db import models

class Collection(models.Model):
    autor_name = models.CharField(max_length=255, verbose_name='Имя автора', blank=True,)
    book_name = models.CharField(max_length=255, verbose_name='Название книги', blank=True)
    year = models.DateField(verbose_name='Год выпуска',blank=True)
    code = models.PositiveBigIntegerField(blank=True,verbose_name='Код книги')

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class Stellaj(models.Model):
    name = models.CharField(blank=True,max_length=20, verbose_name='Название полки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Полка'
        verbose_name_plural = 'Полки'

class Collection_stellaj(models.Model):
    book_id = models.ForeignKey(to=Collection, verbose_name='Книга', blank=True, on_delete=models.CASCADE)
    stellaj_id = models.ForeignKey(to=Stellaj, verbose_name='Полка', blank=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Книга_полки'
        verbose_name_plural = 'Книга_полки'

