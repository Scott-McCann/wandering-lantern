"""wandering_lantern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from tavern import views
from rest_framework import routers
from tavern.api import (UserViewSet, ItemViewSet, CharacterViewSet,
MeleeWeaponViewSet, RangedWeaponViewSet, ArmorViewSet, ClassViewSet, RaceViewSet, FeatsViewSet)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Classes', ClassViewSet)
router.register(r'Races', RaceViewSet)
router.register(r'Characters', CharacterViewSet)
router.register(r'Items', ItemViewSet)
router.register(r'Meleeweapons', MeleeWeaponViewSet)
router.register(r'Rangedweapons', RangedWeaponViewSet)
router.register(r'Armors', ArmorViewSet)
router.register(r'Feats', FeatsViewSet)


urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.view_index, name='index' ),
    url(r'tavern/', include('tavern.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^apidocs/', include('rest_framework_swagger.urls')),
]
