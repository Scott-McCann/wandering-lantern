from django.conf.urls import url
from . import views

app_name = 'tavern'

urlpatterns = [
    url(r'^$', views.view_index, name='index' ),

    url(r'^characters/$', views.view_characters, name='characters-index'),
    url(r'^characters/(?P<character_id>[0-9]+)/$', views.view_character_details, name='character_details'),

    url(r'^melee_weapons/$', views.view_melee_weapons, name='melee_weapons-index'),
    url(r'^melee_weapon/(?P<meleeweapon_id>[0-9]+)/$', views.view_melee_weapon_details, name='melee_weapon_details'),

    url(r'^ranged_weapons/$', views.view_ranged_weapons, name='ranged_weapons-index'),
    url(r'^ranged_weapon/(?P<rangedweapon_id>[0-9]+)/$', views.view_ranged_weapon_details, name='ranged_weapon_details'),

    url(r'^items/$', views.view_items, name='items-index'),
    url(r'^item/(?P<item_id>[0-9]+)/$', views.view_item_details, name='item_details'),

    url(r'^armors/$', views.view_armors, name='armors-index'),
    url(r'^armor/(?P<armor_id>[0-9]+)/$', views.view_armor_details, name='armor_details'),

    url(r'^classes/$', views.view_classes, name='classes-index'),
    url(r'^class/(?P<class_id>[0-9]+)/$', views.view_class_details, name='class_details'),




    url(r'^tools/diceroller/$', views.view_dice_roller, name='diceroller'),
    url(r'^tools/diceroller/(?P<roll>D[0-9]+)$', views.view_dice_roller, name='diceroller-result'),

]
