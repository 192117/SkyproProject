from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from resumes.mixins import TimeStampedMixin


class Resume(TimeStampedMixin):
    class Status(models.TextChoices):
        active = 'active', 'Опубликовано'
        in_active = 'in_active', 'Скрыто'

    class Grade(models.TextChoices):
        intern = 'intern', 'Intern'
        junior = 'junior', 'Junior'
        middle = 'middle', 'Middle'
        senior = 'senior', 'Senior'

    class Education(models.TextChoices):
        school = 'school', 'Среднее общее'
        college = 'college', 'Среднее специальное'
        incomplete_higher = 'incomplete_higher', 'Неоконченное высшее'
        higher = 'higher', 'Высшее'

    class Specialty(models.TextChoices):
        full_stack = 'full_stack', 'Фулл-стек'
        frontend = 'frontend', 'Фронтенд'
        backend = 'backend', 'Бэкенд'
        gamedev = 'gamedev', 'Геймдев'
        devops = 'devops', 'Девопс'
        design = 'design', 'Дизайн'
        products = 'products', 'Продукты'
        management = 'management', 'Менеджмент'
        testing = 'testing', 'Тестирование'

    status = models.CharField(
        verbose_name='Статус резюме',
        max_length=12,
        choices=Status.choices,
        default=Status.in_active,
    )
    grade = models.CharField(
        verbose_name='Уровень',
        max_length=6,
        choices=Grade.choices,
        default=Grade.intern,
    )
    specialty = models.CharField(
        verbose_name='Специализация',
        max_length=10,
        choices=Specialty.choices,
        default=Specialty.full_stack,
    )
    education = models.CharField(
        verbose_name='Образование',
        max_length=18,
        choices=Education.choices,
        default=Education.school,
    )
    experience = models.TextField(
        verbose_name='Опыт работы',
    )
    portfolio = models.URLField(
        verbose_name='Ссылка на портфолио GitHub',
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название резюме',
    )
    phone = PhoneNumberField(
        verbose_name='Номер для связи',
    )
    email = models.EmailField(
        verbose_name='Email для связи',
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Владелец резюме',
    )

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
        ordering = ['-modified']

    def __str__(self):
        return f'{self.title}-{self.grade}'
