from rest_framework import serializers

from Hospital.models import Hospital



class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()



class SaveFileSerializer(serializers.Serializer):

    class Meta:
        model = Hospital
        fields = "__all__"


class HospitalSerializer(serializers.ModelSerializer):


    class Meta:
        model=Hospital
        fields = "__all__"