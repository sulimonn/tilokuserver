from django.db import models
from django.utils.text import slugify


class Group(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class GroupItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    url = models.CharField(max_length=255, null=True, blank=True)
    book = models.FileField(upload_to='books/')
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Элемент группы'
        verbose_name_plural = 'Элементы группы'

    def save(self, *args, **kwargs):
        self.url = '/' + self.group.url + '/' + str(self.id)
        super().save(*args, **kwargs)


class Chapter(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    parent = models.ForeignKey(GroupItem, on_delete=models.CASCADE)
    url = models.CharField(max_length=255, null=True, blank=True)
    page = models.IntegerField()

    def __str__(self):
        return self.parent.title + ' | ' + self.title

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.url = self.parent.url + '/' + str(self.pk)
        super().save(*args, **kwargs)


class Subchapter(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    parent = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    url = models.CharField(max_length=255, null=True, blank=True)
    page = models.IntegerField()
    video = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подглава'
        verbose_name_plural = 'Подглавы'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.url = self.parent.url + '/' + str(self.pk)
        super().save(*args, **kwargs)


class Exercise(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    sub_chapter = models.ForeignKey(Subchapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'


class Exercise1(Exercise):
    answer = models.CharField(max_length=255)