# Generated by Django 4.1 on 2022-08-22 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remont', '0002_alter_about_options_remove_serviceitem_issue_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Телефон')),
                ('message', models.TextField(blank=True, max_length=500, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение, заказ',
                'verbose_name_plural': 'Сообщения, заказы',
            },
        ),
    ]
