from django.urls import path
from Doctor.api.views import DoctorList,UploadFileView,DoctorDetail


urlpatterns = [
    path('Doctors/',DoctorList.as_view(),name='Doctors_List'),
    path('upload_Doctors/', UploadFileView.as_view(), name='upload-file'),
    path('Doctors/<int:pk>',DoctorDetail.as_view(),name='Doctors_detail'),
]