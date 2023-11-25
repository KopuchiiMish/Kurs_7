from django.db import models
from config import settings
import django as django
import datetime


# Модель для представления привычки
class Habit(models.Model):
    objects = None

    # Класс выбора для частоты выполнения привычки
    class HabitFrequency(models.TextChoices):
        Daily = 'DAILY'
        monday = 'MONDAY'
        tuesday = 'TUESDAY'
        wednesday = 'WEDNESDAY'
        thursday = 'THURSDAY'
        friday = 'FRIDAY'
        saturday = 'SATURDAY'
        sunday = 'SUNDAY'

    # Поле для связи с владельцем привычки (пользователем)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name="Владелец привычки")

    # Поле для указания места, связанного с привычкой
    place = models.CharField(max_length=100, null=False, blank=False, verbose_name="Место для привычки")

    # Поле для указания времени начала выполнения привычки
    time = models.TimeField(default=datetime.datetime.now().time, verbose_name="Время начала привычки")

    # Поле для описания действия, связанного с привычкой
    action = models.CharField(max_length=100, null=False, blank=False, verbose_name="Действие привычки")

    # Поле для указания, приятная ли привычка
    is_pleasant = models.BooleanField(default=False, verbose_name="Приятная привычка")

    # Поле для связи с приятной привычкой (если есть)
    link_pleasant = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True,
                                      verbose_name='Ссылка на приятную привычку')

    # Поле для указания частоты выполнения привычки
    frequency = models.CharField(choices=HabitFrequency.choices, default=HabitFrequency.Daily,
                                 verbose_name="Частота выполнения")

    # Поле для указания награды за выполнение привычки
    award = models.CharField(max_length=100, null=True, blank=True, verbose_name="Награда за привычку")

    # Поле для указания продолжительности привычки
    duration = models.IntegerField(null=False, blank=False, verbose_name="Продолжительность привычки")

    # Поле для указания, публичная ли привычка
    is_public = models.BooleanField(default=True, verbose_name="Публичная привычка")

    # Метод для представления модели в виде строки
    def __str__(self):
        return f"ДЕЙСТВИЕ: {self.action} МЕСТО: {self.place}"

    # Метаданные модели
    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = 'привычки'
