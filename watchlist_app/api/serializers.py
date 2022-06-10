
from wsgiref.validate import validator

from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform,Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ("watchlist",)
        # fields = "__all__"
    
class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watch = WatchListSerializer(many=True,read_only=True) #el mismo nombre related_name en el modelo (trae todo)
    # watch = serializers.StringRelatedField(many=True) #trae solo el __str__
    # watch = serializers.PrimaryKeyRelatedField(many=True,read_only=True) #trae solo el id
    # watch = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name="movie-detail") #devuelve la url para consultar la pk
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"        


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("name is too short")
 
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField(required=False)
    
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
#     def update(self,instance,validated_data):
#         instance.name = validated_data.get("name")
#         instance.description = validated_data.get("description")
#         instance.active = validated_data.get("active")
#         instance.save()
#         return instance
#     def validate(self,data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Title and Description should be different")
#         else:
#             return data
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value            

