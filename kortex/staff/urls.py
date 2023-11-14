from django.urls import path
from .views import staff_list, staff_add, staff_change, staff_delete, all_positions, add_position, change_position, \
    delete_position

urlpatterns = [
    path('', staff_list, name='list'),
    path('add', staff_add, name='add'),
    path('change/<int:id>', staff_change, name='change'),
    path('change/<int:id>/delete', staff_delete, name='delete'),
    path('positions', all_positions, name='positions_list'),
    path('positions/add', add_position, name='add_position'),
    path('positions/<int:id>', change_position, name='change_position'),
    path('positions/<int:id>/delete', delete_position, name='delete_position'),
]
