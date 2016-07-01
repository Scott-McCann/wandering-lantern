from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from .models import (Character, MeleeWeapon, RangedWeapon, Armor, Item,
Spells, Class, Race, ClassFeatures, Feats)

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"

class MeleeWeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeleeWeapon
        fields = "__all__"

class RangedWeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = RangedWeapon
        fields = "__all__"

class ArmorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armor
        fields = "__all__"

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"

class FeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feats
        fields = "__all__"

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class MeleeWeaponViewSet(viewsets.ModelViewSet):
    queryset = MeleeWeapon.objects.all()
    serializer_class = MeleeWeaponSerializer

class RangedWeaponViewSet(viewsets.ModelViewSet):
    queryset = RangedWeapon.objects.all()
    serializer_class = RangedWeaponSerializer

class ArmorViewSet(viewsets.ModelViewSet):
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class FeatsViewSet(viewsets.ModelViewSet):
    queryset = Feats.objects.all()
    serializer_class = FeatsSerializer
