import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from tupe.models import Tupe


class TupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tupe  #модель из бд
        fields = "__all__" #все поля
        # fields = ("title", "content", "cat") #поля для возвращения клиенту








#переобразование в json
# class TupeModel:
#     def __init__(self, title, content):  #передаем параметры
#         #параметры
#         self.title = title
#         self.content = content



# ---------  Сериализатор прописанны в ручную  ----------------

#сериализатор с атрибутами
# class TupeSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()    #cериализатор с числом IntegerField
#
#
#     #   create(self, validated_data) - для добавления(создания) записи (данных),
#     #   update(self, instance, validated_data) - для изменения данных
#
#
#     #функция с методом create
#     def create(self, validated_data):
#         # validated_data - словарь из проверенный данных в бд
#         return Tupe.objects.create(**validated_data)    #
#
#
#     #функция с методом update
#     def update(self, instance, validated_data):
#         #instance - ссылка на модель Tupe
#         # validated_data - словарь из проверенный данных в бд
#         # атрибуты для бд
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save() #сохраняет
#         return instance
#






#функции encode, decode более длинный способ для сериализации

# #преобразует в json формат
# def encode():
#     model = TupeModel('dresses', 'Content: guns')   #модель, передаем в скобках параметры
#     model_sr = TupeSerializer(model)#пропускаем модель через сериализатор
#     print(model_sr.data, type(model_sr.data), sep='\n') #выводим то что получилось
#     json = JSONRenderer().render(model_sr.data) #реализует в json формат
#     print(json) #выводит строку json
#
#
# #обратное преобразование
# def decode():
#     #поступление запроса от клиента в формате json
#     stream = io.BytesIO(b'{"title":"dresses","content":"Content: guns"}')
#     data = JSONParser().parse(stream)   #парсер джсон
#     serializer = TupeSerializer(data=data)#декодирование данных пепераем data
#     serializer.is_valid()#корректность принятый данных
#     print(serializer.validated_data) #декодирование строки stream
#
#
#
#
# # пробный способ
# # #ModelSerializer - серилизатор который работает с бд
# # class TupeSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Tupe
# #         fields = ('title', 'cat_id')    #поля для пользователя
#
#




