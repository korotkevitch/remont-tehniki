from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Head, About, AdvBlock, ServiceItem, Contact, ContactForm, CallBackForm, Testimonial
from .forms import UserForm, UserCallBackForm
from django.core.mail import BadHeaderError
from django.views.generic.edit import FormView
from django.core.mail import send_mail


class HomeView(ListView):
    model = Head
    template_name = 'index.html'
    context_object_name = 'head'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['about'] = About.objects.all()
        context['advblock'] = AdvBlock.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['serviceitems'] = ServiceItem.objects.all()
        context['contact'] = Contact.objects.all()

        return context


class ThanksView(ListView):
    model = Head
    template_name = 'thanks.html'
    context_object_name = 'head'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['contact'] = Contact.objects.all()

        return context


class ContactFormView(FormView):
    model = ContactForm
    form_class = UserForm
    success_url = 'thanks'

    def form_valid(self, myform):
        myform.send_mail()
        myform.save()  # сохранение в БД
        return super().form_valid(myform)


class CallBackFormView(FormView):
    model = CallBackForm
    form_class = UserCallBackForm
    success_url = 'thanks'

    def form_valid(self, myform):
        myform.send_mail()
        myform.save()  # сохранение в БД
        return super().form_valid(myform)