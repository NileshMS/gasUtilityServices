from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User, Services, ServiceRequest
from .forms import UserCreationForm

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'phone', 'password1', 'password2'),
        }),
    )
admin.site.register(User, CustomUserAdmin)
admin.site.register(Services)
admin.site.register(ServiceRequest)