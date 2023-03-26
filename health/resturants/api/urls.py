from django.urls import path
from resturants.api.views import ResturantsList,UploadFileView,ResturantsDetail


urlpatterns = [
    path('Resturants/',ResturantsList.as_view(),name='Resturants_List'),
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('Resturants/<int:pk>',ResturantsDetail.as_view(),name='camera_detail'),
]