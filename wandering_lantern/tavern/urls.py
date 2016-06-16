from django.conf.urls import url
from . import views

# url(r'^$', views.tavern_index, name='index' )
app_name = 'tavern'

urlpatterns = [
    url(r'^characters/$', views.view_characters, name='characters-index'),
    url(r'^characters/(?P<character_id>[0-9]+)/$', views.view_character_details, name='character_details'),

    url(r'^melee_weapon/$', views.view_melee_weapons, name='melee_weapons-index'),
    url(r'^melee_weapon/(?P<meleeweapon_id>[0-9]+)/$', views.view_melee_weapon_details, name='melee_weapon_details'),
]
