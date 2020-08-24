from django.contrib import admin
from records.models import Task, Income, Expenditure, Choice, Category

admin.site.register(Task)
admin.site.register(Choice)

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'amount', 'source', 'author', 'slug')
admin.site.register(Income, IncomeAdmin)

class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'category', 'amount', 'target', 'author', 'slug')
admin.site.register(Expenditure, ExpenditureAdmin)

admin.site.register(Category)