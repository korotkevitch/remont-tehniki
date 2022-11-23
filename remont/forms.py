from django import forms
from django.forms import ModelForm, Textarea
from remont.models import About, ServiceItem
from django.core.mail import send_mail as django_send_mail
from .models import ContactForm, CallBackForm, Testimonial


class AboutForm(ModelForm):

    class Meta:
        model = About
        fields = '__all__'
        widgets = {
            'title': Textarea(attrs={'cols': 80,
                                    'rows': 3}),
            'text': Textarea(attrs={'cols': 80,
                                    'rows': 20})
        }


class TestimonialForm(ModelForm):

    class Meta:
        model = Testimonial
        fields = '__all__'
        widgets = {
            'testimonial': Textarea(attrs={'cols': 80,
                                    'rows': 20})
        }


class UserForm(forms.ModelForm):
    # captcha = ReCaptchaField(
    #     public_key='6LdbmQkeAAAAADPuywAjtXN4u-Pd31SfkXBUAHxm',
    #     private_key='6LdbmQkeAAAAAN2ZnJ3-PPe3VkZzScSbyd3AVjKm',
    # )

    class Meta:
        model = ContactForm
        fields = ['name', 'phone', 'message']

    def send_mail(self):
        return django_send_mail('Заказ на ремонт бытовой техники',
                    str('Имя: ') + self.cleaned_data['name'] + '\n' + str('Телефон: ') + self.cleaned_data['phone'] +
                                '\n' + str('Сообщение: ') + self.cleaned_data['message'],
                    'no-reply@remontehniki.by',
                    ['remontehniki@iko-studio.com'])


class UserCallBackForm(forms.ModelForm):

    class Meta:
        model = CallBackForm
        fields = ['phone']

    def send_mail(self):
        return django_send_mail('Заказ обратного звонка', str('Телефон: ') + self.cleaned_data['phone'],
                    'no-reply@remontehniki.by',
                    ['remontehniki@iko-studio.com'])