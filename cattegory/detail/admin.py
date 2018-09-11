from django.contrib import admin

from detail.models import Cattegorys


@admin.register(Cattegorys)
class CattegoryAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = (
        'species',
        'price',
        'food',
        'buy_place'
    )
