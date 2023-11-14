from django.contrib import admin
from .models import Employee, Position


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'position')
    search_fields = ('surname', 'name',)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)




