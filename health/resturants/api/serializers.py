from rest_framework import serializers

from resturants.models import Resturants



class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()



class SaveFileSerializer(serializers.Serializer):

    class Meta:
        model = Resturants
        fields = "__all__"


class ResturantsSerializer(serializers.ModelSerializer):


    class Meta:
        model=Resturants
        fields = "__all__"