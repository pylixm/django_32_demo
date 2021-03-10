# Django 3.1
from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'create_at',
        'create_at_year',
        'title',
    )

    # 老的实现方式
    # def create_at_year(self, obj: Blog) -> str:
    #     return obj.create_at.year
    # create_at_year.admin_order_field = 'create_at__year'
    # create_at_year.short_description = 'Year created'

    @admin.display(ordering='create_at__year', description='Year created')
    def create_at_year(self, obj: Blog) -> str:
        return obj.create_at.year