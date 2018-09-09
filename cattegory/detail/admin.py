from django.contrib import admin
from detail.models import cattegory
# Register your models here.

@admin.register(cattegory)
class cattegoryAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = (
        'species',
        'price',
        'food',
        'buy_place'
    )
