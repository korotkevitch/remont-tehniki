from django.contrib import admin

# Register your models here.
from remont.models import Head, About, AdvBlock, ServiceItem, Contact, ContactForm, CallBackForm, Testimonial

class HeadAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_with_image', 'subtitle_with_image', 'image_preview', 'logo_preview', 'job_time')
admin.site.register(Head, HeadAdmin)


from remont.forms import AboutForm
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
    form = AboutForm
admin.site.register(About, AboutAdmin)


class AdvBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'icon_preview')
admin.site.register(AdvBlock, AdvBlockAdmin)


class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'text_before', 'text_after',  'issue_1', 'issue_2', 'issue_3', 'issue_4', 'issue_5',
                    'issue_6', 'issue_7', 'issue_8', 'issue_9', 'issue_10', 'image_preview')
admin.site.register(ServiceItem, ServiceItemAdmin)


from remont.forms import TestimonialForm
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'testimonial')
    form = TestimonialForm
admin.site.register(Testimonial, TestimonialAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email')
    list_display_links = ('id', 'phone')
admin.site.register(Contact, ContactAdmin)


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'message')
    list_display_links = ('id', 'name', 'phone')
admin.site.register(ContactForm, ContactFormAdmin)


class CallBackFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone')
    list_display_links = ('id', 'phone')
admin.site.register(CallBackForm, CallBackFormAdmin)
