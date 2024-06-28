from django.contrib import admin
from .models import Plantas, Insumos, Maceteros, Clientes
# Register your models here.
admin.site.register(Plantas)
admin.site.register(Insumos)
admin.site.register(Maceteros)
admin.site.register(Clientes)