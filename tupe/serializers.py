import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from tupe.models import Tupe


class TupeSerializer(serializers.ModelSerializer):
    # строчка юзер для админа чтобы можно было добавлять
    # HiddenField - скрытые поля
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Tupe  #модель из бд
        fields = "__all__" #все поля
        # fields = ("title", "content", "cat") #поля для возвращения клиенту


