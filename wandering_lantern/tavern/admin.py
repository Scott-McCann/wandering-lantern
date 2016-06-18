from django.contrib import admin
from .models import (SkillProficiencies, SimpleMelee, SimpleRanged, MartialMelee,
MartialRanged, ArmorProficiency, Languages, Feats, Race, Class, Character, RaceFeatures,
ClassFeatures, Spells, MeleeWeapon, RangedWeapon, WeaponProperties, Armor, Item, MagicItem, Abilities)

admin.site.register(SkillProficiencies)
admin.site.register(SimpleMelee)
admin.site.register(SimpleRanged)
admin.site.register(MartialMelee)
admin.site.register(MartialRanged)
admin.site.register(ArmorProficiency)
admin.site.register(Languages)
admin.site.register(Feats)
admin.site.register(Race)
admin.site.register(Class)
admin.site.register(Character)
admin.site.register(RaceFeatures)
admin.site.register(ClassFeatures)
admin.site.register(Spells)
admin.site.register(MeleeWeapon)
admin.site.register(RangedWeapon)
admin.site.register(Armor)
admin.site.register(Item)
admin.site.register(WeaponProperties)
admin.site.register(MagicItem)
admin.site.register(Abilities)


# Register your models here.
