from rest_framework import serializers

from Doctor.models import Doctor



class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()



class SaveFileSerializer(serializers.Serializer):

    class Meta:
        model = Doctor
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):


    class Meta:
        model=Doctor
        fields = "__all__"