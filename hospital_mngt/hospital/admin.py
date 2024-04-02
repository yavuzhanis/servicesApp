from django.contrib import admin
from .models import Vehicle, Drıver, Admın, Atama, puanTable, Plate


#! admin sayfasında tablo gösterme

admin.site.register(Vehicle)
admin.site.register(Drıver)
admin.site.register(Admın)
admin.site.register(Atama)
admin.site.register(puanTable)
admin.site.register(Plate)
