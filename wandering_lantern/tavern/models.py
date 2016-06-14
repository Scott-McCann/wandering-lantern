from django.db import models
from .level import *

# Create your models here.


class SkillProficiencies(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class SimpleMelee(models.Model):
    weapon_type = models.CharField(max_length=256)

    def __str__(self):
        return self.weapon_type


class SimpleRanged(models.Model):
    weapon_type = models.CharField(max_length=256)

    def __str__(self):
        return self.weapon_type


class MartialMelee(models.Model):
    weapon_type = models.CharField(max_length=256)

    def __str__(self):
        return self.weapon_type


class MartialRanged(models.Model):
    weapon_type = models.CharField(max_length=256)

    def __str__(self):
        return self.weapon_type


class ArmorProficiency(models.Model):
    armor_type = models.CharField(max_length=256)

    def __str__(self):
        return self.armor_type


class Languages(models.Model):
    COMMON = 'CM'
    EXOTIC = "EXO"
    TYPE_CHOICES = (
        (COMMON, 'Common'),
        (EXOTIC, 'Exotic')
    )

    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Feats(models.Model):
    STRENGTH = 'STR'
    DEXTERITY = 'DEX'
    WISDOM = 'WIS'
    INTELLIGENCE = 'INT'
    CHARISMA = 'CHA'
    CONSTITUTION = "CON"
    ATTR_CHOICES = (
        (STRENGTH, 'Strength'),
        (DEXTERITY, 'Dexterity'),
        (WISDOM, 'Wisdom'),
        (INTELLIGENCE, 'Intelligence'),
        (CHARISMA, 'Charisma'),
        (CONSTITUTION, 'Constitution'),
    )
    name = models.CharField(max_length=256)

    ability_increase = models.CharField(
        max_length=256,
        choices=ATTR_CHOICES,
        null=True
    )

    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name



class Race(models.Model):

    TINY = 'T'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    HUGE = 'H'
    GARGANTUAN = 'G'
    SIZE_CHOICES = (
    (TINY, 'Tiny'),
    (SMALL, 'Small'),
    (MEDIUM, 'Medium'),
    (LARGE, 'Large'),
    (HUGE, 'Huge'),
    (GARGANTUAN, 'Gargantuan')
    )
    size = models.CharField(
        max_length=256,
        choices=SIZE_CHOICES,
        default=SMALL,
        null=False
    )

    name = models.CharField(max_length=256)
    speed = models.PositiveSmallIntegerField(default=20)
    vision = models.CharField(max_length=100, default='normal')
    str_mod = models.PositiveSmallIntegerField(default=0)
    dex_mod = models.PositiveSmallIntegerField(default=0)
    wis_mod = models.PositiveSmallIntegerField(default=0)
    int_mod = models.PositiveSmallIntegerField(default=0)
    cha_mod = models.PositiveSmallIntegerField(default=0)
    con_mod = models.PositiveSmallIntegerField(default=0)
    skill_prof = models.ManyToManyField(SkillProficiencies)
    simple_melee_prof = models.ManyToManyField(SimpleMelee)
    martial_melee_prof = models.ManyToManyField(MartialMelee)
    simple_ranged_prof = models.ManyToManyField(SimpleRanged)
    martial_ranged_prof = models.ManyToManyField(MartialRanged)
    armor_proficiencies = models.ManyToManyField(ArmorProficiency)
    Languages = models.ManyToManyField(Languages)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name





class Class(models.Model):
    D4 = "D4"
    D6 = "D6"
    D8 = "D8"
    D10 = "d10"
    D12 = "D12"
    twoD6 = '2D6'

    DIE_CHOICES = (
        (D4, 'D4'),
        (D6, 'D6'),
        (D8, 'D8'),
        (D10, 'D10'),
        (D12, 'D12'),
        (twoD6, '2D6')
    )

    name = models.CharField(max_length=256)
    hit_die = models.CharField(
        max_length=256,
        choices=DIE_CHOICES,
        default=D6, null=False
    )
    ability_score_improvement_levels = models.CommaSeparatedIntegerField(max_length=30)
    skill_prof = models.ManyToManyField(SkillProficiencies)
    simple_melee_prof = models.ManyToManyField(SimpleMelee)
    martial_melee_prof = models.ManyToManyField(MartialMelee)
    simple_ranged_prof = models.ManyToManyField(SimpleRanged)
    martial_ranged_prof = models.ManyToManyField(MartialRanged)
    armor_prof = models.ManyToManyField(ArmorProficiency)

    SIMPLE = 'Simple'
    MARTIAL = 'Martial'
    WEAPON_TYPE_CHOICES = (
        (SIMPLE, 'Simple'),
        (MARTIAL, 'Martial')
    )
    weapon_type_prof = models.CharField(
        max_length=256,
        choices=WEAPON_TYPE_CHOICES
    )
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name



class Character(models.Model):
    LAWFUL_GOOD = 'LG'
    GOOD = 'G'
    CHAOTIC_GOOD= 'CG'
    LAWFUL_NUETRAL = 'LN'
    NUETRAL = 'N'
    CHAOTIC_NUETRAL = 'CN'
    LAWFUL_EVIL = 'LE'
    EVIL = 'E'
    CHAOTIC_EVIL = 'CE'
    ALIGNMENT_CHOICES = (
        (LAWFUL_GOOD, 'Lawful Good'),
        (GOOD, 'Good'),
        (CHAOTIC_GOOD, 'Chaotic Good'),
        (LAWFUL_NUETRAL, 'Lawful Nuetral'),
        (NUETRAL, 'Nuetral'),
        (CHAOTIC_NUETRAL, 'Chaotic Nuetral'),
        (LAWFUL_EVIL, 'Lawful Evil'),
        (EVIL, 'Evil'),
        (CHAOTIC_EVIL, 'Chaotic Evil')

    )
    alignment = models.CharField(
        max_length=256,
        choices=ALIGNMENT_CHOICES,
        default=NUETRAL,
    )


    FEMALE = 'F'
    MALE = 'M'
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    sex = models.CharField(
        max_length=256,
        choices=SEX_CHOICES,
        default=MALE
    )

    ACOLYTE = 'Acolyte'
    CRIMINAL = 'Criminal'
    FOLK_HERO = 'Folk Hero'
    NOBLE = 'Noble'
    SAGE = 'Sage'
    SOILDER = 'Soilder'
    BACKGROUND_CHOICES = (
        (ACOLYTE, 'Acolyte'),
        (CRIMINAL, 'Criminal'),
        (FOLK_HERO, 'Folk Hero'),
        (NOBLE, 'Noble'),
        (SAGE, 'Sage'),
        (SOILDER, 'Soilder')
    )
    name = models.CharField(max_length=256)
    age = models.PositiveSmallIntegerField(default=25, null=False)
    hair_color = models.CharField(max_length=256)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True )
    deity = models.CharField(max_length=256)
    main_class = models.ForeignKey(
        Class,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
        )
    height = models.CharField(max_length=256)
    experience_points = models.PositiveIntegerField()
    languages = models.CharField(max_length=256)
    personality_traits = models.TextField()
    ideals = models.TextField(null=True)
    flaws = models.TextField(null=True)
    bonds = models.TextField(null=True)
    bio = models.TextField(null=True)
    feats = models.ManyToManyField(Feats)
    strength = models.PositiveSmallIntegerField(default=10)
    dexterity = models.PositiveSmallIntegerField(default=10)
    constitution = models.PositiveSmallIntegerField(default=10)
    intelligence = models.PositiveSmallIntegerField(default=10)
    wisdom = models.PositiveSmallIntegerField(default=10)
    charisma = models.PositiveSmallIntegerField(default=10)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name













class RaceFeatures(models.Model):

    level = models.IntegerField(
        choices=CHOICES,
        default=ONE,
        null=False
    )
    name = models.CharField(max_length=256)
    description = models.TextField()
    f_race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name








class ClassFeatures(models.Model):

    level = models.IntegerField(
        choices=CHOICES,
        default=ONE,
        null=False
    )
    name = models.CharField(max_length=256)
    description = models.TextField()
    f_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name






class Spells(models.Model):

    level = models.CharField(
        max_length=256,
        choices=CHOICES,
        default=ONE,
        null=False,
    )

    ABJURATION = 'Abj'
    CONJURATION = 'Conj'
    DIVINATION = 'Div'
    ENCHANTMENT = 'Ench'
    EVOCATION = 'Evo'
    ILLUSION = 'Ill'
    NECROMANCY = 'Necro'
    TRANSMUTAION = 'Trans'
    SCHOOL_CHOICES = (
        (ABJURATION, 'Abjuration'),
        (CONJURATION, 'Conjuration'),
        (DIVINATION, 'Divination'),
        (ENCHANTMENT, 'Enchantment'),
        (ILLUSION, 'Illusion'),
        (NECROMANCY, 'Necromancy'),
        (TRANSMUTAION, 'Transmutaion')
    )
    school = models.CharField(
        max_length=256,
        choices=SCHOOL_CHOICES,
        default=ABJURATION,
        null=False
    )


    name = models.CharField(max_length=256)
    duration = models.CharField(max_length=256)
    casting_time = models.CharField(max_length=256)
    range = models.CharField(max_length=256, null=True)
    v = models.BooleanField()
    s = models.BooleanField()
    m = models.BooleanField()
    component_desc = models.TextField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.name




class WeaponProperties(models.Model):
    name = models.CharField(max_length=256)


    def __str__(self):
        return self.name

class MeleeWeapon(models.Model):
    SIMPLE = 'Simple'
    MARTIAL = 'Martial'
    WEAPON_TYPE_CHOICES = (
        (SIMPLE, 'Simple'),
        (MARTIAL, 'Martial')
    )
    type = models.CharField(
        max_length=256,
        choices=WEAPON_TYPE_CHOICES,
        null=False, default=SIMPLE
        )

    BLUDGEONING = "Bludgeoning"
    PIERCING = 'Piercing'
    SLASHING = 'Slashing'
    DAMAGE_TYPE_CHOICES = (
        (BLUDGEONING, 'Bludgeoning'),
        (SLASHING, 'Slashing'),
        (PIERCING, 'Piercing')
    )
    damage_type = models.CharField(
        max_length=256,
        choices=DAMAGE_TYPE_CHOICES,
        null=False
        )

    D4 = "D4"
    D6 = "D6"
    D8 = "D8"
    D10 = "D10"
    D12 = "D12"
    twoD6 = '2D6'

    DIE_CHOICES = (
        (D4, 'D4'),
        (D6, 'D6'),
        (D8, 'D8'),
        (D10, 'D10'),
        (D12, 'D12'),
        (twoD6, '2D6')
    )
    COPPER = 'cp'
    SILVER = 'sp'
    GOLD = 'gp'
    COIN_CHOICE = (
        (COPPER, 'Cp'),
        (SILVER, 'Sp'),
        (GOLD, 'Gp')
    )

    hit_die = models.CharField(max_length=256, choices=DIE_CHOICES, null=False)
    name = models.CharField(max_length=256, null=False)
    properties = models.ManyToManyField(WeaponProperties, blank=True)
    cost = models.SmallIntegerField(null=False, default=10)
    Denomination = models.CharField(max_length=256, choices=COIN_CHOICE, default=GOLD)
    range = models.CommaSeparatedIntegerField(max_length=20, null=True, blank=True)
    weight = models.IntegerField(default=3)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name



class RangedWeapon(models.Model):
    name = models.CharField(max_length=256, default='name')
    SIMPLE = 'Simple'
    MARTIAL = 'Martial'
    WEAPON_TYPE_CHOICES = (
        (SIMPLE, 'Simple'),
        (MARTIAL, 'Martial')
    )
    type = models.CharField(
        max_length=256,
        choices=WEAPON_TYPE_CHOICES,
        null=False, default=SIMPLE
        )

    BLUDGEONING = "Bludgeoning"
    PIERCING = 'Piercing'
    SLASHING = 'Slashing'
    DAMAGE_TYPE_CHOICES = (
        (BLUDGEONING, 'Bludgeoning'),
        (SLASHING, 'Slashing'),
        (PIERCING, 'Piercing')
    )
    damage_type = models.CharField(
        max_length=256,
        choices=DAMAGE_TYPE_CHOICES,
        null=False
        )

    D4 = "D4"
    D6 = "D6"
    D8 = "D8"
    D10 = "D10"
    D12 = "D12"
    twoD6 = '2D6'

    DIE_CHOICES = (
        (D4, 'D4'),
        (D6, 'D6'),
        (D8, 'D8'),
        (D10, 'D10'),
        (D12, 'D12'),
        (twoD6, '2D6')
    )

    COPPER = 'cp'
    SILVER = 'sp'
    GOLD = 'gp'
    COIN_CHOICE = (
        (COPPER, 'Cp'),
        (SILVER, 'Sp'),
        (GOLD, 'Gp')
    )
    hit_die = models.CharField(max_length=256, choices=DIE_CHOICES, null=False)
    properties = models.ManyToManyField(WeaponProperties)
    cost = models.SmallIntegerField(null=False, default=10)
    range = models.CommaSeparatedIntegerField(max_length=20, null=True, blank=True  )
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    Denomination = models.CharField(max_length=256, choices=COIN_CHOICE, default=GOLD)
    weight = models.PositiveIntegerField(default=20)

    def __str__(self):
        return self.name




class Armor(models.Model):
    LIGHT = 'Light'
    MEDIUM= 'Medium'
    HEAVY= 'Heavy'
    SHIELD= 'Shield'
    ARMOR_TYPE_CHOICES = (
        (LIGHT, 'Light'),
        (MEDIUM, 'Medium'),
        (HEAVY, 'Heavy'),
        (SHIELD, 'Shield')
    )
    armor_type = models.CharField(
        max_length=256,
        null=False,
        choices=ARMOR_TYPE_CHOICES
    )

    SILVER = 'sp'
    GOLD = 'gp'
    COIN_CHOICE = (
        (SILVER, 'Sp'),
        (GOLD, 'Gp')
    )
    name = models.CharField(max_length=256, null=False)
    armor_class = models.PositiveIntegerField(default=12)
    strength = models.PositiveIntegerField(default=0)
    disadvantage = models.BooleanField(default=False, null=False)
    cost = models.PositiveIntegerField(default=40)
    Denomination = models.CharField(max_length=256, choices=COIN_CHOICE, default=GOLD)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    weight = models.PositiveIntegerField(default=20)


    def __str__(self):
        return self.name




class Item(models.Model):
    COPPER = 'cp'
    SILVER = 'sp'
    GOLD = 'gp'
    COIN_CHOICE = (
        (COPPER, 'Cp'),
        (SILVER, 'Sp'),
        (GOLD, 'Gp')
    )
    name = models.CharField(max_length=256, null=False)
    cost = models.PositiveIntegerField(default=2)
    Denomination = models.CharField(max_length=256, choices=COIN_CHOICE, default=GOLD)
    weight = models.PositiveIntegerField(default=2)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
