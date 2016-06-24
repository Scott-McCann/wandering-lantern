from django.conf.urls import url
from . import views

app_name = 'tavern'

urlpatterns = [
    url(r'^$', views.view_index, name='index' ),

    url(r'^characters/$', views.view_characters, name='characters-index'),
    url(r'^characters/(?P<character_id>[0-9]+)/$', views.view_character_details, name='character_details'),
    url(r'^characters/create/$', views.create_character_form, name='create_character'),


    url(r'^melee_weapons/$', views.view_melee_weapons, name='melee_weapons-index'),
    url(r'^melee_weapons/(?P<meleeweapon_id>[0-9]+)/$', views.view_melee_weapon_details, name='melee_weapon_details'),
    url(r'^melee_weapons/create/$', views.create_melee_weapon_form, name='create_melee_weapon'),


    url(r'^ranged_weapons/$', views.view_ranged_weapons, name='ranged_weapons-index'),
    url(r'^ranged_weapons/(?P<rangedweapon_id>[0-9]+)/$', views.view_ranged_weapon_details, name='ranged_weapon_details'),
    url(r'^ranged_weapons/create/$', views.create_ranged_weapon_form, name='create_ranged_weapon'),



    url(r'^items/$', views.view_items, name='items-index'),
    url(r'^items/(?P<item_id>[0-9]+)/$', views.view_item_details, name='item_details'),
    url(r'^items/create/$', views.create_item_form, name='create_item'),


    url(r'^armors/$', views.view_armors, name='armors-index'),
    url(r'^armors/(?P<armor_id>[0-9]+)/$', views.view_armor_details, name='armor_details'),
    url(r'^armors/create/$', views.create_armor_form, name='create_armor'),


    url(r'^classes/$', views.view_classes, name='classes-index'),
    url(r'^classes/(?P<class_id>[0-9]+)/$', views.view_class_details, name='class_details'),
    url(r'^classes/create/$', views.create_class_form, name='create_class'),


    url(r'^races/$', views.view_races, name='races-index'),
    url(r'^races/(?P<race_id>[0-9]+)/$', views.view_race_details, name='race_details'),
    url(r'^races/create/$', views.create_race_form, name='create_race'),




    url(r'^tools/diceroller/$', views.view_dice_roller, name='diceroller'),
    url(r'^tools/diceroller/(?P<roll>D[0-9]+)$', views.view_dice_roller, name='diceroller-result'),

]
