from django.db import models


class Voting(models.Model):
    title = models.CharField("Название", max_length=50)
    created_at = models.DateTimeField("Дата начала голосования", auto_now_add=True)
    finish_at = models.DateTimeField("Дата окончания голосования")
    max_voice = models.IntegerField("Максимальное кол-во голосов")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'voting_table'
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'


class Character(models.Model):
    surname = models.CharField("Фамилия", max_length=50)
    name = models.CharField("Имя", max_length=50)
    patronymic = models.CharField("Отчество", max_length=50)
    photo = models.ImageField("Фотография персонажа", upload_to='images/')
    age = models.IntegerField("Возраст персонажа")
    brief_biography = models.TextField("Краткая биография", max_length=500)
    voting = models.ForeignKey(
        Voting,
        on_delete=models.CASCADE,
        verbose_name="Голосование",
        related_name='characters'
    )

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    class Meta:
        db_table = 'voting'
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'
