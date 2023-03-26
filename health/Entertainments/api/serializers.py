from rest_framework import serializers

from Entertainments.models import Entertainments



class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()



class SaveFileSerializer(serializers.Serializer):

    class Meta:
        model = Entertainments
        fields = "__all__"


class EntertainmentsSerializer(serializers.ModelSerializer):


    class Meta:
        model=Entertainments
        fields = "__all__"