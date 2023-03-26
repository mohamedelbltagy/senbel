from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
import pandas as pd

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from Doctor.models import Doctor
from Doctor.api.serializers import DoctorSerializer,FileUploadSerializer,SaveFileSerializer



class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_excel(file)
        for _, row in reader.iterrows():
            new_file = Doctor(
                       name= row["name"],
                       telephone_number= row['telephone_number'],
                       address= row['address'],
                       locations= row['locations'],
                       features= row['features'],
                       opening_hours= row['opening_hours'],

                       )
            new_file.save()
        return Response({"status": "success"},status.HTTP_201_CREATED)



class DoctorList(APIView):
    def get(self,request):
        resturants = Doctor.objects.all()
        serializer = DoctorSerializer(resturants, many=True)
        return Response(serializer.data)

    def post(self,request):
        # this is the only field we want to update
        # model=Camera.objects.create(camera_name=request.data["camera_name"],
        #                             camera_ip=request.data["camera_ip"],
        #                             )
        # model.save()
        # req = request.data
        data={
            "name":request.data["name"],
            "telephone_number":request.data["telephone_number"],
            "address":request.data["address"],
            "locations":request.data["locations"],
            "features":request.data["features"],
            "opening_hours":request.data["opening_hours"],

        }
        serializer = DoctorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            # return Response({"message":"sucess"})


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # for i in req["user"]:
        #     data =get_object_or_404(User, pk=i)
        #     model.user.add(data)
        # return Response({"status": "success"},status.HTTP_201_CREATED)

    # def delete(self, request):
    #     Resturants.objects.all().delete()
    #     return Response({"status": "success"},status.HTTP_201_CREATED)



# update and delete
class DoctorDetail(APIView):

    def get(self,request,pk):
        model = get_object_or_404(Doctor, pk=pk)

        serializer = DoctorSerializer(model)
        return Response(serializer.data)

    def post(self, request, pk):
        # if no model exists by this PK, raise a 404 error
        model = get_object_or_404(Doctor, pk=pk)
        # this is the only field we want to update
        req = request.data

        # for i in req["user"]:
        #     data =get_object_or_404(User, pk=i)
        #     model.user.add(data)

        data = {"camera_name":req["camera_name"],
                "camera_ip":req["camera_ip"],
                "active": False,
                "emad":req["id"],
                }

        serializer = DoctorSerializer(model, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,requests,pk):
        # model = get_object_or_404(Camera, pk=pk)
        # model.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        model = get_object_or_404(Doctor, pk=pk)
        model.soft_delete = True
        model.active =False
        model.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
