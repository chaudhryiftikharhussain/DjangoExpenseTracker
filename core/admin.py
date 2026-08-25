from django.contrib import admin
from core.models import Category, Expense


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'amount', 'description', 'category', 'date')
    list_filter = ('category',)
    search_fields = ('uuid', 'description',)
