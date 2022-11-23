# Generated by Django 4.1 on 2022-08-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remont', '0004_callbackform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial', models.CharField(blank=True, max_length=1500, verbose_name='Отзыв')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Имя, фамилия')),
            ],
            options={
                'verbose_name': '   Отзыв',
                'verbose_name_plural': '   Отзывы',
            },
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': '     Об услуге', 'verbose_name_plural': '     Об услугах'},
        ),
        migrations.AlterModelOptions(
            name='advblock',
            options={'verbose_name': '    Рекламный блок', 'verbose_name_plural': '    Рекламные блоки'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': '  Контактные данные', 'verbose_name_plural': '  Контактные данные'},
        ),
        migrations.AlterModelOptions(
            name='contactform',
            options={'verbose_name': ' Сообщение, заказ', 'verbose_name_plural': ' Сообщения, заказы'},
        ),
        migrations.AlterModelOptions(
            name='head',
            options={'verbose_name': '      Верхняя часть с фото', 'verbose_name_plural': '      Верхняя часть с фото'},
        ),
        migrations.AlterModelOptions(
            name='serviceitem',
            options={'verbose_name': '   Вид техники', 'verbose_name_plural': '   Виды техники'},
        ),
    ]