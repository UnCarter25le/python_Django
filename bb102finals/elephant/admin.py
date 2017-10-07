from django.contrib import admin
from .models import maplist,daanburglar,daanpets,daangogoro,daantemple,daannarrowroadway,daannoise,daanroomtest,daanpolice,daanfiredepart,daanpets10000,daanpetsall,tucheng5km10000,tucheng3km10000,tucheng5km,daanfuneral,daangas,daanmarkets

# Register your models here.

admin.site.register(maplist)
admin.site.register(daanburglar)
admin.site.register(daanpets)
admin.site.register(daangogoro)
admin.site.register(daantemple)
admin.site.register(daannarrowroadway)
admin.site.register(daannoise)
# admin.site.register(daansuite)
admin.site.register(daanroomtest)
admin.site.register(daanpolice)
admin.site.register(daanfiredepart)
admin.site.register(daanpets10000)
admin.site.register(daanpetsall)
admin.site.register(tucheng5km10000)
admin.site.register(tucheng3km10000)
admin.site.register(tucheng5km)
admin.site.register(daanfuneral)
admin.site.register(daanmarkets)
admin.site.register(daangas)


# class maplistAdmin(admin.ModelAdmin):
#     list_display=('mapName','mapDesc','mapLat','mapLng','mapTel','mapAddr')

# admin.site.register(maplist,maplistAdmin)

