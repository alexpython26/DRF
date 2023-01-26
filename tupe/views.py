from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from tupe.models import *
from .permissions import IsAdminReadOnly
from .serializers import TupeSerializer



#лучший способ который добавляет в себя все
# ReadOnlyModelViewSet - позволяет только читать



# ListCreateAPIView - создает лист APIView в постмэне с запросом GET
# возращает список статей
class TupeAPIList(generics.ListCreateAPIView):
    queryset = Tupe.objects.all()   #ссылает список записей возвращаемых клиенту
    serializer_class = TupeSerializer   #применяет к классу queryset
    permission_classes = [IsAuthenticatedOrReadOnly]  #ограничение, только для авторизированных




# изменение записи по PUT- или PATCH-запросу
# меняет опр запись
class TupeAPIUpdate(generics.UpdateAPIView):
    queryset = Tupe.objects.all()   #ссылает список записей возвращаемых клиенту
    serializer_class = TupeSerializer   #применяет к классу queryset



 # чтение, изменение и добавление отдельной записи(GET, PUT, PATCH, DELETE-запросов)
 # удаляет записи
class TupeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tupe.objects.all()   #ссылает список записей возвращаемых клиенту
    serializer_class = TupeSerializer   #применяет к классу queryset
    permission_classes = [IsAdminReadOnly]  #доступ только для админа






# #список статей из моделей
# class TupeViewSet( mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     # если коммантить кверисет то надо в urls написать basename=tupe
#     # queryset = Tupe.objects.all()   #all - ссылает список записей возвращаемых клиенту
#     serializer_class = TupeSerializer   #применяет к классу queryset
#
#
#     #возращаем только записи которые указали в квадратных скобках
#     def get_queryset(self):
#         # список кол-во статей по id
#         pk= self.kwargs.get("pk")
#         # если не нашли id
#         if not pk:
#             return Tupe.objects.all()[:3]   #кол-во записей
#         # иначе если проверка не прошла
#         return Tupe.objects.filter(pk=pk)
#
#
#     # спиок категорий выводим, добавлем марштрут по id
#     @action(methods=['get'], detail=True)   #читаем категории, detail - возращает список катег
#     def category(self, request, pk=None): #через pk находит id категории
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': [c.name for c in cats]})   #возращает json формат
#
#




