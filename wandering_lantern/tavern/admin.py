from django.contrib import admin
from .models import (Skill_Proficiencies, Simple_Melee, Simple_Ranged, Martial_Melee,
Martial_Ranged, Armor_Proficiency, Languages, Feats, Race, Class, Character, Race_Features,
Class_Features, Spells)

admin.site.register(Skill_Proficiencies)
admin.site.register(Simple_Melee)
admin.site.register(Simple_Ranged)
admin.site.register(Martial_Melee)
admin.site.register(Martial_Ranged)
admin.site.register(Armor_Proficiency)
admin.site.register(Languages)
admin.site.register(Feats)
admin.site.register(Race)
admin.site.register(Class)
admin.site.register(Character)
admin.site.register(Race_Features)
admin.site.register(Class_Features)
admin.site.register(Spells)


# Register your models here.
