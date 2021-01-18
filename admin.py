from django.contrib import admin

# Register your models here.


from .models import PrivateMessage

admin.site.register(PrivateMessage)
