from django.urls import path
from Hospital.api.views import HospitalList,UploadFileView,HospitalDetail


urlpatterns = [
    path('Hospital/',HospitalList.as_view(),name='Hospital_List'),
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('Hospital/<int:pk>',HospitalDetail.as_view(),name='camera_detail'),
]