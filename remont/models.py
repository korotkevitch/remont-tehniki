from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber

# Create your models here.
class Head(models.Model):
    title = models.CharField('Title страницы', max_length=120, blank=True)
    title_with_image = models.CharField('Заголовок рядом с фото', max_length=90, blank=True)
    subtitle_with_image = models.CharField('Подзаголовок рядом с фото', max_length=120, blank=True)
    logo = models.FileField('Лого', blank=True,)
    image = models.FileField('Главное фото', blank=True)
    job_time = models.CharField('Время работы', max_length=50, blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото'

    def logo_preview(self):
        if self.logo:
            return mark_safe('<img src="%s" style="width:100px; height:30px;" />' % self.logo.url)
        else:
            return 'No Image Found'

    logo_preview.short_description = 'Логотип'

    class Meta:
        verbose_name = '      Верхняя часть с фото'
        verbose_name_plural = '      Верхняя часть с фото'

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField('Заголовок', max_length=100, blank=True)
    text = models.CharField('Текст', max_length=800, blank=True)

    class Meta:
        verbose_name = '     Об услуге'
        verbose_name_plural = '     Об услугах'

    def __str__(self):
        return self.title


class AdvBlock(models.Model):
    icon = models.FileField('Иконка', blank=True, default='')
    title = models.CharField('О чем блок (для себя)', max_length=20, blank=True)
    text = models.CharField('Текст', max_length=60, blank=True)

    def icon_preview(self):
        if self.icon:
            return mark_safe('<img src="%s" style="width:60px; height:60px;" />' % self.icon.url)
        else:
            return 'Нет изображения'

    icon_preview.short_description = 'Картинка'

    class Meta:
        verbose_name = '    Рекламный блок'
        verbose_name_plural = '    Рекламные блоки'

    def __str__(self):
        return self.title


class ServiceItem(models.Model):
    title = models.CharField('Что ремонтируем? (для себя)', max_length=50, blank=True)
    text_before = models.CharField('Текст до перечня поломок', max_length=100, blank=True)
    text_after = models.CharField('Текст после перечня поломок', max_length=100, blank=True)
    issue_1 = models.CharField('Описание проблемы', max_length=2000, blank=True)
    issue_2 = models.CharField('Описание проблемы', max_length=2000, blank=True)
    issue_3 = models.CharField('Описание проблемы', max_length=2000, blank=True)
    issue_4 = models.CharField('Описание проблемы', max_length=2000, blank=True)
    issue_5 = models.CharField('Описание проблемы', max_length=2000, blank=True)
    issue_6 = models.CharField('Описание проблемы', max_length=2000, blank=True)
    issue_7 = models.CharField('Описание проблемы', max_length=2000, blank=True)
    issue_8 = models.CharField('Описание проблемы', max_length=2000, blank=True)
    issue_9 = models.CharField('Описание проблемы', max_length=2000, blank=True)
    issue_10 = models.CharField('Описание проблемы', max_length=2000, blank=True)
    image = models.FileField('Фото', blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:80px; height:70px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото 548*460'

    class Meta:
        verbose_name = '   Вид техники'
        verbose_name_plural = '   Виды техники'

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    testimonial = models.CharField('Отзыв', max_length=1500, blank=True)
    name = models.CharField('Имя, фамилия', max_length=50, blank=True)

    class Meta:
        verbose_name = '   Отзыв'
        verbose_name_plural = '   Отзывы'


class Contact(models.Model):
    phone = models.CharField('Телефон', max_length=50, blank=True)
    email = models.EmailField('Email', max_length=50, blank=True)

    def phone_link(self):
        return PhoneNumber.from_string(phone_number=self.phone, region='RU').as_e164

    phone_link.short_description = 'Телефон для ссылки'

    class Meta:
        verbose_name = '  Контактные данные'
        verbose_name_plural = '  Контактные данные'

    def __str__(self):
        return "Телефоны"


class ContactForm(models.Model):
    name = models.CharField('Имя', max_length=50, blank=True)
    phone = models.CharField('Телефон', max_length=50, blank=True)
    message = models.TextField('Сообщение', max_length=500, blank=True)

    class Meta:
        verbose_name = ' Сообщение, заказ'
        verbose_name_plural = ' Сообщения, заказы'

    def __str__(self):
        return self.name


class CallBackForm(models.Model):
    phone = models.CharField('Телефон', max_length=50, blank=True)

    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Обратные звонки'

    def __str__(self):
        return self.phone