from django.contrib import admin
from django.utils.html import format_html
from .models import HealthProgram, Client, Enrollment

admin.site.site_header = format_html('<span style="color: #ff6b6b;">HEALTH WELLNESS</span> Admin Dashboard')
admin.site.site_title = "Health Wellness Admin Portal"
admin.site.index_title = "Welcome to Health Wellness Management System"

@admin.register(HealthProgram)
class HealthProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_number', 'gender', 'date_of_birth')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'program', 'date_enrolled')
    list_filter = ('program', 'date_enrolled')