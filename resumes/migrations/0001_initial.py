# Generated by Django 4.2.3 on 2023-07-19 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Опубликовано'), ('in_active', 'Скрыто')], default='in_active', max_length=12, verbose_name='Статус резюме')),
                ('grade', models.CharField(choices=[('intern', 'Intern'), ('junior', 'Junior'), ('middle', 'Middle'), ('senior', 'Senior')], default='intern', max_length=6, verbose_name='Уровень')),
                ('specialty', models.CharField(choices=[('full_stack', 'Фулл-стек'), ('frontend', 'Фронтенд'), ('backend', 'Бэкенд'), ('gamedev', 'Геймдев'), ('devops', 'Девопс'), ('design', 'Дизайн'), ('products', 'Продукты'), ('management', 'Менеджмент'), ('testing', 'Тестирование')], default='full_stack', max_length=10, verbose_name='Специализация')),
                ('education', models.CharField(choices=[('school', 'Среднее общее'), ('college', 'Среднее специальное'), ('incomplete_higher', 'Неоконченное высшее'), ('higher', 'Высшее')], default='school', max_length=18, verbose_name='Образование')),
                ('experience', models.TextField(verbose_name='Опыт работы')),
                ('portfolio', models.URLField(verbose_name='Ссылка на портфолио GitHub')),
                ('title', models.CharField(max_length=100, verbose_name='Название резюме')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер для связи')),
                ('email', models.EmailField(max_length=254, verbose_name='Email для связи')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец резюме')),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
                'ordering': ['-modified'],
            },
        ),
    ]
