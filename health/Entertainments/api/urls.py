from django.urls import path
from Entertainments.api.views import EntertainmentsList,UploadFileView,EntertainmentsDetail


urlpatterns = [
    path('Entertainments/',EntertainmentsList.as_view(),name='Entertainments_List'),
    path('upload_Entertainments/', UploadFileView.as_view(), name='upload-file'),
    path('Entertainments/<int:pk>',EntertainmentsDetail.as_view(),name='camera_detail'),
]