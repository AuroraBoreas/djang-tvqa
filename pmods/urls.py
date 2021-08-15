from .views import pmod_bom_create_view, pmod_bom_list_view, pmod_bom_update_view
from django.urls import path

app_name = 'pmods'

urlpatterns = [
    path('pmod_bom_create/', pmod_bom_create_view, name='pmod_bom_create'),
    path('pmod_bom_list/', pmod_bom_list_view, name='pmod_bom_list'),
    path('pmod_bom_list/<id>/update', pmod_bom_update_view, name='pmod_bom_update'),
]