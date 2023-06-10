from django.contrib import admin
from .models import Conta

@admin.register(Conta)
class contaAdmin(admin.ModelAdmin):
    pass

