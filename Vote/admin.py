from django.contrib import admin
from .models import Faculte,promotion

class tableFac(admin.ModelAdmin):
    list_display=('codeFac','denomination_extact')
class tablePromotion(admin.ModelAdmin):
    list_display=('faclte','codePromotion','denomination_exact_Promo')



admin.site.register(Faculte,tableFac)
admin.site.register(promotion,tablePromotion)