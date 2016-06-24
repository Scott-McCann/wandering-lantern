from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .utils import get_next, get_previous, Die
from .models import (Character, MeleeWeapon, RangedWeapon, Armor, Item,
 Spells, Class, Race, ClassFeatures)
from .forms import (CharacterForm, RaceForm, ClassForm, ItemForm, ArmorForm,
MeleeWeaponForm, RangedWeaponForm, FeatsForm)

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
                'previous_id': previous_id }

    return render(request, 'tavern/character_details.html', context)

#TODO Character Forms

def create_character_form(request):
    # if request.method == 'POST':
    #     form = CharacterForm(request.POST)
    #     if form.is_valid():
    #         character = form.save()
    #         return HttpResponseRedirect('/tavern/characters/' + str(character.id))
    # else:
    #     form = CharacterForm()
    #
    # return render(request, 'tavern/create_character.html', { 'form':form })

    if request.method == 'POST':
        characterform = CharacterForm(request.POST, prefix='charcter')
        if characterform.is_valid():
            characterform.save()
    else:
        characterform = CharacterForm(prefix='character')

    if request.method == 'POST' and not characterform.is_valid():
        featsform = FeatsForm(request.POST, prefix='feats')
        characterform = CharacterForm(prefix='character')
        if featsform.is_valid():
            featsform.save()

    else:
        featsform = FeatsForm(prefix='feats')

    return render(request,
                  'tavern/create_character.html',
                  {'characterform' : characterform,
                   'featsform': featsform })





#TODO Race views
def view_races(request):

    races = Race.objects.all()
    context = { 'races': races }

    return render(request, 'tavern/races.html', context)

def view_race_details(request, race_id):

    try:
        race = Race.objects.get(id=race_id)
    except race.DoesNotExist:
        raise http404('This race has yet to be created.')

    all_things = Race.objects.all()
    next_id = get_next(all_things, race_id)
    previous_id = get_previous(all_things, race_id)

    context = { 'race': race,
                'next_id': next_id,
                'previous_id': previous_id }

    return render(request, 'tavern/race_details.html', context)
#TODO Race Forms

def create_race_form(request):
    if request.method == 'POST':
        form= RaceForm(request.POST)
        if form.is_valid():
            race = form.save()
            return HttpResponseRedirect('/tavern/races/' + str(race.id))
    else:
        form = RaceForm()

    return render(request, 'tavern/create_race.html', { 'form':form })





#TODO Class Views
def view_classes(request):

    Classes = Class.objects.all()
    context = { 'classes': Classes }

    return render(request, 'tavern/classes.html', context)

def view_class_details(request, class_id):

    try:
        cLass = Class.objects.get(id=class_id)
    except cLass.DoesNotExist:
        raise http404('This class has yet to be created.')

    features = ClassFeatures.objects.all()
    all_things = Class.objects.all()
    next_id = get_next(all_things, class_id)
    previous_id = get_previous(all_things, class_id)

    context = { 'class': cLass,
                'next_id': next_id,
                'previous_id': previous_id,
                'features': features }

    return render(request, 'tavern/class_details.html', context)


#TODO Class Forms
def create_class_form(request):
    if request.method == 'POST':
        form= ClassForm(request.POST)
        if form.is_valid():
            Class = form.save()
            return HttpResponseRedirect('/tavern/classs/' + str(Class.id))
    else:
        form = ClassForm()

    return render(request, 'tavern/create_class.html', { 'form':form })





#TODO Armor Views
def view_armors(request):

    armors =  Armor.objects.all()
    context = { 'armors': armors }

    return render(request, 'tavern/armors.html', context)

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
                'previous_id': previous_id }

    return render(request, 'tavern/armor_details.html', context)

#TODO Armor Forms
def create_armor_form(request):
    if request.method == 'POST':
        form= ArmorForm(request.POST)
        if form.is_valid():
            armor = form.save()
            return HttpResponseRedirect('/tavern/classs/' + str(armor.id))
    else:
        form = ArmorForm()

    return render(request, 'tavern/create_class.html', { 'form':form })







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
                'previous_id': previous_id }

    return render(request, 'tavern/item_details.html', context)

#TODO Item Forms
def create_item_form(request):
    if request.method == 'POST':
        form= ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return HttpResponseRedirect('/tavern/items/' + str(Item.id))
    else:
        form = ItemForm()

    return render(request, 'tavern/create_item.html', { 'form':form })






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
                'previous_id': previous_id }

    return render(request, 'tavern/melee_weapon_details.html', context)
#TODO MeleeWeapon Forms

def create_melee_weapon_form(request):
    if request.method == 'POST':
        form= MeleeWeaponForm(request.POST)
        if form.is_valid():
            item = form.save()
            return HttpResponseRedirect('/tavern/melee_weapons/' + str(meleeweapon.id))
    else:
        form = MeleeWeaponForm()

    return render(request, 'tavern/create_melee_weapon.html', { 'form':form })








#TODO RangedWeapon Views
def view_ranged_weapons(request):

    ranged_weapons = RangedWeapon.objects.all()
    context = { 'ranged_weapons': ranged_weapons }

    return render(request, 'tavern/ranged_weapons.html', context)

def view_ranged_weapon_details(request, rangedweapon_id):

    try:
        ranged_weapon = RangedWeapon.objects.get(id=rangedweapon_id)
    except ranged_weapon.DoesNotExist:
        raise http404('This ranged weapon has yet to be created.')

    all_things = RangedWeapon.objects.all()
    next_id = get_next(all_things, rangedweapon_id)
    previous_id = get_previous(all_things, rangedweapon_id)

    context = { 'ranged_weapon': ranged_weapon,
                'next_id': next_id,
                'previous_id': previous_id}

    return render(request, 'tavern/ranged_weapon_details.html', context)
#TODO RangedWeapon Forms
def create_ranged_weapon_form(request):
    if request.method == 'POST':
        form= RangedeaponForm(request.POST)
        if form.is_valid():
            item = form.save()
            return HttpResponseRedirect('/tavern/ranged_weapons/' + str(rangedweapon.id))
    else:
        form = RangedWeaponForm()

    return render(request, 'tavern/create_ranged_weapon.html', { 'form':form })









#TODO Spell Views
def view_spells(request):

    spell =  Spells.objects.all()
    context = { 'spell': spell }

    return render(request, 'tavern/spell.html', context)

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
                'previous_id': previous_id }

    return render(request, 'tavern/spell_details.html', context)

#TODO Spell Forms





def view_dice_roller(request, roll=None):
    D3 = Die.d3
    D4 = Die.d4
    D6 = Die.d6
    D8 = Die.d8
    D10 = Die.d10
    D12 = Die.d12
    D20 = Die.d20
    D30 = Die.d30
    D100 = Die.d100

    context = { 'D3': D3,
                'D4': D4,
                'D6': D6,
                'D8': D8,
                'D10': D10,
                'D12': D12,
                'D20': D20,
                'D30': D30,
                'D100': D100,
                'result': None
    }

    if roll:
        context['result'] = context[roll]

    return render(request, 'tavern/diceroller.html', context)
