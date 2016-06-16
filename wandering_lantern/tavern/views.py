from django.shortcuts import render
from django.http import Http404
from .utils import get_next, get_previous
from .models import (Character, MeleeWeapon, RangedWeapon, Armor, Item,
 Spells, Class, Race)

def view_index(request):
    return render(request, 'tavern/index.html')
#Charcter Views
def view_characters(request):

    characters =  Character.objects.all()
    context = { 'characters': characters }

    return render(request, 'tavern/characters.html', context)

def view_character_details(request, character_id):

    try:
        character = Character.objects.get(id=character_id)
    except char.DoesNotExist:
        raise http404('This character has yet to be created.')

    all_things = Character.objects.all()
    next_id = get_next(all_things, character_id)
    previous_id = get_previous(all_things, character_id)

    context = { 'character': character,
                'next_id': next_id,
                'previous_id': previous_id}

    return render(request, 'character_details.html', context)

#TODO Character Forms


#TODO Race views
def view_races(request):

    races = Race.objects.all()
    context = { 'races': races }

    return render(request, 'tavern/races.html', context)

def view_race_details(request, race_id):

    try:
        race = Race.objects.get(id=race_id)
    except char.DoesNotExist:
        raise http404('This race has yet to be created.')

    all_things = Race.objects.all()
    next_id = get_next(all_things, race_id)
    previous_id = get_previous(all_things, race_id)

    context = { 'race': race,
                'next_id': next_id,
                'previous_id': previous_id}

    return render(request, 'race_details.html', context)
#TODO Race Forms

#TODO Class Views
def view_class(request):

    Class = Class.objects.all()
    context = { 'class': Class }

    return render(request, 'tavern/class.html', context)

def view_class_details(request, class_id):

    try:
        Class = Class.objects.get(id=class_id)
    except char.DoesNotExist:
        raise http404('This class has yet to be created.')

    all_things = Class.objects.all()
    next_id = get_next(all_things, class_id)
    previous_id = get_previous(all_things, class_id)

    context = { 'class': Class,
                'next_id': next_id,
                'previous_id': previous_id}

    return render(request, 'class_details.html', context)
#TODO Class Forms

#TODO Armor Views
def view_armor(request):

    armor =  Armor.objects.all()
    context = { 'armor': armor }

    return render(request, 'tavern/armor.html', context)

def view_armor_details(request, armor_id):

    try:
        armor = Armor.objects.get(id=armor_id)
    except armor.DoesNotExist:
        raise http404('This armor has yet to be created.')

    all_things = Armor.objects.all()
    next_id = get_next(all_things, armor_id)
    previous_id = get_previous(all_things, armor_id)

    context = { 'armor': armor,
                'next_id': next_id,
                'previous_id': previous_id}

    return render(request, 'armor_details.html', context)

#TODO Armor Forms

#TODO Item Views
def view_items(request):

    items =  Item.objects.all()
    context = { 'items': items }

    return render(request, 'tavern/items.html', context)

def view_item_details(request, item_id):

    try:
        item = Item.objects.get(id=item_id)
    except item.DoesNotExist:
        raise http404('This item has yet to be created.')

    all_things = Item.objects.all()
    next_id = get_next(all_things, item_id)
    previous_id = get_previous(all_things, item_id)

    context = { 'item': item,
                'next_id': next_id,
                'previous_id': previous_id}

    return render(request, 'item_details.html', contet)
#TODO Item Forms

# MeleeWeapon Views
def view_melee_weapons(request):

    melee_weapons =  MeleeWeapon.objects.all()
    context = { 'melee_weapons': melee_weapons }

    return render(request, 'tavern/melee_weapons.html', context)

def view_melee_weapon_details(request, meleeweapon_id):

    try:
        melee_weapon = MeleeWeapon.objects.get(id=meleeweapon_id)
    except melee_weapon.DoesNotExist:
        raise http404('This melee weapon has yet to be created.')

    all_things = MeleeWeapon.objects.all()
    next_id = get_next(all_things, meleeweapon_id)
    previous_id = get_previous(all_things, meleeweapon_id)

    context = { 'melee_weapon': melee_weapon,
                'next_id': next_id,
                'previous_id': previous_id}

    return render(request, 'tavern/melee_weapon_details.html', context)
#TODO MeleeWeapon Forms

#TODO RangedWeapon Views
def view_ranged_weapon(request):

    ranged_weapon =  RangedWeapon.objects.all()
    context = { 'ranged_weapon': ranged_weapon }

    return render(request, 'tavern/ranged_weapon.html')

def view_ranged_weapon_details(request, rangedweapon_id):

    try:
        ranged_weapon = RangedWeapon.objects.get(id=ranged_weapon_id)
    except ranged_weapon.DoesNotExist:
        raise http404('This ranged weapon has yet to be created.')

    all_things = RangedWeapon.objects.all()
    next_id = get_next(all_things, ranged_weapon_id)
    previous_id = get_previous(all_things, ranged_weapon_id)

    context = { 'ranged_weapon': ranged_weapon,
                'next_id': next_id,
                'previous_id': previous_id}

    return render(request, 'ranged_weapon_details.html')
#TODO RangedWeapon Forms

#TODO Spell Views
def view_spell(request):

    spell =  Spells.objects.all()
    context = { 'spell': spell }

    return render(request, 'tavern/spell.html')

def view_spell_details(request, meleeweapon_id):

    try:
        spell = Spells.objects.get(id=spell_id)
    except spell.DoesNotExist:
        raise http404('This melee weapon has yet to be created.')

    all_things = Spells.objects.all()
    next_id = get_next(all_things, spell_id)
    previous_id = get_previous(all_things, spell_id)

    context = { 'spell': spell,
                'next_id': next_id,
                'previous_id': previous_id}

    return render(request, 'spell_details.html')
#TODO Spell Forms
