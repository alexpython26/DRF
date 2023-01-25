"""DRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from tupe.views import *



# классы роутеров
class MyCustomRouter(routers.SimpleRouter):
    #список марщрутов
    routes = [
        routers.Route(url=r'^{prefix}$',    #шаблон маршрута
                      mapping={'get': 'list'},  #связывает тип запроса с соотв вьюсета
                      name='{basename}-list',   #название марштр
                      detail=False, #список или отдельная запись
                      initkwargs={'suffix': 'List'}),   #аргументы которые передаются в маршрут
        routers.Route(url=r'^{prefix}/{lookup}$',   #
                      mapping={'get': 'retrieve'},  #
                      name='{basename}-detail', #
                      detail=True,  #
                      initkwargs={'suffix': 'Detail'})  #
    ]



# роутер
# отличине между DefaultRouter пишется /api/v1/ (+ появляется ссылка), а в SimpleRouter /api/v1/tupe
# router = routers.DefaultRouter()    #DefaultRouter - возращает список марштрутов если есть в роутере
router = MyCustomRouter()     #SimpleRouter -
router.register(r'tupe', TupeViewSet, basename='tupe')
print(router.urls)  #выводит в терминале



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)), #http://127.0.0.1:8000/api/v1/tupe/  #связана с TupeViewSet, подк все маршруты
    # path('api/v1/tupelist/', TupeViewSet.as_view({'get': 'list'})),
    # path('api/v1/tupelist/<int:pk>/', TupeViewSet.as_view({'put': 'update'})),
    # path('api/v1/tupelist/', TupeAPIList.as_view()), #маршрут по API
    # path('api/v1/tupelist/<int:pk>/', TupeAPIList.as_view()), #маршрут по API с запросом GET
    # path('api/v1/tupelist/<int:pk>/', TupeAPIUpdate.as_view()), #изменение записи по PUT- или PATCH-запросу
    # path('api/v1/tupelist/<int:pk>/', TupeAPIDetailView.as_view()) #чтение, изменение и добавление отдельной записи
]
