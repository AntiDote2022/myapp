from django.db import models


class Texts(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    f_text = models.TextField('Статья')
    date = models.DateTimeField('Дата и время')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Comments(models.Model):
    numbers = models.ForeignKey(Texts, verbose_name='ид новости', on_delete=models.CASCADE, blank=True, null=True, related_name='comments_texts' )
    kom_name = models.CharField('Имя комментатора', max_length=20, blank=False)
    kom_text = models.TextField('Текст комментария', null=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{}".format(self.numbers)
