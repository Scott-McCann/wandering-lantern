from django import forms
from .models import (Character, Race, Class, Item, Spells, Armor, RangedWeapon,
MeleeWeapon, Feats)



class ContactForm(forms.Form):
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField()

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'race','main_class', 'level',
                  'deity', 'age', 'sex', 'height', 'hair_color',
                  'experience_points','languages', 'alignment', 'background',
                  'strength', 'dexterity', 'constitution', 'intelligence',
                  'wisdom', 'charisma', 'feats', 'personality_traits',
                   'ideals','flaws', 'bonds', 'bio'
                  ]

class RaceForm(forms.ModelForm):
    class Meta:
        model = Race
        fields = ['size', 'name', 'speed', 'vision', 'str_mod',
                  'dex_mod', 'wis_mod', 'int_mod', 'cha_mod',
                  'con_mod', 'skill_prof', 'simple_melee_prof',
                  'martial_melee_prof', 'simple_ranged_prof',
                  'martial_ranged_prof', 'armor_proficiencies',
                  'Languages', 'description'
                  ]

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'hit_die', 'ability_score_improvement_levels',
                  'skill_prof', 'simple_melee_prof', 'martial_melee_prof',
                  'simple_ranged_prof', 'martial_ranged_prof',
                  'armor_prof', 'weapon_type_prof', 'description'
                  ]

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'cost', 'Denomination', 'weight', 'description']

class ArmorForm(forms.ModelForm):
    class Meta:
        model = Armor
        fields = ['name', 'cost', 'Denomination', 'armor_class',
                  'strength', 'disadvantage', 'weight'
                  ]

class RangedWeaponForm(forms.ModelForm):
    class Meta:
        model = RangedWeapon
        fields = ['name', 'type', 'damage_type', 'hit_die', 'properties',
                  'cost', 'Denomination', 'range', 'description', 'weight'
                  ]

class MeleeWeaponForm(forms.ModelForm):
    class Meta:
        model = MeleeWeapon
        fields = ['name', 'type', 'damage_type', 'hit_die', 'properties',
                  'cost','Denomination', 'range', 'description', 'weight'
                  ]
class FeatsForm(forms.ModelForm):
    class Meta:
        model = Feats
        fields = ['name', 'ability_increase', 'description']
